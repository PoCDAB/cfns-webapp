# Define the nav menu of the webapplication, located at the header
def header_context(request):
    nav_menu = {}
    nav_menu['nav_menu'] = {}
    nav_menu['nav_menu']['home'] = 'Home'
    nav_menu['nav_menu']['geoview'] = 'GIS'
    nav_menu['nav_menu']['send-dab'] = 'Send DAB+'
    nav_menu['nav_menu']['fake-acknowledgement'] = 'Mock ACK'
    nav_menu['nav_menu']['about'] = 'About Us'
    nav_menu['nav_menu']['contact'] = 'Contact'
    return nav_menu