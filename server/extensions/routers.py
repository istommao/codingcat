

def create_routers(app, api_list):
    for api in api_list:
        app.add_route(api['view'](), api['url'])
