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
        for i in range(0, 56):
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

def candidate_contributions(request):
    donors_array = []
    attributes = '@attributes'
    url = ('https://www.opensecrets.org/api/?method=candContrib&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    candidate_contributions = response.json()
    # print("Candidate Contributions: " + str(candidate_contributions))
    candidate_response = candidate_contributions['response']
    # print("Candidate Response: " + str(candidate_response))
    contributors = candidate_response['contributors']
    print("Contributors: " + str(contributors))
    candidate_contributor = contributors['contributor']
    print("Candidate Contributor: " + str(candidate_contributor))
    for i in range(0,10):
        donors = candidate_contributor[i][attributes]
        print("Donor # " + str(i+1) + ": " + str(donors))
        donors_array.append(donors)
        i += 1
    org_name = candidate_contributor[0][attributes]['org_name']
    print("Organization Name: " + str(candidate_contributor[0][attributes]['org_name']))
    contributor_attributes = contributors[attributes]
    print("Contributor Attributes: " + str(contributor_attributes))
    for organization in candidate_contributor:
        print("Organization: " + str(organization))
        for key, value in contributors.iteritems():    
            print("Key: " + str(key) + ", Value: " + str(value))
            for key, value in value.iteritems():
                print("First Value: " + str(value))
                print("Key: " + str(key) + ", Value: " + str(value))
                for item in value:
                    print("ITEM: " + str(item))
                    context = {
                        'attributes': attributes,
                        'candidate_contributions': candidate_contributions,
                        'candidate_response': candidate_response,
                        'contributor_attributes': contributor_attributes,
                        'contributors': contributors,
                        'donors_array': donors_array,
                        'org_name': org_name,
                        }
                    return render(request, 'open_secrets_api/candidate_contributions.html', context)


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