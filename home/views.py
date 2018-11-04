# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings

def Index(request):
    return render(request, "home/index.html", {})
