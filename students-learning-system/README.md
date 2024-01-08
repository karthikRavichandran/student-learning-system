# Student Event Tracking System
Our project is called the Student Event Tracking System, which is targeted towards students. Our objective is to create a system for students who can view critical and non-critical alerts in the form of a one-liner and a short summary. The primary reason for developing this system is to bring events pertaining to each user in various categories into a single view. 

The project consists of an interactive UI developed using the streamlit library in python, a cloud-based database that stores user data and course information, and LLM-based information extraction from different sources, those being Moodle, Gradescope, and Piazza. For the purposes of demonstration, we are using synthetic data to emulate these platforms, obtaining permission to access this information is difficult.

## Setting up the application
1. To set up your environment in order to run the app, run `pip install -r requirements.txt`.
2. You will also need an OPENAI_API_KEY to run the LLM portion of the code. You can find information on that here: https://openai.com/blog/openai-api

## Running the application
In the terminal, with the installed environment open and starting in the base directory:
1. `cd src`
2. `streamlit run main.py`
```
