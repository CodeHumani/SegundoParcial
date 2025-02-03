from odoo import models, fields

class PaymentPlan(models.Model):
    _name = 'school.paymentplan'
    _description = 'school.paymentplan'

    name = fields.Char(string='Payment Plan Name', required=True)
    description = fields.Char(string='Payment Plan Description', required=True)
    amount_plan = fields.Integer(string='Payment Plan Amount', required=True)
    
class StudentPlan(models.Model):
    _name = 'school.studentplan'
    _description = 'school.studentplan'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    paymentplan_id = fields.Many2one('school.paymentplan', string='Payment Plan', required=True)
    date_save = fields.Date(string='date', required=True)
    
class Payments(models.Model):
    _name = 'school.payments'
    _description = 'school.payments'

    date_payment = fields.Date(string='Date Payment', required=True)
    total_amount = fields.Float(string='Total Amount', required=True)
    # student_name = fields.Many2one('school.student', string='Student Name', required=True)
    paymentplanstudent_id = fields.Many2one('school.studentplan', string='Payment Student Plan', required=True)