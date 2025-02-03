from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class Activity(models.Model):
    _name = 'school.activity'
    _description = 'Activity'

    name = fields.Char(string='Description', required=True)
    activity_type = fields.Selection([
        ('task', 'Tarea'),
        ('sports', 'Deportes'),
        ('games', 'Juegos'),
        ('selling', 'Vender')],
        string='Tipo de Actividad', required=True)
    start_time = fields.Datetime(string='Hora de Inicio', required=True)
    end_time = fields.Datetime(string='Hora de Finalización', required=True)
    completed = fields.Boolean(string='Actividad Completada', default=False)
    schedule_id = fields.Many2one('school.schedule', string='Schedule', required=True)
    user_id = fields.Many2one('res.users', string='Assigned User', required=True, default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        activity = super(Activity, self).create(vals)
        self.send_notification(activity, 'Nueva actividad creada')
        return activity

    def write(self, vals):
        result = super(Activity, self).write(vals)
        for activity in self:
            self.send_notification(activity, 'Actividad modificada')
        return result

    def send_notification(self, activity, message):
        url = 'http://localhost:3000/send-notification'
        payload = {
            'activity_id': activity.id,
            'activity_name': activity.name,
            'message': message,
            'students': self.get_students(activity.schedule_id.id),
            'teachers': self.get_teachers(activity.schedule_id.id),
            'tutors': self.get_tutors(activity.schedule_id.id)
        }
        try:
            requests.post(url, json=payload)
        except requests.exceptions.RequestException as e:
            _logger.error(f'Error enviando notificación: {str(e)}')

    def get_students(self, schedule_id):
        students = self.env['school.enrollment'].search([('schedule_id', '=', schedule_id)]).mapped('student_id')
        return [student.id for student in students]

    def get_teachers(self, schedule_id):
        teachers = self.env['school.teaching.load'].search([('subject_id.schedule_id', '=', schedule_id)]).mapped('teacher_id')
        return [teacher.id for teacher in teachers]

    def get_tutors(self, schedule_id):
        students = self.env['school.enrollment'].search([('schedule_id', '=', schedule_id)]).mapped('student_id')
        tutors = students.mapped('tutor_principal') + students.mapped('tutor_secundary')
        return [tutor.id for tutor in tutors]
