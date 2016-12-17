# coding: utf-8
import os
import json

from sanic import response as response

from jinja2 import Environment, PackageLoader, Template

from extensions.views import BaseView

env = Environment(loader=PackageLoader('extensions', 'templates'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def generate_homepage_template():
    path = '{}/web/index.html'.format(
        os.path.dirname(BASE_DIR)
    )
    with open(path, 'r') as file:
        template = Template(file.read())

    return template


class HomePageView(BaseView):

    def get(self, request, url):
        template = generate_homepage_template()

        html_content = template.render()
        return response.html(html_content)


class SiteListView(BaseView):

    def get(self, request, name):
        """Site list api."""
        site_list = []
        path = '{}/sources/{}_sites.json'.format(BASE_DIR, name)
        if os.path.exists(path):
            with open(path, 'r') as handler:
                site_list = json.load(handler)

        dataset = {
            'results': site_list
        }

        return response.json(dataset)
