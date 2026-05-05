"""
HATEOAS (Hypermedia as the Engine of Application State)

Proporciona _links en las respuestas para navegación.
"""

from urllib.parse import urljoin
from rest_framework.reverse import reverse


def get_base_url(request):
    """Obtiene la URL base de la API."""
    return request.build_absolute_uri('/api/v1/restaurant/')


def generate_links(request, endpoint, resource_id=None, actions=None):
    """
    Genera hipervínculos para un recurso.
    
    Args:
        request: Objeto request de Django
        endpoint: Nombre del endpoint (e.g., 'menu', 'categories')
        resource_id: ID del recurso (opcional)
        actions: Acciones adicionales disponibles
    
    Returns:
        dict: Diccionario de _links
    """
    base = get_base_url(request)
    
    links = {
        'self': {'href': f"{base}{endpoint}/"},
    }
    
    if resource_id:
        links['self'] = {'href': f"{base}{endpoint}/{resource_id}/"}
        links['collection'] = {'href': f"{base}{endpoint}/"}
    
    if actions:
        for action in actions:
            if action == 'update':
                links['update'] = {
                    'href': f"{base}{endpoint}/{resource_id}/",
                    'method': 'PUT'
                }
            elif action == 'partial_update':
                links['partial_update'] = {
                    'href': f"{base}{endpoint}/{resource_id}/",
                    'method': 'PATCH'
                }
            elif action == 'delete':
                links['delete'] = {
                    'href': f"{base}{endpoint}/{resource_id}/",
                    'method': 'DELETE'
                }
            elif action == 'create':
                links['create'] = {
                    'href': f"{base}{endpoint}/",
                    'method': 'POST'
                }
    
    return links


def add_pagination_links(request, count, page, page_size):
    """Genera enlaces de paginación."""
    base = get_base_url(request)
    pages = (count + page_size - 1) // page_size if page_size > 0 else 0
    
    links = {}
    
    if page > 1:
        links['previous'] = {
            'href': f"{base}?page={page-1}&page_size={page_size}"
        }
    
    if page < pages:
        links['next'] = {
            'href': f"{base}?page={page+1}&page_size={page_size}"
        }
    
    links['first'] = {'href': f"{base}?page=1&page_size={page_size}"}
    links['last'] = {'href': f"{base}?page={pages}&page_size={page_size}"}
    
    return links


def item_links(request, endpoint, item):
    """Genera _links para un item individual."""
    return generate_links(request, endpoint, item.get('id'))


def collection_links(request, endpoint, count, page, page_size):
    """Genera _links para una colección paginada."""
    return {
        'self': {'href': f"{request.path}?page={page}&page_size={page_size}"},
        **add_pagination_links(request, count, page, page_size)
    }