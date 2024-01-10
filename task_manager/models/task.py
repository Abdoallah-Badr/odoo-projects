from odoo import fields,models

class Task(models.Model):
    _name='task_manager.task'
    _description='the task model for task_manager module'

    name = fields.Char(string='Task name',required=True)
    description = fields.Char(string='Task description')
    dead_line = fields.Date(string='Dead line')
    completed = fields.Boolean(string='Completed')