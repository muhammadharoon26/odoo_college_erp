from odoo import models, fields

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'College Department'
    
    name = fields.Char(string='Department Name', required=True)
    code = fields.Char(string='Department Code', required=True)
    head_id = fields.Many2one('college.faculty', string='Department Head')
    description = fields.Text(string='Description')
