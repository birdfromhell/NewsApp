"""
Configuration file for sidebar menus based on user roles.
This file makes it easy to edit menu items without changing HTML templates.
"""

# Menu configuration for admin users (is_superuser=True)
ADMIN_MENU = [
    {
        'title': 'Dashboard',
        'icon': 'dashboard',
        'url': '/dashboard/admin/',
        'active_paths': ['/dashboard/admin/']
    },
    {
        'title': 'Manage Authors',
        'icon': 'group',
        'url': '#',
        'active_paths': ['/dashboard/authors/', '/dashboard/authors/add/'],
        'submenu': [
            {'title': 'All Authors', 'url': '/dashboard/authors/', 'active_paths': ['/dashboard/authors/']},
            {'title': 'Add Author', 'url': '/dashboard/authors/add/', 'active_paths': ['/dashboard/authors/add/']}
        ]
    },
    {
        'title': 'Manage Categories',
        'icon': 'category',
        'url': '/dashboard/categories/',
        'active_paths': ['/dashboard/categories/', '/dashboard/categories/add/']
    },
    {
        'title': 'Manage Articles',
        'icon': 'article',
        'url': '/dashboard/articles/',
        'active_paths': ['/dashboard/articles/']
    },
    {
        'title': 'Settings',
        'icon': 'settings',
        'url': '/dashboard/settings/',
        'active_paths': ['/dashboard/settings/']
    }
]

# Menu configuration for author users (is_staff=True, is_superuser=False)
AUTHOR_MENU = [
    {
        'title': 'Dashboard',
        'icon': 'dashboard',
        'url': '/dashboard/author/',
        'active_paths': ['/dashboard/author/']
    },
    {
        'title': 'My Articles',
        'icon': 'article',
        'url': '#',
        'active_paths': ['/dashboard/articles/my/', '/dashboard/articles/add/'],
        'submenu': [
            {'title': 'All Articles', 'url': '/dashboard/articles/my/', 'active_paths': ['/dashboard/articles/my/']},
            {'title': 'Add Article', 'url': '/dashboard/articles/add/', 'active_paths': ['/dashboard/articles/add/']}
        ]
    },
    {
        'title': 'Profile',
        'icon': 'person',
        'url': '/dashboard/profile/',
        'active_paths': ['/dashboard/profile/']
    }
]
