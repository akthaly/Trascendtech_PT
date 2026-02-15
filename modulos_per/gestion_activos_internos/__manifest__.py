{
    'name': "Gestión de Activos Internos",
    'version': '1.0',
    'category': 'Recursos Humanos',
    'summary': 'Este módulo esta diseñado para manejar el control y gestión de activos internos de la empresa',
    'description': """
        Con este módulo podremos registrar, controlar y dar seguimiento a los 
        bienes físicos y digitales que forman parte de su operación diaria. """,
    'author': "Alejandro Anona",
    'depends': ['base', 'hr'],
    'data': [
        # rutas a los archivos XML de vistas, acciones, menús, etc.
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,

}