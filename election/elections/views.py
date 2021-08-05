import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate, Poll, Choice


def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/index.html', context)


def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(
            area=area, start_date__lte=today, end_date__gte=today)
        candidates = Candidate.objects.filter(area=area)
    except:
        poll = None
        candidates = None

    context = {'candidates': candidates, 'area': area, 'poll': poll}
    return render(request, 'elections/area.html', context)


def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    selection = request.POST['choice']

    try:
        choice = Choice.objects.get(poll_id=poll.id, candidate_id=selection)
        choice.votes += 1
        choice.save()

    except:
        choice = Choice(poll_id=poll_id, candidate_id=selection, votes=1)
        choice.save()

    return HttpResponseRedirect("/areas/{}/results", poll.area)


def results(request, area):

    candidates = Candidate.objects.filter(area=area)
    polls = Poll.objects.filter(area)
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        poll_results.append(result)

    context = {'candidates': candidates,
               'area': area, 'poll_results': poll_results}
    return render(request, 'templates/index.html', context)
