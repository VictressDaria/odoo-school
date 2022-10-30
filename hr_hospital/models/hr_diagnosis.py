from odoo import fields, models


class Diagnosis(models.Model):
    _name = 'hr.hosp.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    active = fields.Boolean(default=True, )
