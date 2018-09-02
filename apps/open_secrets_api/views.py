from django.shortcuts import render, redirect
import requests
import json
from objectpath import *
from state_dict import state_dict

# Create your views here.
def index(request):
    session_state_abr = request.session['state_abr']
    session_state_name = request.session['state_name']
    print("Session State Abbreviation: " + str(session_state_abr))
    attributes = '@attributes'
    url_root = 'http://www.opensecrets.org/api/?method=getLegislators&id='
    url_tail = '&output=json&apikey=11c4c60af966085902db37697f3c52e3'
    url = str(url_root) + str(session_state_abr) + str(url_tail)
    print("URL: " + str(url))
    response = requests.get(url)
    ca_legs = response.json()
    ca_legs_response = ca_legs['response']
    # print("Response: " + str(ca_legs_response))
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))
    # legislator_count = ca_legislator.count()
    # print("Legislator Count: " + str(legislator_count))

    legislators_array = []
    
    for i in range(0, len(ca_legislator)):
        legislator = ca_legislator[i][attributes]
        print("Legislator: " + str(legislator))
        legislators_array.append(legislator)
        i += 1
    
    # print("Dictionary Item: " + str(state_dict['UT']))
    context = {
        'attributes': attributes,
        'ca_legislator': ca_legislator,
        'ca_legs': ca_legs,
        'ca_legs_response': ca_legs_response,
        'legislators_array': legislators_array,
        'session_state_abr': session_state_abr,
        'session_state_name': session_state_name,
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
    for i in range(0,len(candidate_contributor)):
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
    attributes = '@attributes'
    url = ('http://www.opensecrets.org/api/?method=candSummary&cid=N00007360&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
    response = requests.get(url)
    candidate_summaries = response.json()
    print("Candidate Summaries: " + str(candidate_summaries))
    candidate_summary_response = candidate_summaries['response']
    candidate_summary = candidate_summary_response['summary']
    #.items() or .iteritems - with () - for iterating
    candidate_summary_attributes = candidate_summary[attributes]
    print("Candidate Summary Attributes: " + str(candidate_summary_attributes))
    origin = candidate_summary_attributes['origin']
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
                'attributes': attributes,
                'items_array': items_array,
                'candidate_summary': candidate_summary,
                'candidate_summary_attributes': candidate_summary_attributes,
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

def other_states(request):
    if request.method == 'POST':
        state_abr = request.POST['state']
        print("State Abbreviation: " + str(state_abr))
        request.session['state_abr'] = state_abr
        session_state_abr = request.session['state_abr']
        state_name = state_dict[session_state_abr]
        request.session['state_name'] = state_name
        print("State Name: " + str(state_name))
        session_state_name = request.session['state_name'] 
        print("Session State Name: " + str(session_state_name))
        context = {
            'session_state_abr': session_state_abr,
            'session_state_name': session_state_name
        }
        return redirect('/', context)
    if request.method == 'GET':
        return render(request, 'open_secrets_api/other_states.html')