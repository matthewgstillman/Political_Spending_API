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
    print("Response: " + str(ca_legs_response))
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))
    legislators_array = []
    for key, value in ca_legs_response.iteritems():
        print("Key: " + str(key))
        legislators_array.append(key)
        print("Value: " + str(value))
        legislators_array.append(value)
        for i in range(0, len(legislators_array)):
            print("Length of Legislators Array: " + str(len(legislators_array)))
            legs = legislators_array[i]
            print("Legs: " + str(legs))
            i += 1
            print("i=" + str(i))
            # print("Key: " + str(key) + "Value: " + str(value))
        #Below Doesn't Work - Yet
        # for key, value in ca_legislator.iteritems():
        #     print(key, value)
        #     for key, value in value.iteritems():
        #         print("Key: " + str(key) + ", Value: " + str(value))
        #         for item in value.iteritems():
        #             print("Key: " + str(key) + ", Value: " + str(value))
        #             print("Item: " + str(item))
        #             legislators_array.append(item)
            context = {
                'attributes': attributes,
                'ca_legislator': ca_legislator,
                'ca_legs': ca_legs,
                'ca_legs_response': ca_legs_response,
                'legislators_array': legislators_array,
                'legs': legs,
                }
            return render(request, 'open_secrets_api/index.html', context)

def candidate_summary(request):
    url = ('http://www.opensecrets.org/api/?method=candSummary&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    candidate_summaries = response.json()
    print("Candidate Summaries: " + str(candidate_summaries))
    candidate_summary_response = candidate_summaries['response']
    candidate_summary = candidate_summary_response['summary']
    #.items() or .iteritems - with () - for iterating
    items_array = []
    for key, value in candidate_summary_response.iteritems():
        print(key, value)
        for key, value in value.iteritems():
            # print("Key: " + str(key) + ", Value: " + str(value))
            for item in value.iteritems():
                print("Key: " + str(key) + ", Value: " + str(value))
                print("Item: " + str(item))
                items_array.append(item)
            context = {
                'items_array': items_array,
                'candidate_summary': candidate_summary,
                'candidate_summary_response': candidate_summary_response,
            }
            return render(request, 'open_secrets_api/candidate_summary.html', context)