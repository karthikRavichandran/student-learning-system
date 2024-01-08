import json
import pandas as pd

class Dataloader:
    """
    The Dataloader object reads the local directory for student 
    information and processes it into pandas dataframes.

    ...

    Attributes
    ----------
    student_id : int
        The student id for which data which is currently being accessed and served

    Methods
    -------
    get_all_student_info()
        Loads in all the relevant student information for accessing.
    get_student_info()
        Gets student information for the current student.
    get_course_enrollment(json_file_path)
        Gets the enrolled students for the class described using the json file path.
    get_moodle_data(json_file_path)
        Gets all the moodle data for the class described using the json file path.
    get_gradescope_data(json_file_path)
        Gets all the gradescope data for the class described using the json file path.
    get_piazza_df(json_file_path)
        Gets all the piazza data for the class described using the json file path.
    get_dashboard_data(json_file_path)
        Gets all the dashboard data described using the json file path.
    """

    def __init__(self, student_id):
        """
        Parameters
        ----------
        student_id : int
            The student id for which data which is currently being accessed and served
        """
        self.student_id = student_id

    def get_all_student_info():
        """
        Loads in all the relevant student information for accessing.

        Returns
        -------
        pandas.Dataframe
            The processed student information as a dataframe
        """
        return pd.read_csv("../data/students.csv")
    
    def get_student_info(self):
        """
        Loads in all the relevant student information for accessing.

        Returns
        -------
        pandas.Dataframe
            The processed student information as a dataframe
        """
        out = pd.read_csv("../data/students.csv")
        return out[out["student id"] == self.student_id]
    
    def get_course_enrollment(json_file_path):
        """
        Gets the enrolled students for the class described using the json file path.

        Parameters
        ----------
        json_file_path : str
            The json file path which we will read and process.

        Returns
        -------
        pandas.Dataframe
            The processed course enrollment information as a dataframe
        """
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data["Enrolled Students"]

    def get_moodle_data(self, json_file_path):
        """
        Gets all the moodle data for the class described using the json file path.

        Parameters
        ----------
        json_file_path : str
            The json file path which we will read and process.
        
        Returns
        -------
        dict
            The processed moodle information to feed into the LLM
        pandas.Dataframe
            The processed moodle information as a dataframe
        pandas.Dataframe
            The processed summary of grade information as a dataframe
        pandas.Dataframe
            The processed raw grade information as a dataframe
        """
        keys_to_keep = ['Course Title', 'Course Syllabus', 'Grade Breakdown']

        with open(json_file_path, 'r') as file:
            data = json.load(file)

            # Filtered dictionary using a dictionary comprehension
        data_for_llm = {key: data[key] for key in keys_to_keep if key in data}

        if 'Assignments' in data:
            moodle_df = pd.DataFrame(data['Assignments']).T
        else:
            moodle_df = None
        if 'Grades' in data:
            summary_of_moodle_grade = pd.DataFrame(data['Grades']).describe().drop(index='count')
            score = pd.DataFrame(data['Grades']).T.filter([f'{self.student_id}'], axis=1) * 100
        else:
            summary_of_moodle_grade = None
            score = None

        return data_for_llm, moodle_df, summary_of_moodle_grade, score

    def get_gradescope_data(self, json_file_path):
        """
        Gets all the gradescope data for the class described using the json file path.
    
        Parameters
        ----------
        json_file_path : str
            The json file path which we will read and process.

        Returns
        -------
        pandas.Dataframe
            The processed homework information as a dataframe
        pandas.Dataframe
            The processed grade statistics information as a dataframe
        pandas.Dataframe
            The processed raw grade information as a dataframe
        """
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        # data = json.loads('./gradescope/math314.json')

        hws = pd.DataFrame(data['Assignments']).T

        stats = pd.DataFrame(data['Grades']).describe().drop(index='count')
        score = pd.DataFrame(data['Grades']).T.filter([f'{self.student_id}'], axis=1) * 100
        return hws, stats, score

    def get_piazza_df(self, json_file_path):
        """
        Gets all the piazza data for the class described using the json file path.

        Parameters
        ----------
        json_file_path : str
            The json file path which we will read and process.

        Returns
        -------
        pandas.Dataframe
            The processed piazza information as a dataframe
        """
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        title = []
        topic = []
        poster = []
        poster_date = []
        body = []
        body = []
        follow_up_1 = []
        follow_up_2 = []
        follow_up_3 = []
        follow_up_4 = []
        if isinstance(data, list):
            json_data = data[0]['Posts']
        else:
            json_data = data['Posts']
        for i in json_data:  # or data['Posts'] - for
            title.append(i['Title'])
            topic.append(i['Topic'])
            poster.append(i['Poster'])
            poster_date.append(i['Post Date'])
            body.append(i['Body'])
            follow_up_1.append(i['Followups'][0]['Body'])
            try:
                follow_up_2.append(i['Followups'][1]['Body'])
            except:
                follow_up_2.append(None)
            try:
                follow_up_3.append(i['Followups'][2]['Body'])
            except:
                follow_up_3.append(None)
            try:
                follow_up_4.append(i['Followups'][3]['Body'])
            except:
                follow_up_4.append(None)

        df = pd.DataFrame({
            'title': title,
            'topic': topic,
            'poster': poster,
            'poster_date': poster_date,
            'body': body,
            'follow_up_1': follow_up_1,
            'follow_up_2': follow_up_2,
            'follow_up_3': follow_up_3,
            'follow_up_4': follow_up_4
        })

        return df

    def get_dashboard_data(self, json_file_path):
        """
        Gets all the dashboard data described using the json file path.

        Parameters
        ----------
        json_file_path : str
            The json file path which we will read and process.
        
        Returns
        -------
        dict
            The processed dashboard information as a dictionary
        """
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        return data
