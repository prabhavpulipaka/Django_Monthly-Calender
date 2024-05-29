from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    'december': "Eat no meet on whole month"
}

def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
    for month in months:
        cap_month = month.capitalize()
        redirect_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{redirect_path}\">{cap_month}</a></li>"
    return_list = f"<ul>{list_items}</ul>"
    return HttpResponse(return_list)

def monthly_number(request,month):
    months = list(monthly_challenges.keys())
    forward_months = months[month-1]
    redirect_url = reverse("month-challenge", args=[forward_months])
    return HttpResponseRedirect(redirect_url)

def monthly_challenge(request,month):
    try:
        challengetext = monthly_challenges[month]
        response_data = f"<h1>{challengetext}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month doesn't Exist !!!")


    return HttpResponse(challengetext)