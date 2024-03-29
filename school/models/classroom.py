from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Classroom(models.Model):
    _name = 'school.classroom'
    _description = 'classroom model'
    name = fields.Char(string='Class ID', required=True)

    student_ids = fields.One2many('school.student', 'classroom_id', string='students')
    count_of_students = fields.Integer(string='students count', readonly=True, compute='_track_students_count',store=1)

    @api.depends('student_ids')
    def _track_students_count(self):
        for rec in self:
            rec.count_of_students = len(rec.student_ids)


    @api.constrains('student_ids')    # raise when store on database
    def _raise_count_exception(self):
        for rec in self:
            if len(rec.student_ids) > 3:
                raise ValidationError(_('the student count more than class capacity'))


    @api.onchange('student_ids')    # use on_change is preferable with computed field
    def _onchange_count_of_students(self):
        if self.count_of_students > 3:
            warning = {
                'title': _('Warning'),
                'message': _('The student count exceeds the class capacity. delete the records more than 20'),
            }
            return {'warning': warning}
