from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

# First option to render a page, Second option: render()
from django.http import HttpResponse
# from django.template import RequestContext, loader

    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'poll_list':latest_poll_list})
    # return HttpResponse(template.render(context))
from polls.models import Poll, Author, Choice

def index(request):
    latest_poll_list = Poll.objects.order_by('pub_date')[:4]
    # output = ', '.join([p.question for p in latest_poll_list])
    context = {'poll_list':latest_poll_list}

    return render(request, 'polls/index.html', context)


# def index2(request):
#     return HttpResponse("Hello, second world. You're at the poll index.")

def vote(request, poll_id):
    # long version of get_object_or_404
    # try:
    #     currentPoll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404

    currentPoll = get_object_or_404(Poll, pk=poll_id)
    return render(request, "polls/vote.html", {"poll": currentPoll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def voted(request, poll_id):
    return HttpResponse("You have voted on poll %s." % poll_id)