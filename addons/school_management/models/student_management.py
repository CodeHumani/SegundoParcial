from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    lastname = fields.Char(string='Last Name', required=True)
    birthdate = fields.Date(string='Birthdate', required=True)
    gender = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')
    ], string='Gender', required=True)
    ci = fields.Char(string='CI')
    cellphone = fields.Char(string='Cellphone')
    tutor_principal = fields.Many2one('school.tutor', string='Tutor')
    tutor_secundary = fields.Many2one('school.tutor', string='Tutor Secundario')
    enrollment_ids = fields.One2many('school.enrollment', 'student_id', string='Enrollments')
    prueba = fields.Char(string='prueba')

class Tutor(models.Model):
    _name = 'school.tutor'
    _description = 'Tutor'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string=' Last Name', required=True)
    ci = fields.Char(string='CI')
    cellphone = fields.Char(string=' cellphone', required=True)
    email = fields.Char(string=' Email', required=True)

class Enrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    schedule_id = fields.Many2one('school.schedule', string='Schedule', required=True)
    grade = fields.Float(string='Grade', required=True)
    tutor_id = fields.Many2one('school.tutor', string='Tutor')
