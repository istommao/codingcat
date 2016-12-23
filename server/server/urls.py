from server import apis

API_LIST = [
    {'view': apis.SiteListView, 'url': r'/api/sites/<name:.*>/$'},
    {'view': apis.SiteDetailView, 'url': r'/api/detail/<endpoint:.*>/'},
    {'view': apis.HomePageView, 'url': r'/<url:.*>'}
]
