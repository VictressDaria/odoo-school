from odoo import fields, models


class Patient_chart(models.Model):
    _name = 'hr.hosp.patient_chart'
    _description = 'Patient chart'

    number = fields.Char(string="Card number")
    active = fields.Boolean(default=True, )
    doctor = fields.Many2many(
        comodel_name='hr.hosp.doctor',)
    diagnosis = fields.Many2many(
        comodel_name='hr.hosp.diagnosis', )
