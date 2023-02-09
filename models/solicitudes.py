# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError
import smtplib


class LmBusquedas(models.Model):
    _name = "lm.busquedas"
    _description = "Litoral Movil Busquedas"

    def _default_stage_id(self):
        if 1 == 1:
            return self.env['lm.busquedas.stage'].search([
                ('id', '=', '4')
            ], order='sequence asc', limit=1).id
        return False
    
    
       
        
    user_id: fields.Many2one(
        'res.users', 'User', help="The user responsible for this journal")
    nombre_usuario_actual = fields.Char(
        string="Nombre del Usuario", default=lambda self: self.env.user.login)
    nom_sol = fields.Char('Nombre de Solicitante', required=True)
    puesto = fields.Selection(
        [('SUPERVISORA CALL CENTER', 'SUPERVISORA CALL CENTER'),
         ('ANALISTA DE RECL.Y SELECCION', 'ANALISTA DE RECL.Y SELECCION'),
         ('VENDEDOR TERRENO', 'VENDEDOR TERRENO'),
         ('SUPERVISOR', 'SUPERVISOR'),
         ('CAMINANTE', 'CAMINANTE'),
         ('EJECUTIVO VENTAS', 'EJECUTIVO VENTAS'),
         ('BACK OFFICE', 'BACK OFFICE'),
         ('TECNICO INSTALADOR', 'TECNICO INSTALADOR'),
         ('PAÑOL', 'PAÑOL'),
         ('JEFE OPERATIVO', 'JEFE OPERATIVO'),
         ('AYUDANTE DE DEPOSITO', 'AYUDANTE DE DEPOSITO'),
         ('GERENTE DE INSTALACIONES', 'GERENTE DE INSTALACIONES'),
         ('JEFE DE DEPOSITO', 'JEFE DE DEPOSITO'),
         ('MESA DE DESPACHO', 'MESA DE DESPACHO'),
         ('ANALISTA', 'ANALISTA'),
         ('COORDINADOR', 'COORDINADOR'),
         ('ADMINISTRATIVO', 'ADMINISTRATIVO'),
         ('EJECUTIVO DE BAF', 'EJECUTIVO DE BAF'),
         ('EJECUTIVO DE CUENTAS', 'EJECUTIVO DE CUENTAS'),
         ('VENDEDOR MAYORISTA', 'VENDEDOR MAYORISTA'),
         ('VENDEDOR LOCAL', 'VENDEDOR LOCAL'),
         ('TESORERO', 'TESORERO'),
         ('GERENTE', 'GERENTE'),
         ('ANALISTA DE CAPAC. Y DESARR.', 'ANALISTA DE CAPAC. Y DESARR.'),
         ('VENDEDOR/A', 'VENDEDOR/A'),
         ('APP REFERIDOS', 'APP REFERIDOS'),
         ('PASANTE', 'PASANTE'),
         ('ANALISTA GENERALISTA', 'ANALISTA GENERALISTA'),
         ('PROMOTOR', 'PROMOTOR'),
         ('SEGURIDAD', 'SEGURIDAD'),
         ('BACK UP', 'BACK UP'),
         ('CADETE', 'CADETE'),
         ('ANALISTA PAYROLL', 'ANALISTA PAYROLL'),
         ('ANALISTA DE ADM. DE PERSONAL', 'ANALISTA DE ADM. DE PERSONAL'),
         ('AUXILIAR PAYROLL', 'AUXILIAR PAYROLL'),
         ('MAESTRANZA', 'MAESTRANZA'),
         ('ADMINISTRATIVA CUENTAS A PAGAR', 'ADMINISTRATIVA CUENTAS A PAGAR'),
         ('ANALISTA DE DATOS', 'ANALISTA DE DATOS'),
         ('ANALISTA CONTABLE', 'ANALISTA CONTABLE'),
         ('VENDEDOR DE TERRENO', 'VENDEDOR DE TERRENO'),
         ('TELEMARKETER', 'TELEMARKETER')],
        'Puesto a Cubrir', default='CADETE', required=True)
    motivo = fields.Selection(
        [('incremento', 'Incremento'),
         ('reemplazo', 'Reemplazo'),
         ('reemplazo_incremento', 'Reemplazo e Incremento')],
        'Motivo de la Busqueda', default='incremento', required=True)
    reemplazo_de = fields.Char('En reemplazo de')
    cantidad = fields.Integer('Cantidad de Vacantes a cubrir', required=True)
    reporta_a = fields.Char('Supervisor', required=True)
    convenio = fields.Selection(
        [('comer_vend_B', 'Empleado de comercio vendedor B'),
         ('comer_aux_b', 'Empleado de comercio auxiliar B'),
         ('comer_admin_b', 'Empleado de comercio administrativo B'),
         ('comer_maes_a', 'Empleado de comercio maestranza A'),
         ('uocra_ayu', 'UOCRA Ayudante'),
         ('uocra_med_of', 'UOCRA Medio Oficial'),
         ('uocra_of', 'UOCRA Oficial'),
         ('uocra_of_especializado', 'UOCRA Oficial Especializado'),
         ('fuera_convenio', 'Fuera de Convenio')],
        'Convenio', default='comer_vend_B', required=True)
    tipo_busqueda = fields.Selection(
        [('interna', 'Interna'),
         ('externa', 'Externa'),
         ('mix', 'Mix')],
        'Tipo de Busqueda', default='externa', required=True)
    f_ingreso = fields.Date('Fecha de Ingreso', required=True)
    jornada = fields.Selection(
        [('70', '70'),
         ('80', '80'),
         ('100', '100'),
         ('125', '125'),
         ('138', '138'),
         ('150', '150'),
         ('200', '200')],
        'Jornada', default='200', required=True)
    gcia_aprobacion = fields.Selection(
        [('rrhh', 'RRHH'),
         ('comercial', 'Comercial'),
         ('distribucion', 'Distribución'),
         ('administracion', 'Administración')],
        'Gcia. Aprobación', default='comercial', required=True)
    centro_costo = fields.Selection(
        [('TECHMOVIL - GENERAL', 'TECHMOVIL - GENERAL'),
         ('TECHMOVIL-AMBA-GENERAL', 'TECHMOVIL-AMBA-GENERAL'),
         ('TECHMOVIL-AMBA-INSTALACIÓN HORIZONTAL',
          'TECHMOVIL-AMBA-INSTALACIÓN HORIZONTAL'),
         ('TECHMOVIL-ROSARIO-INSTALACIÓN HORIZONTAL',
          'TECHMOVIL-ROSARIO-INSTALACIÓN HORIZONTAL'),
         ('TECHMOVIL-ROSARIO- DESPLIEGUE VERTICAL',
          'TECHMOVIL-ROSARIO- DESPLIEGUE VERTICAL'),
         ('TECHMOVIL-ROSARIO- MANTENIMIENTO', 'TECHMOVIL-ROSARIO- MANTENIMIENTO'),
         ('BAF LISU - COMERCIAL', 'BAF LISU - COMERCIAL'),
         ('BAF LISU - GENERAL', 'BAF LISU - GENERAL'),
         ('BAF LINO - GENERAL', 'BAF LINO - GENERAL'),
         ('BAF LINO - COMERCIAL', 'BAF LINO - COMERCIAL'),
         ('BAF-CABA-GENERAL', 'BAF-CABA-GENERAL'),
         ('BAF- CABA- COMERCIAL', 'BAF- CABA- COMERCIAL'),
         ('CALL LINO - COMERCIAL', 'CALL LINO - COMERCIAL'),
         ('CALL LINO - GENERAL', 'CALL LINO - GENERAL'),
         ('CALL LISU - COMERCIAL', 'CALL LISU - COMERCIAL'),
         ('CALL - CABA - COMERCIAL', 'CALL - CABA - COMERCIAL'),
         ('CALL- GENERAL', 'CALL- GENERAL'),
         ('CANAL DIGITAL - TECHSTORE', 'CANAL DIGITAL - TECHSTORE'),
         ('CANAL DIGITAL - CLARO', 'CANAL DIGITAL - CLARO'),
         ('CANAL DIGITAL - MAYORISTAS', 'CANAL DIGITAL - MAYORISTAS'),
         ('CANAL DIGITAL - GENERAL', 'CANAL DIGITAL - GENERAL'),
         ('ADMINISTRACION - ADMINISTRACIÓN', 'ADMINISTRACION - ADMINISTRACIÓN'),
         ('ADMINISTRACION - ADV BAF', 'ADMINISTRACION - ADV BAF'),
         ('ADMINISTRACION - LOGÍSTICA', 'ADMINISTRACION - LOGÍSTICA'),
         ('ADMINISTRACION - ADV GENERAL', 'ADMINISTRACION - ADV GENERAL'),
         ('ADMINISTRACION - LOGISTICA', 'ADMINISTRACION - LOGISTICA'),
         ('ADMINISTRACION - RRHH', 'ADMINISTRACION - RRHH'),
         ('ADMINISTRACION - ADV CALL', 'ADMINISTRACION - ADV CALL'),
         ('GM-PASO DEL BOSQUE', 'GM-PASO DEL BOSQUE'),
         ('GM-MOTOROLA ALTO', 'GM-MOTOROLA ALTO'),
         ('GM-HIPER LIBERTAD', 'GM-HIPER LIBERTAD'),
         ('LOCALES - LISU -CORDOBA PEATONAL', 'LOCALES - LISU -CORDOBA PEATONAL'),
         ('LOCALES - LISU - HIPER', 'LOCALES - LISU - HIPER'),
         ('LOCALES LISU- ALTO ROSARIO', 'LOCALES LISU- ALTO ROSARIO'),
         ('LOCALES LISU - SAN MARTIN', 'LOCALES LISU - SAN MARTIN'),
         ('LOCALES - LINO - CLORINDA', 'LOCALES - LINO - CLORINDA'),
         ('LOCALES - LINO - RESISTENCIA', 'LOCALES - LINO - RESISTENCIA'),
         ('LOCALES - LINO - PIRANÉ', 'LOCALES - LINO - PIRANÉ'),
         ('LINEA-COMERCIALIZACION', 'LINEA-COMERCIALIZACION'),
         ('INEA-GENERAL', 'LINEA-GENERAL'),
         ('REFERIDOS - LISU', 'REFERIDOS - LISU'),
         ('REFERIDOS - LINO', 'REFERIDOS - LINO'),
         ('REFERIDOS - GENERAL', 'REFERIDOS - GENERAL'),
         ('DISTRIBUCIÓN - LISU - COMERCIAL', 'DISTRIBUCIÓN - LISU - COMERCIAL'),
         ('DISTRIBUCIÓN - LINO - COMERCIAL', 'DISTRIBUCIÓN - LINO - COMERCIAL'),
         ('DISTRIBUCIÓN - LINO - GENERAL', 'DISTRIBUCIÓN - LINO - GENERAL'),
         ('DISTRIBUCIÓN - GENERAL', 'DISTRIBUCIÓN - GENERAL'),
         ('DISTRIBUCIÓN - CABA - COMERCIAL', 'DISTRIBUCIÓN - CABA - COMERCIAL'),
         ('DISTRIBUCIÓN - LISU - GENERAL', 'DISTRIBUCIÓN - LISU - GENERAL'),
         ('DISTRIBUCIÓN - CABA - GENERAL', 'DISTRIBUCIÓN - CABA - GENERAL')],
        'Centro de Costo', default='DISTRIBUCIÓN - CABA - GENERAL', required=True)
    razon_social = fields.Selection(
        [('Litoral Movil SRL', 'Litoral Movil SRL'),
         ('Lino Movil SRL', 'Lino Movil SRL'),
         ('Linea Movil SRL', 'Linea Movil SRL'),
         ('Tech Movil SRL', 'Tech Movil SRL'),
         ('Grupo Movil SRL', 'Grupo Movil SRL'),
         ('Amba Movil SRL', 'Amba Movil SRL')],
        'Razón Social', default='Litoral Movil SRL', required=True)
    perfil_site = fields.Selection(
        [('No', 'No'),
         ('BackOffice Fibra', 'BackOffice Fibra'),
         ('Supervisor', 'Supervisor'),
         ('Supervisor Terreno', 'Supervisor Terreno'),
         ('Supervisor Resistencia', 'Supervisor Resistencia'),
         ('Vendedor Call Center Rosario', 'Vendedor Call Center Rosario'),
         ('Supervisor Call Center Rosario', 'Supervisor Call Center Rosario'),
         ('Supervisor Call Center Resistencia',
          'Supervisor Call Center Resistencia'),
         ('BackOffice Porta Resistencia', 'BackOffice Porta Resistencia'),
         ('Vendedor Call Center Resistencia', 'Vendedor Call Center Resistencia'),
         ('Vendedor Canal Digital', 'Vendedor Canal Digital'),
         ('Vendedor Terreno Rosario', 'Vendedor Terreno Rosario'),
         ('Vendedor Terreno Resistencia', 'Vendedor Terreno Resistencia'),
         ('BackOffice Porta Rosario', 'BackOffice Porta Rosario'),
         ('Cotizador', 'Cotizador'),
         ('Back Office BAFE', 'Back Office BAFE'),
         ('Vendedor Terreno Caba', 'Vendedor Terreno Caba'),
         ('Vendedor Call Center CABA', 'Vendedor Call Center CABA'),
         ('vendedor referidos', 'vendedor referidos'),
         ('Vendedor BAFE Terreno CABA', 'Vendedor BAFE Terreno CABA'),
         ('Supervisor Terreno Caba', 'Supervisor Terreno Caba'),
         ('Banco Santa Fe', 'Banco Santa Fe'),
         ('RRHH', 'RRHH')],
        'Perfil para Site', default='No', required=True)
    perfil_caddis = fields.Selection(
        [('No', 'No'),
         ('Admin. Contable', 'Admin. Contable'),
         ('Admin. Tesoreria', 'Admin. Tesoreria'),
         ('BackOffice', 'BackOffice'),
         ('Coordinador Locales', 'Coordinador Locales'),
         ('Logistica', 'Logistica'),
         ('Vendedor', 'Vendedor')],
        'Perfil para Caddis', default='No', required=True)
    perfil_ammo = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Perfil para Ammo', default='No', required=True)
    perfil_stealth = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Perfil para STEALTH', default='No', required=True)
    demo = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Demo', default='No', required=True)
    notebook = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Computadora', default='No', required=True)
    remera = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Remera', default='No', required=True)
    campera = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Campera (BAF- DISTRIBUCIÓN)', default='No', required=True)
    linea = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Linea', default='No', required=True)
    mochila = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Mochila', default='No', required=True)
    credencial = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Credencial', default='No', required=True)
    mail = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Mail', default='No', required=True)
    ticket_card = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'Ticket Card', default='No', required=True)
    elementos_tr = fields.Selection(
        [('No', 'No'),
         ('Si', 'Si')],
        'NO se le debe entregar elementos de trabajo', default='No', required=True)
    is_done = fields.Boolean('Esta Hecho')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
         ('blocked', 'Blocked'),
         ('done', 'Ready for next stage')],
        'Kanban State', default='normal')
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority', default='1')
    color = fields.Integer('Color Index')
    stage_id = fields.Many2one('lm.busquedas.stage', 'Stage', ondelete='restrict',
                               tracking=True, copy=False, index=True, default=_default_stage_id)

    state = fields.Selection([('ped_bsc', 'Pedido de Busqueda'), ('bsc_autorizada', 'Busqueda Autorizada'), ('bsc_rechazada', 'Busqueda Rechazada'), (
        'bsc_progreso', 'Busqueda en Progreso'), ('bsc_finalizada', 'Busqueda Finalizada')], default='ped_bsc', string="Status",  group_expand='_expand_states', index=True)
    notificacion=fields.Char('Esta Busqueda se ha Notificado', default='no')

    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    _defaults = {
        'user_id': lambda self, cr, uid, context: uid,
    }

    def activar_busqueda(self):
        self._cr.execute(
            """  UPDATE hr_job SET state = 'recruit', expected_employees =%s, no_of_recruitment=%s  WHERE name =%s""", (self.cantidad, self.cantidad, self.puesto))
    def notificacion_busqueda(self):
        remitente = "diegoruiz9220@gmail.com"
        
        receptor=""
        
        if self.gcia_aprobacion == 'rrhh':
            receptor = "diegoruiz1984@gmail.com"
            mensaje = "Tiene una busqueda pendiente de aprobacion "+self.puesto
               
        elif self.gcia_aprobacion == 'comercial':
            receptor = "diegoruiz1984@gmail.com"
            mensaje = "Tiene una busqueda pendiente de aprobacion "+self.puesto
                
        elif self.gcia_aprobacion == 'distribucion':
            receptor = "diegoruiz1984@gmail.com"
            mensaje = "Tiene una busqueda pendiente de aprobacion "+self.puesto
              
        elif self.gcia_aprobacion == 'administracion':
            receptor = "diegoruiz1984@gmail.com"
            mensaje = "Tiene una busqueda pendiente de aprobacion "+self.puesto
          
        smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(user="diegoruiz9220@gmail.com", password="zbjztubwvbtivsbo")
        smtpObj.sendmail(remitente, receptor, mensaje)
        self.notificacion='si'