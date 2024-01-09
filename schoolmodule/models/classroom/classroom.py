from odoo import models,fields
class Classroom(models.Model):
    _name ='schoolmodule.classroom'
    _description='classroom model'
    name = fields.Char(string='Class ID',required=True)

    student_ids=fields.One2many('schoolmodule.student','classroom_id',string='students')
