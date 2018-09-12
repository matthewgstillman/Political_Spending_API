from django.shortcuts import render, redirect
import requests
import json
import wikipedia
from objectpath import *
from state_dict import state_dict
from cid_list import cid_list, name_list
from candidate_dict import candidate_dict
from api_key import api_key

# Create your views here.
def index(request):
    session_state_abr = request.session['state_abr']
    session_state_name = request.session['state_name']
    for key, value in candidate_dict[session_state_name].iteritems():
        print("Key: " + str(key) + ", Value: " + str(value))
    state_legislators = candidate_dict[session_state_name]
    print("State Legislators: " + str(state_legislators))
    # if session_state_name in candidate_dict:
    #     print("Session State Name: " + str(candidate_dict[session_state_name]))
    # else:
    #     pass
    print("Session State Abbreviation: " + str(session_state_abr))
    attributes = '@attributes'
    url_root = 'http://www.opensecrets.org/api/?method=getLegislators&id='
    url_middle = '&output=json&apikey='
    url_tail = api_key['api_key']
    url = str(url_root) + str(session_state_abr) + str(url_middle) + str(url_tail)
    print("URL: " + str(url))
    response = requests.get(url)
    ca_legs = response.json()
    ca_legs_response = ca_legs['response']
    # print("Response: " + str(ca_legs_response))
    ca_legislator = ca_legs_response['legislator']
    print("California Legislators: " + str(ca_legislator))

    legislators_array = []
    legislators_id_array = []
    
    for i in range(0, len(ca_legislator)):
        legislator = ca_legislator[i][attributes]
        name = ca_legislator[i][attributes]['firstlast']
        candidate_id = ca_legislator[i][attributes]['cid']
        print("Candidate ID: " + str(candidate_id))
        print("Name: " + str(name))
        print("Legislator: " + str(legislator))
        legislators_array.append(legislator)
        legislators_id_array.append(name)
        legislators_id_array.append(candidate_id)
        i += 1
    context = {
        'attributes': attributes,
        'ca_legislator': ca_legislator,
        'ca_legs': ca_legs,
        'ca_legs_response': ca_legs_response,
        'legislators_array': legislators_array,
        'legislators_id_array': legislators_id_array,
        'session_state_abr': session_state_abr,
        'session_state_name': session_state_name,
        'state_legislators': state_legislators,
        }
    return render(request, 'open_secrets_api/index.html', context)

def candidate_contributions(request):
    donors_array = []
    attributes = '@attributes'
    url_root = 'https://www.opensecrets.org/api/?method=candContrib&cid=N00007364&cycle=2018&output=json&apikey='
    url_tail = api_key['api_key']
    # url_tail = '11c4c60af966085902db37697f3c52e3'
    url = str(url_root) + str(url_tail)
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
    url_root = 'https://www.opensecrets.org/api/?method=candIndustry&cid=N00007364&cycle=2018&output=json&apikey='
    url_tail = api_key['api_key']
    url = str(url_root) + str(url_tail)
    url = ('https://www.opensecrets.org/api/?method=candIndustry&cid=N00007364&cycle=2018&output=json&apikey=11c4c60af966085902db37697f3c52e3')
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

def candidate_sectors(request):
    sector_array = []
    attributes = '@attributes'
    url_root = 'http://www.opensecrets.org/api/?method=candSector&cid=N00007364&cycle=2018&output=json&apikey='
    url_tail = api_key['api_key']
    url = str(url_root) + str(url_tail)
    response = requests.get(url)
    # sectors = response['sectors']
    # print("Sectors " + str(sectors))
    campaign_sectors = response.json()
    print("Candidate Sectors: " + str(campaign_sectors))
    sector_attributes = campaign_sectors['response']['sectors'][attributes]
    print("Sector Attributes: " + str(sector_attributes))
    for i in range(0, 13):
        sector = campaign_sectors['response']['sectors']['sector'][i][attributes]
        print("Sector: " + str(sector))
        sector_array.append(sector)
        i += 1
    # sector = sector_attributes
    context = {
        'sector': sector,
        'sector_array': sector_array,
        'sector_attributes': sector_attributes,
        'campaign_sectors': campaign_sectors,
    }
    return render(request, 'open_secrets_api/candidate_sectors.html', context)

def candidate_summary(request):
    attributes = '@attributes'
    url_root = 'http://www.opensecrets.org/api/?method=candSummary&cid=N00007364&cycle=2018&output=json&apikey='
    url_tail = api_key['api_key']
    url = str(url_root) + str(url_tail)
    response = requests.get(url)
    candidate_summaries = response.json()
    print("Candidate Summaries: " + str(candidate_summaries))
    candidate_summary_response = candidate_summaries['response']
    candidate_summary = candidate_summary_response['summary']
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
    url_root = 'http://www.opensecrets.org/api/?method=independentExpend&output=json&apikey='
    url_tail = api_key['api_key']
    url = str(url_root) + str(url_tail)
    response = requests.get(url)
    expenditures = response.json()
    expenditure_response = expenditures['response']
    expenditure_index = expenditure_response['indexp']
    for i in range(0,50):
        expenditure_item = expenditure_index[i][attributes]
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


def select_candidate(request):
    candidate_list = []
    names_length = len(name_list)
    cid_length = len(cid_list)
    print("Length of Names = " + str(names_length))
    print("Length of CIDs = " + str(cid_length))
    # print(name_list)
    # print(cid_list)
    # for i in name_list:
    #     for j in cid_list:
            
    context = {
        'candidate_list': candidate_list,
        # 'candidate_dict': candidate_dict,
    }
    return render(request, 'open_secrets_api/select_candidate.html', context)