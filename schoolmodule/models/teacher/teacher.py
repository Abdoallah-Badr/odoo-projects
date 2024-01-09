from odoo import models,fields
class Teacher(models.Model):
    _name='schoolmodule.teacher'
    _description='teacher model'

    name = fields.Char(string='Teacher name', required=True)
    age = fields.Integer(string='Age', required=True)
    courses = fields.Selection([
        ('arabic','Arabic'), ('math','Math'), ('english','English'), ('science','Science')
    ],string="Teaching Course")

    classroom_ids=fields.Many2many('schoolmodule.classroom',string='Classrooms')
