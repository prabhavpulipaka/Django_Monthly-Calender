from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthly_challenges = {
    'january': "Eat no meet on whole month",
    'february':"Walk 20 mins everyday",
    'march': "Walk 20 mins everyday",
    'april': "Walk 20 mins everyday",
    'may': "Eat no meet on whole month",
    'june': "Eat no meet on whole month",
    'july': "Walk 20 mins everyday",
    'august': "Eat no meet on whole month",
    'september': "Play football everyday",
    'october': "Eat no meet on whole month",
    'november': "Walk 20 mins everyday",
    'december': None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_number(request,month):
    months = list(monthly_challenges.keys())
    forward_months = months[month-1]
    redirect_url = reverse("month-challenge", args=[forward_months])
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request,month):
    try:
        challengetext = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challengetext, 
            "text_1": month.capitalize()
        })
    except:
        raise Http404()


    return HttpResponse(challengetext)