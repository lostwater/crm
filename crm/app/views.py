"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import *

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
        'app/clients.html',
        {
            'title':'客户',
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

def case_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CaseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CaseForm()
    return render(request, 'app/case_create.html', {'form': form})

def client_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientForm()
    return render(request, 'app/client_create.html', {'form': form})