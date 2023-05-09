import requests


class CourseChecker():
    """
    Class which represents a course to be checked
    
    === Attributes ===
    _course_code: the course code of the course
    _course_title: the title of the course
    _course_session: the session of the course (Y/F/S)
    _activities: the activities to be tracked (LEC/TUT/PRA)
    user: the Discord UserID of the user who requested the course to be tracked
    
    === Representation Invariants ===
    - _course_code is a valid course code
    - _course_title is a valid course title, and is the corrspoding title to _course_code
    - _course_session is a valid course session, and is a session which _course_code is offered in
    _activity is a valid activity for the course
    - user is a valid Discord UserID
    """

    _course_code: str
    _course_title: str
    _course_session: str
    _activitiy: str
    
    def __init__(self, course_code: str, course_title: str, course_session: str, activity: str, user: int) -> None:
        self._course_code = course_code
        self._course_title = course_title
        self._course_session = course_session
        self._activity = activity
        self.user = user
        
        self.headers = {
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

        self.json_data = {
            'courseCodeAndTitleProps': {
                'courseCode': '',
                'courseTitle': '',
                'courseSectionCode': '',
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
        
        
    
    def scrape(self) -> bool:
        """
        Checks whether there is space free in the course for the activities specified
        """
        
        # Step One: Modify the headers to include the course code and session
        self.json_data['courseCodeAndTitleProps']['courseCode'] = self._course_code
        self.json_data['courseCodeAndTitleProps']['courseSectionCode'] = self._course_session
        self.json_data['courseCodeAndTitleProps']['courseTitle'] = self._course_title
        
        response = requests.post('https://api.easi.utoronto.ca/ttb/getPageableCourses', headers=self.headers, json=self.json_data)

        response = response.json()
        course = response['payload']['pageableCourse']['courses'][0]
        
        # course['sections'] is a list of all the activities for the course
        # We need to iterate through the list and find the activity we are looking for
        # We can use a list comprehension to do this
        
        # Step Two: Find the activity we are looking for
        activity = [section for section in course['sections'] if section['name'] == self._activity][0]
        
        # Step Three: Check if there is space in the activity
        # To do this, ew can return whether activity['maxEnrolment'] > activity['currentEnrolment']
        return activity['maxEnrolment'] > activity['currentEnrolment']