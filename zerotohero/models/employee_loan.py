from odoo import models, fields, api
import xlsxwriter
import base64
from io import BytesIO
from dateutil.relativedelta import relativedelta


class EmployeeLoan(models.Model):
    _name = 'employee.loan'
    _description = 'Employee Loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    emp_name = fields.Many2one('hr.employee', string='Employee', required=True)
    loan_amount = fields.Integer(string='Loan Amount', required=True)
    emi_amount = fields.Float(string='EMI Amount', required=True)
    date = fields.Date(default=fields.Date.today, string='Date')
    loan_line_ids = fields.One2many('employee.loan.line', 'loan_id', string='Repayment Amounts', readonly=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', "Cancel")], string='Status', default='draft'
    )
    employee_image = fields.Binary(related='emp_name.image_1920', string="Employee Image")
    department=fields.Many2one(related='emp_name.department_id',string='Department')





    def action_send_email(self):
        template = self.env.ref('zerotohero.name_email_template')
        if template:
            template.send_mail(self.id, force_send=True)
        return True




    def calculate_repayment_lines(self):
        self.loan_line_ids.unlink()
        for record in self:
            total_emi_count = record.loan_amount // record.emi_amount
            lines = []
            emi_date = fields.Date.today()
            for i in range(int(total_emi_count)):
                emi_date_with_months = emi_date + relativedelta(months=i)
                lines.append((0, 0, {'emi_number': i + 1, 'repayment_amount': record.emi_amount, 'emi_date': emi_date_with_months,'paid': False,}))
            record.loan_line_ids = lines
    def action_confirm_form(self):
        for rec in self:
            rec.status = 'confirm'


    def action_cancel_form(self):
        for rec in self:
            rec.status = 'cancel'


    def action_open_wizard(self):
        action = self.env['ir.actions.act_window']._for_xml_id('zerotohero.emi_wizard_action')
        # action = self.env.ref("zerotohero.emi_wizard_action")
        # return action

        return {
            'type': 'ir.actions.act_window',
            'name': 'Unpaid EMIs for Selected Month',
            'res_model': 'emi.filter.wizard',
            'view_mode': 'form',

            'target': 'new',
        }




    def send_email_to_employee(self):
        # Retrieve the employee's email address
        employee_email = self.emp_name.work_email
        if not employee_email:
            raise ValueError("Employee does not have an email address.")

        # Create the Excel file for the EMI lines
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('EMI Schedule')

        # Write headers in the Excel file
        worksheet.write(0, 0, 'Serial Number')
        worksheet.write(0, 1, 'EMI Amount')
        worksheet.write(0, 2, 'EMI Date')

        # Write EMI lines to the Excel file
        row = 1
        for emi_line in self.loan_line_ids:  # Loop through loan_line_ids (the One2many field)
            worksheet.write(row, 0, emi_line.emi_number)
            worksheet.write(row, 1, emi_line.repayment_amount)
            worksheet.write(row, 2, emi_line.emi_date.strftime('%Y-%m-%d'))  # Format date
            row += 1

        # Close the workbook to save the Excel file
        workbook.close()
        output.seek(0)

        # Create an attachment for the Excel file
        attachment = self.env['ir.attachment'].create({
            'name': f'EMI_Schedule_{self.emp_name.name}.xlsx',
            'type': 'binary',
            'datas': base64.b64encode(output.read()),  # Base64 encode the content
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'res_model': 'employee.loan',
            'res_id': self.id,
        })

        # Prepare the email content
        subject = "Loan Information and EMI Schedule"
        body = f"""
        <p>Dear {self.emp_name.name},</p>
        <p>Please find attached the EMI schedule for your loan.</p>
        <p><b>Loan Amount:</b> {self.loan_amount}</p>
        <p><b>EMI Amount:</b> {self.emi_amount}</p>
        <p><b>Status:</b> {self.status}</p>
        <p>Best Regards,<br>Your Company</p>
        """

        # Create the email with attachment
        mail_values = {
            'subject': subject,
            'body_html': body,
            'email_to': employee_email,
            'attachment_ids': [(4, attachment.id)],
        }
        mail = self.env['mail.mail'].create(mail_values)
        mail.send()

        # Post the attachment in the chatter
        self.message_post(
            body="The EMI schedule Excel file has been sent to the employee.",
            subject="EMI Schedule Sent",
            message_type="notification",
            attachment_ids=[attachment.id],
            subtype_id=self.env.ref('mail.mt_comment').id
        )

    # Method to trigger email sending manually from a button
    def action_send_email_with_attachment(self):
        for loan in self:
            loan.send_email_to_employee()





