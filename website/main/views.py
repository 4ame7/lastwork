from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def buy(request):
    return render(request, 'main/buy.html')


def return_ticket(request):
    return render(request, 'main/return_ticket.html')


def contacts(request):
    return render(request, 'main/contacts.html')