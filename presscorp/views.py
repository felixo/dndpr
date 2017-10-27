#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Slider #Partner, Wwd, Video, How_to_help, Media, Media_images, About, We_cares, MainPage
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def index(request):
    slider = Slider.objects.all()
    return render(request, 'presscorp/index.html', {'slider': slider})