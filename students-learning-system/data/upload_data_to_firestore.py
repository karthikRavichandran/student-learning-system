import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Replace these paths with your service account and CSV file paths
cred_path = 'serviceAccount.json'
csv_path = './students.csv'

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Read CSV into DataFrame
df = pd.read_csv(csv_path)


#------------ remove later -------------

json_file_path = './gradescope/math314.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)
# data = json.loads('./gradescope/math314.json')

event = []
title = []
description = []
due_date = []
for i in data['Assignments']:
    event.append(i)
    title.append(data['Assignments'][i]['Title'])
    description.append(data['Assignments'][i]['Description'])
    due_date.append(data['Assignments'][i]['Due Date'])
df = pd.DataFrame({"Event": event, "Title":title, 
             "Description": description, "Due_date": due_date})

#---------------------------------------

# Convert DataFrame to dictionary
data_dict = df.to_dict(orient='records')

# Upload data to Firestorex
for record in data_dict:
    db.collection('test').add(record)

