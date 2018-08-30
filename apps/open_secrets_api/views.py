from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    attributes = "@attributes"
    url = ('http://www.opensecrets.org/api/?method=getLegislators&id=CA&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    ca_legs = response.json()
    ca_legs_response = ca_legs['response']
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))
    # print("Legislators: " + str(leg_atts))
    for legislators in ca_legislator:
        print("Legislators: " + str(legislators))
    context = {
        'attributes': attributes,
        'ca_legislator': ca_legislator,
        'ca_legs': ca_legs,
        'ca_legs_response': ca_legs_response,
        'legislators': legislators,
    }
    return render(request, 'open_secrets_api/index.html', context)