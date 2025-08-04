from odoo import models, fields

class CollegeFaculty(models.Model):
    _name = 'college.faculty'
    _description = 'College Faculty'
    
    name = fields.Char(string='Name', required=True)
    employee_id = fields.Char(string='Employee ID', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    department_id = fields.Many2one('college.department', string='Department')
    designation = fields.Char(string='Designation')
