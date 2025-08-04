# -*- coding: utf-8 -*-
from odoo import models, fields

class CollegeCourse(models.Model):
    _name = 'college.course'
    _description = 'College Course'
    
    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    duration = fields.Integer(string='Duration (Years)')
    description = fields.Text(string='Description')
