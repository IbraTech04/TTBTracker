class CourseChecker():
    """
    Class which represents a course to be checked
    
    === Attributes ===
    _course_code: the course code of the course
    _course_title: the title of the course
    _course_session: the session of the course (Y/F/S)
    _activities: the activities to be tracked (LEC/TUT/PRA)
    
    === Representation Invariants ===
    - _course_code is a valid course code
    - _course_title is a valid course title, and is the corrspoding title to _course_code
    - _course_session is a valid course session, and is a session which _course_code is offered in
    _activities is a list of valid activities, and is the list of activities which _course_code is offered in
    """
    
    _course_code: str
    _course_title: str
    _course_session: str
    _activities: list[str]
    
    def __init__(self, course_code: str, course_title: str, course_session: str) -> None:
        self._course_code = course_code
        self._course_title = course_title
        self._course_session = course_session
        
        