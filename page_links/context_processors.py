from .models import PageWidget

def page_widgets_context(request):
    """Context processor to add page widgets to all templates"""
    # Get the current page based on the URL path
    current_page = 'home'  # default
    
    if request.path.startswith('/rent/'):
        current_page = 'rent'
    elif request.path.startswith('/sale/'):
        current_page = 'sale'
    elif request.path.startswith('/events/'):
        current_page = 'events'
    elif request.path == '/':
        current_page = 'home'
    
    # Get active widgets for the current page
    page_widgets = PageWidget.objects.filter(
        page=current_page,
        is_active=True
    )
    
    return {
        'page_widgets': page_widgets,
        'current_page': current_page
    }
