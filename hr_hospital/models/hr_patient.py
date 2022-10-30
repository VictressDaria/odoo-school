from odoo import fields, models


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    patient_dob = fields.Date(string="Date of Birth")
    gender = fields.Selection([('Male', 'Male'),
                               ('Female', 'Female'),
                               ('Other', 'Other')], )
    address = fields.Text()
