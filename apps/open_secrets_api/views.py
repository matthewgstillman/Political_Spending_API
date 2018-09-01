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
    # print("Response: " + str(ca_legs_response))
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))

    legislators_array = []
    
    for i in range(0, 56):
        legislator = ca_legislator[i][attributes]
        print("Legislator: " + str(legislator))
        legislators_array.append(legislator)
        # legs = legislators_array[i]
        # print("Legs: " + str(legs))
        print("i = " + str(i))
        i += 1
        print("NOW i = " + str(i))

    context = {
        'attributes': attributes,
        'ca_legislator': ca_legislator,
        'ca_legs': ca_legs,
        'ca_legs_response': ca_legs_response,
        'legislators_array': legislators_array,
        # 'legs': legs,
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

def candidate_industry(request):
    industry_type_array = []
    attributes = '@attributes'
    url = ('https://www.opensecrets.org/api/?method=candIndustry&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    # url = ('http://www.opensecrets.org/api/?method=candSummary&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    candidate_industry = response.json()
    print("Candidate Donations By Industry: " + str(candidate_industry))
    industries = candidate_industry['response']['industries']['industry']
    print("Industries: " + str(industries))
    candidate_attributes = candidate_industry['response']['industries'][attributes]
    print("Candidate Attributes: " + str(candidate_attributes))
    candidate_name = candidate_industry['response']['industries'][attributes]['cand_name']
    print("Candidate Name: " + str(candidate_name))
    for i in range(0, 10):
        industry_type = industries[i][attributes]
        print("Industry Type: " + str(industry_type))
        industry_type_array.append(industry_type)
        i += 1
    context = {
        'candidate_attributes': candidate_attributes,
        'candidate_name': candidate_name,
        'candidate_industry': candidate_industry,
        'industries': industries,
        'industry_type_array': industry_type_array,
    }
    return render(request, 'open_secrets_api/candidate_industry.html', context)

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


def expenditures(request):
    expenditure_item_array = []
    attributes = '@attributes'
    url = ('http://www.opensecrets.org/api/?method=independentExpend&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    expenditures = response.json()
    print("Expenditures: " + str(expenditures))
    expenditure_response = expenditures['response']
    expenditure_index = expenditure_response['indexp']
    for i in range(0,50):
        expenditure_item = expenditure_index[i][attributes]
        print("Expenditure Item: " + str(expenditure_item))
        expenditure_item_array.append(expenditure_item)
        i += 1
    context = {
        'expenditures': expenditures,
        'expenditure_index': expenditure_index,
        'expenditure_item_array': expenditure_item_array,
        'expenditure_response': expenditure_response,
    }
    return render(request, 'open_secrets_api/expenditures.html', context)