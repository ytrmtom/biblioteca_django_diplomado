

def validar_isbn(isbn):
    if len(isbn) != 13:
        raise serializers.ValidationError('El ISBN debe tener 13 caracteres') 
    
def validar_fecha_publicacion(fecha_publicacion):
    if fecha_publicacion > datetime.now().date():
        raise serializers.ValidationError('La fecha de publicacion no puede ser mayor a la fecha actual')
    
def validar_estado(estado):
    if estado not in [True, False]:
        raise serializers.ValidationError('El estado debe ser True o False')

def validar_fecha_devolucion(fecha_devolucion):
    if fecha_devolucion < datetime.now().date():
        raise serializers.ValidationError('La fecha de devolucion no puede ser menor a la fecha actual')

def validar_fecha_prestamo(fecha_prestamo):
    if fecha_prestamo > datetime.now().date():
        raise serializers.ValidationError('La fecha de prestamo no puede ser mayor a la fecha actual')
