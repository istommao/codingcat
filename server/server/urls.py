from server import apis

API_LIST = [
    {'view': apis.SiteListView, 'url': r'/api/sites/<name:.*>/'},
    {'view': apis.HomePageView, 'url': r'/<url:.*>'}
]
