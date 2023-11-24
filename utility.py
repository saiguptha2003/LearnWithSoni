from firebase_admin import credentials, initialize_app, db, firestore, auth, storage,credentials
import firebase_admin
from flask_mail import Mail, Message
import pyrebase
import hashlib
import json
import pandas as pd
import numpy as np
import random
def randomnumber(j):
    return random.randint(0,j)
    
# from .dotenv import load_dotenv
# import os
# def configure():
#     load_dotenv()
#     #os.getenv('required env variable')
    
cred = credentials.Certificate('soni-94809-firebase-adminsdk-igagy-fe6fda0c2b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
with open('configure.json', 'r') as json_file:
    config = json.load(json_file)
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def checkuser(email,password):
    try:
        user=auth.sign_in_with_email_and_password(email,password)
        accountstatus=auth.get_account_info(user['idToken'])['users'][0]['emailVerified']
        if accountstatus==True:
            return user['localId']
        
        elif accountstatus==False:
            return 1
        else:
            return -1
    except:
        return None
    
def createuser(email,password,first):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        x=auth.send_email_verification(user['idToken'])
    
        if x :
            ref=db.collection('userData').document('{}'.format(user['localId']))
            ref.set({
                'uuid':user['localId'],
                'email':email,
                'first-name':first,
                })
        if(user):
            return user['localId']
        else:
            return False
    except:
        return False
    
def getparagraphId():
    try:
        dataframe=pd.read_csv(r'static\resources\paragraph.csv',encoding= 'unicode_escape')
        paralist=dataframe['paragraph_id'].tolist()
        s=paralist[randomnumber(randomnumber(len(paralist)))]
        
        return s
    except:
        return None
# def getQuestions(paragraphId):
#     try:
#         print(paragraphId)
#         dataframe=pd.read_csv(r'static\resources\questions.csv')
#         dataframe=dataframe[dataframe['paragraph_id']==paragraphId]
#         return dataframe.values.tolist()
#     except:
#         print("not found")
        
        
def getQuestions(paragraphId):
    try:
        #print(paragraphId)
        dataframe=pd.read_csv(r'static\resources\questions.csv')
        dataframe=dataframe[dataframe['paragraph_id']==paragraphId]
        return dataframe.to_dict('records')
    except:
        return None

def getParagraphDetails(id):
    try:
        
        dataframe=pd.read_csv(r'static\resources\paragraph.csv',encoding= 'unicode_escape')
        
        dataframe=dataframe[dataframe['paragraph_id']==id.strip()]
        return dataframe.to_dict('records')
    except:
        return None
        

def get_audio_links():
    datframe=pd.read_csv(r'static\resources\audioparagraph.csv',encoding= 'unicode_escape')
    
    
    return datframe.to_dict('records')
    # try:
    #     dataframe=pd.read_csv(r'static\resources\audioparagraph.csv',encoding= 'unicode_escape')
    #     print(dataframe)
    #     return dataframe.to_dict('records')
    # except:
    #     print("not found")
get_audio_links()


def getAudioparagraphId():
    try:
        dataframe=pd.read_csv(r'static\resources\audioparagraph.csv',encoding= 'unicode_escape')
        paralist=dataframe['paragraph_id'].tolist()
        s=paralist[randomnumber(randomnumber(len(paralist)))]
        return s
    except:
        return None
print("d",getAudioparagraphId())

def getAudioQuestions(paragraphId):
    try:
        #print(paragraphId)
        dataframe=pd.read_csv(r'static\resources\Audioquestions.csv')
        dataframe=dataframe[dataframe['paragraph_id']==paragraphId]
        return dataframe.to_dict('records')
    except:
        return None


def getAudioParagraphDetails(id):
    try:
        dataframe=pd.read_csv(r'static\resources\audioparagraph.csv',encoding= 'unicode_escape')
        dataframe=dataframe[dataframe['paragraph_id']==id.strip()]
        return dataframe.to_dict('records')
    except:
        return None      
        
def getfirstname(uuid):
    try:
        ref=db.collection('userData').document('{}'.format(uuid))
        data=ref.get()
        
        return data.to_dict()['first-name']
    except:
        return None

def addReadingPassageScoretoDb(uuid,score,paragraph_id,feedback):
    try:
        ref=db.collection('userData').document('{}'.format(uuid))
        ref.update({
            'ReadingPassage':firestore.ArrayUnion([{
                'paragraph_id':paragraph_id,
                'feedback':feedback,
                'score':score
                }])
            })
    except:
        return None
def getReadingPassageScoretoDb(uuid):
    try:
        ref=db.collection('userData').document('{}'.format(uuid))
        data=ref.get()
        
        return data.to_dict()['ReadingPassage']
    except:
        return None
def addAudioPassageScoretoDb(uuid,score,paragraph_id,feedback):
    try:
        ref=db.collection('userData').document('{}'.format(uuid))
        ref.update({
            'AudioPassage':firestore.ArrayUnion([{
                'paragraph_id':paragraph_id,
                'feedback':feedback,
                'score':score
                }])
            })
    except:
        return None

def getAudioPassageScoretoDb(uuid):
    try:
        ref=db.collection('userData').document('{}'.format(uuid))
        data=ref.get()
       
        return data.to_dict()['AudioPassage']
    except:
        return None
    
def gettotalusers():
    try:
        ref=db.collection('userData')
        data=ref.get()
       
        return len(data)
    except:
        return None

def  getuserdetails():
    lis=[]
    try:
        docs=db.collection('userData').stream()
        for doc in docs:
            lis.append(doc.to_dict())
        
        return lis
    except:
        return None

def getReadingComments():
    try:
        lis=[]
        ref=db.collection('userData').stream()
        
        for doc in ref:
            for i in range(0,len(doc.to_dict()['ReadingPassage'])):
                df={}
                df['Email']=doc.to_dict()['email']
                df['ParagraphId']=doc.to_dict()['ReadingPassage'][i]['paragraph_id']
                df['Score']=doc.to_dict()['ReadingPassage'][i]['score']
                df['Feedback']=doc.to_dict()['ReadingPassage'][i]['feedback']
                lis.append(df)
        print(lis)
        return lis
    except:
        return None
print(getReadingComments())   
def getAudioComments():
    try:
        lis=[]
        ref=db.collection('userData').stream()
        for doc in ref:
            print(doc.to_dict()['AudioPassage'])
            for i in range(0,len(doc.to_dict()['AudioPassage'])):
                df={}
                df['Email']=doc.to_dict()['email']
                df['ParagraphId']=doc.to_dict()['AudioPassage'][i]['paragraph_id']
                df['Score']=doc.to_dict()['AudioPassage'][i]['score']
                df['Feedback']=doc.to_dict()['AudioPassage'][i]['feedback']
                lis.append(df)
        return lis
    except:
        return None
print(getAudioComments())
def checkUserInClass(email):
    try:
        print(email.strip())
        doc=pd.read_excel(r'static\resources\studentlist.xlsx')
        if email.strip() in doc['Email Id'].tolist():
    
            return True
        else:
            return False
    except:
        return None
