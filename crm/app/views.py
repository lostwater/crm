"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def cases(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cases.html',
        {
            'title':'项目',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def clients(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cases.html',
        {
            'title':'项目',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def developers(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'开发者',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def developer(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'开发者',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def case(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'开发者',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def manager(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'开发者',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def client(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developers.html',
        {
            'title':'开发者',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

