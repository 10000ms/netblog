# -*- coding: utf-8 -*-
from neko_server.views.common import render_template


def index(request):
    return render_template('index.html')


publish_handler = {
    '/': index,
}
