from odoo import models, fields, api

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    numero_uno = fields.Integer(string='Número Uno')
    numero_dos = fields.Integer(string='Número Dos')
    resultado = fields.Integer(string='Resultado', compute='_compute_resultado', store=True)

    @api.depends('numero_uno', 'numero_dos')
    def _compute_resultado(self):
        for record in self:
            record.resultado = record.numero_uno + record.numero_dos
