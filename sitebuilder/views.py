__author__ = 'Victor'

import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from django.utils._os import safe_join

def get_page_or_404(name):
    """
    returns page content as a Django template
    """
    try:
        file_path = os.path.abspath(os.path.join(settings.SITE_PAGES_DIRECTORY, name))
        print(file_path)
    except ValueError:
        raise Http404('Page not found')
    else:
        if not os.path.exists(file_path):
            print(file_path)
            raise Http404('Page not found')

    with open(file_path, 'r') as f:
        page = Template(f.read())
    return page

def page (request, slug='index'):
    """
    render the requested page, if found
    :param request:
    :param slug:
    :return:
    """
    print (slug)
    file_name = "{}.html".format(slug)
    print("filename = " + os.path.abspath(settings.SITE_PAGES_DIRECTORY))
    page = get_page_or_404(file_name)
    # print("page = " + page)
    context = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', context)