from sanic.response import html, json

from jinja2 import Environment, PackageLoader

from extensions.views import BaseView

env = Environment(loader=PackageLoader('extensions', 'templates'))


class HomePageView(BaseView):

    def get(self, request):
        template = env.get_template('index.html')

        dataset = {
            'name': 'hello world'
        }
        html_content = template.render(**dataset)
        return html(html_content)


class SiteList(BaseView):

    def get(self, request):
        site_list = [
            {'url': 'https://www.zhihu.com/'}
        ]
        dataset = {
            'results': site_list
        }

        return json(**dataset)
