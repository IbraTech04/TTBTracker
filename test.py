import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Origin': 'https://ttb.utoronto.ca',
    'Prefer': 'safe',
    'Referer': 'https://ttb.utoronto.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'courseCodeAndTitleProps': {
        'courseCode': 'CCT109H5',
        'courseTitle': '',
        'courseSectionCode': 'F',
        'searchCourseDescription': False,
    },
    'departmentProps': [],
    'campuses': [],
    'sessions': [
        '20235F',
        '20235S',
        '20235',
    ],
    'requirementProps': [],
    'instructor': '',
    'courseLevels': [],
    'deliveryModes': [],
    'dayPreferences': [],
    'timePreferences': [],
    'divisions': [
        'ERIN',
    ],
    'creditWeights': [],
    'page': 1,
    'pageSize': 20,
    'direction': 'asc',
}

response = requests.post('https://api.easi.utoronto.ca/ttb/getPageableCourses', headers=headers, json=json_data)

# Save the response as a JSON object
json_response = response.json()
import json
# Save this to a file called example_json.json
with open('example_json.json', 'w') as f:
    json.dump(json_response, f)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"courseCodeAndTitleProps":{"courseCode":"CCT109H5","courseTitle":"Contemporary Communication Technologies","courseSectionCode":"F","searchCourseDescription":false},"departmentProps":[],"campuses":[],"sessions":["20235F","20235S","20235"],"requirementProps":[],"instructor":"","courseLevels":[],"deliveryModes":[],"dayPreferences":[],"timePreferences":[],"divisions":["ERIN"],"creditWeights":[],"page":1,"pageSize":20,"direction":"asc"}'
#response = requests.post('https://api.easi.utoronto.ca/ttb/getPageableCourses', headers=headers, data=data)