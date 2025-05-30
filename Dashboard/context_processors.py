from django.template.defaultfilters import safe
from .menu_config import ADMIN_MENU, AUTHOR_MENU

def sidebar_menu(request):
    """
    Context processor that provides the appropriate sidebar menu based on user role
    """
    if not request.user.is_authenticated:
        return {'sidebar_menu': []}
        
    menu_items = []
    
    # Determine which menu to use based on user role
    if request.user.is_superuser:
        menu_items = ADMIN_MENU
    elif request.user.is_staff:
        menu_items = AUTHOR_MENU
    
    # Check for active menu items based on current path
    for item in menu_items:
        if request.path in item.get('active_paths', []):
            item['is_active'] = True
            
        # Check submenu items
        if 'submenu' in item:
            for submenu in item['submenu']:
                if request.path in submenu.get('active_paths', []):
                    submenu['is_active'] = True
                    item['is_open'] = True
    
    return {'sidebar_menu': menu_items}
