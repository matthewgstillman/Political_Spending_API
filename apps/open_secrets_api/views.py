from django.shortcuts import render, redirect
import requests
import json
from objectpath import *

# Create your views here.
def index(request):
    attributes = '@attributes'
    url = ('http://www.opensecrets.org/api/?method=getLegislators&id=CA&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    ca_legs = response.json()
    ca_legs_response = ca_legs['response']
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))
    for keys in ca_legislator:
        print("Keys: " + str(keys) + ", Value: " + str(keys))
        context = {
            'attributes': attributes,
            'ca_legislator': ca_legislator,
            'ca_legs': ca_legs,
            'ca_legs_response': ca_legs_response,
        }
        return render(request, 'open_secrets_api/index.html', context)

def candidate_summary(request):
    url = ('http://www.opensecrets.org/api/?method=candSummary&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    candidate_summaries = response.json()
    # print("Candidate Summaries: " + str(candidate_summaries))
    candidate_summary_response = candidate_summaries['response']
    # print("Candidate Summary Responses: " + str(candidate_summary_response))
    candidate_summary = candidate_summary_response['summary']
    # print("Summary: " + str(candidate_summary))
    # attributes = candidate_summary[0]
    # print("Attributes: " + str(attributes))
    #.items() - with () - works for iterating
    for key, value in candidate_summary_response.iteritems():
        print(key, value)
        for key, value in value.iteritems():
            print("Key: " + str(key) + ", Value: " + str(value))
        context = {
            'candidate_summary': candidate_summary,
            'candidate_summary_response': candidate_summary_response,
        }
        return render(request, 'open_secrets_api/candidate_summary.html', context)