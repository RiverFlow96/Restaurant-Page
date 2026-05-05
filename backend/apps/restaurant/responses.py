import os
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def error_response(message, error_type='Error', details=None, status_code=status.HTTP_400_BAD_REQUEST):
    """Respuesta de error estandarizada."""
    data = {
        'error': error_type,
        'message': message,
        'timestamp': datetime.now().isoformat(),
    }
    if details:
        data['details'] = details
    return Response(data, status=status_code)


def validation_error(details, message='Datos inválidos'):
    """Error de validación."""
    return error_response(message, 'ValidationError', details, status.HTTP_422_UNPROCESSABLE_ENTITY)


def not_found(resource, resource_id=None):
    """Error 404 - No encontrado."""
    msg = f"{resource} no encontrado"
    details = {'id': resource_id} if resource_id else None
    return error_response(msg, 'NotFound', details, status.HTTP_404_NOT_FOUND)


def forbidden(message='No tienes permiso'):
    """Error 403 - Prohibido."""
    return error_response(message, 'Forbidden', status_code=status.HTTP_403_FORBIDDEN)


def unauthorized(message='Autenticación requerida'):
    """Error 401 - No autenticado."""
    return error_response(message, 'Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)


def conflict(message, details=None):
    """Error 409 - Conflicto."""
    return error_response(message, 'Conflict', details, status.HTTP_409_CONFLICT)


def created(message, data=None):
    """Respuesta 201 - Creado."""
    response = {
        'success': True,
        'message': message,
        'timestamp': datetime.now().isoformat(),
    }
    if data:
        response['data'] = data
    return Response(response, status=status.HTTP_201_CREATED)


def success(message, data=None):
    """Respuesta 200 - Éxito."""
    response = {
        'success': True,
        'message': message,
        'timestamp': datetime.now().isoformat(),
    }
    if data:
        response['data'] = data
    return Response(response, status=status.HTTP_200_OK)


def paginated_response(results, count, page, page_size, next_url=None, previous_url=None):
    """Respuesta paginada estándar."""
    return Response({
        'count': count,
        'next': next_url,
        'previous': previous_url,
        'results': results,
        'pagination': {
            'page': page,
            'page_size': page_size,
            'pages': (count + page_size - 1) // page_size if page_size > 0 else 0
        }
    })


def custom_exception_handler(exc, context):
    """Manejador global de excepciones."""
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == 400:
            response.data = {
                'error': 'ValidationError',
                'message': 'Datos inválidos',
                'timestamp': datetime.now().isoformat(),
                'details': response.data
            }
        elif response.status_code == 401:
            response.data = {
                'error': 'Unauthorized',
                'message': 'Autenticación requerida',
                'timestamp': datetime.now().isoformat(),
            }
        elif response.status_code == 403:
            response.data = {
                'error': 'Forbidden',
                'message': 'No tienes permiso',
                'timestamp': datetime.now().isoformat(),
            }
        elif response.status_code == 404:
            response.data = {
                'error': 'NotFound',
                'message': response.data.get('detail', 'Recurso no encontrado'),
                'timestamp': datetime.now().isoformat(),
            }
        elif response.status_code >= 500:
            response.data = {
                'error': 'InternalError',
                'message': 'Error interno del servidor',
                'timestamp': datetime.now().isoformat(),
            }

    return response