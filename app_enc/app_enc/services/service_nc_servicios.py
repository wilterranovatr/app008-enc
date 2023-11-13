from datetime import datetime
from ..models.model_solicitud_nc import SolicitudNC
from ..models.model_detalle_solicitud import DetalleSolicitud

class ServiceNCServicios:

    def save_solicitud(data):
        # Solicitud NC
        tipo_nc = "SER"
        usuario_creador=1 ##
        estado = "EMITIDO"
        fecha_solicitud = data["datos_documento"]["fecha_emision_nc"]['date']
        fecha_solicitud = datetime.strptime(fecha_solicitud,'%Y-%m-%dT%H:%M:%S.%fZ')

        # Detalle
        fecha_emision = data["datos_documento"]["fecha_emision"]['date']
        fecha_emision = datetime.strptime(fecha_emision,'%Y-%m-%dT%H:%M:%S.%fZ')
        nro_comprobante= data["datos_documento"]["nro_comprobante"]
        motivo= data["datos_documento"]["motivo"]
        importe_total= data["datos_documento"]["importe_nc"]

        ## Guardando
        solicitud_nc = SolicitudNC(
            sol_fecha_solicitud=fecha_solicitud.date(),
            sol_tipo_nc=tipo_nc,
            sol_usuario_creador=usuario_creador,
            sol_fecha_creacion=datetime.now().date(),
            sol_estado=estado
        )
        solicitud_nc.save()
        #
        detalle_sol = DetalleSolicitud(
            det_fecha_emision=fecha_emision.date(),
            det_nro_comprobante=nro_comprobante,
            det_importe_total=importe_total,
            det_motivo=motivo,
            sol_id=solicitud_nc.sol_id
        )
        detalle_sol.save()