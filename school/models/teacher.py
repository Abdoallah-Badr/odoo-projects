from odoo import models, fields, api
from datetime import datetime


class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'teacher model'

    name = fields.Char(string='Teacher name', required=True)
    age = fields.Integer(string='Age', required=True)
    courses = fields.Selection([
        ('arabic', 'Arabic'), ('math', 'Math'), ('english', 'English'), ('science', 'Science'), ('history', 'History')
    ], string="Teaching Course")
    join_date = fields.Date(string='Join date', required=True)
    teaching_period = fields.Float(string="Teaching period", readonly=True, compute="_compute_teaching_period", digits=(3, 1))
    classroom_ids = fields.Many2many('school.classroom', string='Classrooms')

    @api.depends('join_date')
    def _compute_teaching_period(self):
        for rec in self:
            if rec.join_date:
                join_date = fields.Date.from_string(rec.join_date)
                today_date = datetime.now().date()
                difference = (today_date - join_date).days
                if difference < 365:
                    rec.teaching_period = difference
                else:
                    rec.teaching_period = difference/365
            else:
                rec.teaching_period = 0
