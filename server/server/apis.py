# coding: utf-8
import os
import json
import ujson

import asyncio

import aiofiles

from sanic import response

from jinja2 import Environment, PackageLoader, Template

from redis import StrictRedis, ConnectionPool

from extensions.views import BaseView

env = Environment(loader=PackageLoader('extensions', 'templates'))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': '6379',
    'db': '4'
}
KVSTORE = StrictRedis(connection_pool=ConnectionPool(**REDIS_CONFIG))


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


def get_sites(path):
    value = KVSTORE.get(path)
    if value:
        dataset = ujson.loads(value.decode())
    else:
        site_list = []
        if os.path.exists(path):
            with open(path, 'r') as handler:
                site_list = ujson.load(handler)

        dataset = {
            'results': site_list
        }

        KVSTORE.set(path, ujson.dumps(dataset))

    return dataset


class SiteListView(BaseView):

    def get(self, request, name):
        """Site list api."""
        site_list = []
        path = '{}/sources/{}_sites.json'.format(BASE_DIR, name)

        dataset = get_sites(path)
        return response.json(dataset)


class SiteDetailView(BaseView):

    def get(self, request, endpoint):
        name, uid = endpoint.split('/')

        path = '{}/sources/{}_sites.json'.format(BASE_DIR, name)

        dataset = get_sites(path)

        data = {}
        for item in dataset['results']:
            if uid == item['uid']:
                data = item
                break

        return response.json(data)
