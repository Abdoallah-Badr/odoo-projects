from odoo import models,fields,api,_
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name='school.student'
    _description='student model'

    name = fields.Char(string='Student name',required=True)
    age = fields.Integer(string='Age',required=True )
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',required=True)
    description=fields.Html('description')
    gpa=fields.Float('GPA')
    classroom_id=fields.Many2one('school.classroom',string='classroom')
    grade = fields.Selection([("first","First"),("second","Second"),('third',"Third"),('fourth',"Fourth"),('fifth','Fifth'),('sixth','Sixth')],string='Grade',required=True,default=False)
    grade_compute=fields.Char(readonly=True ,compute='_grade_compute')
    subjects_num=fields.Integer(string="num of subjects")
    @api.constrains('age')
    def _age_constrains(self):
        for rec in self:
            if rec.age < 6:
                raise ValidationError(_('the student is still young'))
    @api.onchange('grade')
    def _grade_compute(self):
        for rec in self:
            rec.grade_compute = rec.grade

    @api.constrains('subjects_num')
    def subjects_num_constrains(self):
        for rec in self:
            if rec.subjects_num < 6 and rec.grade_compute in ['fourth','fifth','sixth']:
                raise ValidationError(_('The subject must me more than six subjects After third grade'))