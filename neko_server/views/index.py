# -*- coding: utf-8 -*-
from views.common import render_template


def index(request):
    return render_template('index.html')


index_handler = {
    '/': index,
}
