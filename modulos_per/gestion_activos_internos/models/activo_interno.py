from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Modelo para gestion de activos internos
class ActivoInterno(models.Model):
    _name = 'gestion.activo.interno'
    _description = 'Modelo para gestionar activos internos'


    nombre = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código Interno', required=True)

    tipo = fields.Selection([
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('licencia', 'Licencia'),
        ('impresora', 'Impresora'),
        ('otro', 'Otro'),
    ], string='Tipo de Activo', required=True)

    empleado_asignado = fields.Many2one('hr.employee', string='Empleado Asignado')
    fecha_asignacion = fields.Date(string='Fecha de Asignación')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('asignado', 'Asignado'),
        ('en_reparacion', 'En reparación'),
    ], string='Estado', default='disponible', required=True)

    # Define una restricción para SQL que asegura que el código interno sea único
    _sql_constraints = [
        ('codigo_unico', 'UNIQUE(codigo)', 'El código interno ya está en uso. Por favor, ingrese un código único.')
    ]

    @api.constrains('estado', 'empleado_asignado')
    def _check_estado_empleado(self):
        for record in self:
            if record.estado == 'asignado' and not record.empleado_asignado:
                raise ValidationError("Si el estado es 'Asignado', debe tener un empleado asignado.")
            if record.estado == 'disponible' and record.empleado_asignado:
                raise ValidationError("Si el estado es 'Disponible', no debe tener un empleado asignado.")