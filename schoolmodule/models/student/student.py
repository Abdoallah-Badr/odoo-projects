from odoo import models,fields

class Student(models.Model):
    _name='schoolmodule.student'
    _description='student model'

    name = fields.Char(string='Student name',required=True)
    age = fields.Integer(string='Age',required=True )
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender')
    description=fields.Html('description')
    gpa=fields.Float('GPA')

    classroom_id=fields.Many2one('schoolmodule.classroom',string='classroom')
