# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'
    
    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    date_of_birth = fields.Date(string='Date of Birth')
    admission_date = fields.Date(string='Admission Date')
    gender = fields.Selection([
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
    ], string='Gender')

    age = fields.Integer(string='Age', compute='_compute_age')
    mobile = fields.Char(string='Mobile')
    address = fields.Text(string='Address')

    course_id = fields.Many2one('college.course', string='Course')
    department_id = fields.Many2one('college.department', string='Department')

@api.depends('date_of_birth')
def _compute_age(self):
    for student in self:
        if student.date_of_birth:
            today = fields.Date.today()
            student.age = today.year - student.date_of_birth.year
        else:
            student.age = 0
