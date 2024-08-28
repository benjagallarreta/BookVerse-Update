import locale
from decimal import Decimal

def totalCarrito(request):
    total = Decimal('0.00')
    if request.session.get("carrito"):
        for key, value in request.session["carrito"].items():
            total += Decimal(value.get("Acumulado", '0.00'))
    
    # Configurar la localización a una convención específica
    locale.setlocale(locale.LC_ALL, 'es_ES.utf8')  # Configura la localización adecuada para España
    
    # Formatear el número según la localización configurada
    total_formateado = locale.format_string("%.2f", total, grouping=True)
    #LAS 2 LINEAS DE ARRIBA ES PARA EL FORMATO DEL PRECIO DEL CARRITO
    
    return {"totalCarrito": total_formateado}

#ESTE SCRIP SIRVE PARA MANEJAR EL PRECIO DEL CARRITO
