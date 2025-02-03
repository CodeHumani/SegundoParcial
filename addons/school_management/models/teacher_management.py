from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'
    ci = fields.Char(string='CI')    
    _inherits = {'hr.employee': 'employee_id'}
    hola = fields.Char(string='Hola')
    
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')

class TeachingLoad(models.Model):
    _name = 'school.teaching.load'
    _description = 'Teaching Load'

    teacher_id = fields.Many2one('school.teacher', string='Teacher', required=True)
    subject_id = fields.Many2one('school.subject', string='Subject', required=True)
    hours_per_week = fields.Integer(string='Hours per Week', default=0, required=True)
    hours_total = fields.Integer(string='Hours Total', default=0, required=True)
