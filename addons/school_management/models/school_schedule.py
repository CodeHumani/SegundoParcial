from odoo import models, fields, api

class Schedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'
    
    teacher_id = fields.Many2one('school.teaching.load', string='Teaching Load', required=True)
    classroom_id = fields.Many2one('school.classroom', string='Classroom', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    cycle_id = fields.Many2one('school.cycle', string='Cycle', required=True) 
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    day_of_week = fields.Selection([
        ('0', 'Lunes'), 
        ('1', 'Martes'), 
        ('2', 'Miércoles'),
        ('3', 'Jueves'), 
        ('4', 'Viernes'), 
        ('5', 'Sábado'), 
        ('6', 'Domingo')],
        string='Day of the Week', required=True)

    @api.model
    def create(self, vals):
        if vals.get('start_time') >= vals.get('end_time'):
            raise UserError("El tiempo de inicio debe ser menor que el tiempo de fin.")
        
        return super(Schedule, self).create(vals)
