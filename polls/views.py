from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll

from django.views import generic 



# First option to render a page, Second option: render()
# from django.http import Http404
from django.http import HttpResponse
# from django.template import RequestContext, loader

    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {'poll_list':latest_poll_list})
    # return HttpResponse(template.render(context))
from polls.models import Poll, Author, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "poll_list"

    def get_queryset(self):
        return Poll.objects.order_by('pub_date')[:4]


# def index2(request):
#     return HttpResponse("Hello, second world. You're at the poll index.")

class VoteView(generic.DetailView):
    # long version of get_object_or_404
    # try:
    #     currentPoll = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #     raise Http404

    # get_object_or_404
    # currentPoll = get_object_or_404(Poll, pk=poll_id)
    # return render(request, "polls/vote.html", {"poll": currentPoll})

    # use django.views.generic.DetailView
    model = Poll
    template_name = "polls/vote.html"

class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"


def voted(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/vote.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', kwargs={"pk":p.id}))

