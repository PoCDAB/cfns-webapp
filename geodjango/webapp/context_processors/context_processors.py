def header_context(request):
    nav_menu = {}
    nav_menu['nav_menu'] = {}
    nav_menu['nav_menu']['home'] = 'Home'
    nav_menu['nav_menu']['geoview'] = 'GIS'
    nav_menu['nav_menu']['send-dab'] = 'Verstuur DAB+'
    nav_menu['nav_menu']['about'] = 'Over CFNS'
    nav_menu['nav_menu']['contact'] = 'Bericht ons'
    return nav_menu