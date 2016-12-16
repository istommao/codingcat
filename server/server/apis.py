# coding: utf-8
import os

from sanic.response import html, json

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
        return html(html_content)


class SiteListView(BaseView):

    def get(self, request):
        """Site list api."""
        site_list = [
            {'title': '知乎', 'url': 'https://www.zhihu.com/',
             'image': 'http://upload.chinaz.com/2013/1126/1385456238376.png'},
            {'title': 'v2ex', 'url': 'https://www.v2ex.com/',
             'image': 'http://ww3.sinaimg.cn/large/59767ad8tw1e5bs93qmiaj207r044742.jpg'},
            {'title': 'Quora', 'url': 'https://www.quora.com/',
             'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Quora_logo_2015.svg/1280px-Quora_logo_2015.svg.png'},
            {'title': 'medium', 'url': 'https://medium.com/',
             'image': 'https://cdn-images-1.medium.com/max/800/1*5ztbgEt4NqpVaxTc64C-XA.png'},
            {'title': '36kr', 'url': 'http://www.36kr.com/',
             'image': 'http://nzr2ybsda.qnssl.com/images/15452/FtW9MmdQBhP1o2lDRTGIMcwPYojR.png'},
            {'title': 'CSDN', 'url': 'http://www.csdn.net/',
             'image': 'http://www.csdn.net/css/logo.png'}
        ]
        dataset = {
            'results': site_list
        }

        return json(dataset)
