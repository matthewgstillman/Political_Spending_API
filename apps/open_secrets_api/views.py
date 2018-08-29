from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = ('http://www.opensecrets.org/api/?method=getLegislators&id=CA&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    ca_legs = response.json()
    print("Response: " + str(response))
    print("California Politics: " + str(ca_legs))
    ca_legs_response = ca_legs['response']
    print("California-Legs Response: " + str(ca_legs_response))
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))
    # attributes = ca_legislator['@attributes']
    # print("California Legislator Attributes: " + str(attributes))
    context = {
        # 'attributes': attributes,
        'ca_legislator': ca_legislator,
        'ca_legs': ca_legs,
        'ca_legs_response': ca_legs_response,
    }
    return render(request, 'open_secrets_api/index.html', context)