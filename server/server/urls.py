from server import apis

API_LIST = [
    {'view': apis.HomePageView, 'url': r'/<url:.*>'},
    {'view': apis.SiteListView, 'url': r'/api/sites/'}
]
