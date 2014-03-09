from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse("Hello, world. You're at the poll index.")

# def index2(request):
#     return HttpResponse("Hello, second world. You're at the poll index.")

def vote(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def voted(request, poll_id):
    return HttpResponse("You have voted on poll %s." % poll_id)