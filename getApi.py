from flask import Response
from flask import Flask, jsonify, request,redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
from geopy.geocoders import Nominatim
import time
import requests
import json
from pprint import pprint
import json
app=Flask(__name__)
CORS(app)
api=Api(app)
aps = Nominatim(user_agent="tutorial")

# def get_address_by_location(latitude, longitude, language="en"):
#     """This function returns an address as raw from a location
#     will repeat until success"""
#     # build coordinates string to pass to reverse() function
#     coordinates = f"{latitude}, {longitude}"
#     # sleep for a second to respect Usage Policy
    
#     location = app.reverse(coordinates, language=language).raw
#     # print(location)
#     getRecommended(location['address']['county'])
#     pass

class getDataRecommended(Resource):
    def get(self,pk=None,latitude='',longitude='',language="en"):
        """This function returns an address as raw from a location
        will repeat until success"""
        # build coordinates string to pass to reverse() function
        print(latitude)
        coordinates = f"{latitude}, {longitude}"
        # sleep for a second to respect Usage Policy
        
        location = aps.reverse(coordinates, language=language).raw
        # print(location)
        # getRecommended(location['address']['county'])
        print(location)
        if(location['address'].get('county')==None):
            data = getRecommended(location['address']['city'])
        else:
            data = getRecommended(location['address']['county'])
        return data

def getRecommended(cityName):
    print(cityName)
    response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key=&cityName={cityName}&page=1&compId=')
    listItem = []
    x = json.loads(response.text)
    listData = x['jobs']['rows'][0]
    for i in listData:
        listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName']})
    
    response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries=&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
    x = json.loads(response.text)
    listData = x['data']['jobs']
    for i in listData:
        listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name']})
    
    url = "https://www.philjobnet.gov.ph/jobs/vacant/"
    payload=f'JobLocation=${cityName}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x = json.loads(response.text)
    if(x.get('Job Search')==None):
        pass
    else:
        listData = x['data']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name']})
    return listItem


def getRecommended1(cityName):
    response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries=&degrees=&is_company_verified=0&job_categories=&job_locations=Makati&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
    x = json.loads(response.text)
    print(x)
    return x


# def searchJob(cityName=''):
#     print(cityName)
#     response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key=&cityName={cityName}&page=1&compId=')
#     x = json.loads(response.text)
#     print(x)
#     return x

class getSearchedJob(Resource):
    def get(self,pk=None,cityName='',searchvalue=''):
        print("searchedJob")
        response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key={searchvalue}&cityName={cityName}&page=1&compId=')
        listItem = []
        x = json.loads(response.text)
        listData = x['jobs']['rows'][0]
        for i in listData:
            listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName']})
        
        response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries=&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
        x = json.loads(response.text)
        listData = x['data']['jobs']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name']})
        
        url = "https://www.philjobnet.gov.ph/jobs/vacant/"
        payload=f'JobLocation=${cityName}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        x = json.loads(response.text)
        if(x.get('Job Search')==None):
            pass
        else:
            listData = x['data']
            for i in listData:
                listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name']})
        return listItem


class getSearchedJobTittle(Resource):
    def get(self,pk=None,cityName='',searchvalue=''):
        print("searchedJob")
        response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key=&cityName={cityName}&page=1&compId=')
        listItem = []
        x = json.loads(response.text)
        listData = x['jobs']['rows'][0]
        for i in listData:
            listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName']})
        
        response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries=&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
        x = json.loads(response.text)
        listData = x['data']['jobs']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name']})
        
        url = "https://www.philjobnet.gov.ph/jobs/vacant/"
        payload=f'JobLocation=${cityName}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        x = json.loads(response.text)
        if(x.get('Job Search')==None):
            pass
        else:
            listData = x['data']
            for i in listData:
                listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name']})
        return listItem
        

api.add_resource(getDataRecommended,'/api/v1/getdata/<string:latitude>/<string:longitude>')
api.add_resource(getSearchedJob,'/api/v1/search/<string:cityName>/<string:searchvalue>')
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)