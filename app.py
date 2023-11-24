from utility import *
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import dotenv

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login',methods=['get','POST'])
def login():
    if request.method == 'POST':
        session.pop('_flashes', None)
        email = request.form['email']
        password = request.form['password']
        print(os.getenv("admin"))
        if(email==os.getenv("admin") and password==os.getenv("adminpass")):
            session['AloggedIn']=True
            return redirect(url_for('Admindashboard'))
        x=checkuser(email,password)
        if(x==1):
            flash("Please verify your email by clicking on the link sent to your email address")
        elif(x==-1):
            flash("Invalid email or password")
        elif(x==303):
            flash("something went wrong try after some time")
        elif(x==None):
            flash ("enter valid password or email or account not found")
        else:
            session['uuid']=x
            session['loggedIn']=True
            session['firstname']=getfirstname(x)
            return redirect(url_for('dashboard'))
            
    return render_template('login.html')



@app.route('/register',methods=['get','POST'])
def register():
    if request.method == 'POST':
        first = request.form['firstname']
        email = request.form['email']
        password = request.form['password']
        if(checkUserInClass(email)):
            print("success")
            check=createuser(email,password,first)
            if(check!=False):
                session['firstname']=first
                session['uuid']=check
                session['loggedin']=True
                return redirect(url_for('discription'))
            else:
                flash("Something went wrong try after some time")
                return redirect(url_for('register'))
        else:
            flash("You are not registered in this class")
            return redirect(url_for('register'))
    return render_template('register.html')




@app.route('/forgot')
def forgot():
    return render_template('forgot.html')



@app.route('/reset')
def reset():
    return render_template('reset.html')



@app.route('/user/dashboard')
def dashboard():
    if 'loggedIn' in session:
        return render_template('dashboard.html',firstname=session['firstname'],uuid=session['uuid'],ReadComData=getReadingPassageScoretoDb(session['uuid']),AudioComData=getAudioPassageScoretoDb(session['uuid']))
    return render_template('error_page_not_found.html')



@app.route('/user/dashboard/Exam',methods=['get','POST'])
def Exam():
    if 'loggedIn' in session:
        id=getparagraphId().strip()
        t=getQuestions("{}".format(id))
        print(t)
        d={}
        for i in t:
            d[i['question_id']]=i['answers']
        count=0
        details=getParagraphDetails(id)
        if request.method=='POST':
            for i in t:
                print(i['type'])
                if i['type']=='mcq':
                    if(request.form.getlist(i['question_id']) == d[i['question_id']].strip()):
                        count=count+1
                elif i['type']=='sat':
                    if(request.form[i['question_id']].strip()== d[i['question_id']].strip()):
                        count=count+1
                elif i['type']=='saq':
                    if(request.form[i['question_id']].strip()== d[i['question_id']].strip()):
                        count=count+1
            session['count']=count
            session['total']=len(t)
            addReadingPassageScoretoDb(session['uuid'],count,details[0]['paragraph_id'],request.form['feedback'])
            return redirect(url_for('result',score=count))
        return render_template('questions.html',t=t,f=details)
    
    return render_template('error_page_not_found.html')
        


@app.route('/user/dashboard/Exam/result')
def result():
    if 'loggedIn' in session:
        return render_template('scorecard.html',count=session['count'],total=session['total'],firstname=session['firstname'])
    return render_template('error_page_not_found.html')

@app.route('/user/dashboard/audioExam',methods=['get','POST'])
def audioExam():
    if 'loggedIn' in session:
         id=getAudioparagraphId().strip()
         t=getAudioQuestions("{}".format(id))
         print(t)
         d={}
         print(t)
         for i in t:
             d[i['question_id'.strip()]]=i['answers']
             
         print(d)
         count=0
         details=getAudioParagraphDetails(id)
         if request.method=='POST':
             for i in t:
                 print(i['type'])
                 if i['type']=='mcq':
                     if(request.form.getlist(i['question_id']) == d[i['question_id']].strip()):
                         count=count+1
                 elif i['type']=='sat':
                     if(request.form[i['question_id']].strip()== d[i['question_id']].strip()):
                         count=count+1
                 elif i['type']=='saq':
                     if(request.form[i['question_id']].strip()== d[i['question_id']].strip()):
                         count=count+1
             session['count']=count
             session['total']=len(t)
             addAudioPassageScoretoDb(session['uuid'],count,details[0]['paragraph_id'],request.form['feedback'])
             return redirect(url_for('result',score=count))
        
         return render_template('audioquestions.html',t=t,f=details,filename=details[0]['audioparagraph'])
    return render_template('error_page_not_found.html')



@app.route('/contact')
def contact():
    return "hello"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/register/discription')
def discription():
    if 'loggedin' in session:
        return render_template('displaycards.html')
    return render_template('error_page_not_found.html')



@app.route('/register/discription/1')
def info1():
    if 'loggedin' in session:
        return render_template('info1.html')
    return render_template('error_page_not_found.html')


    
@app.route('/register/discription/2')
def info2():
    if 'loggedin' in session:
        return render_template('info2.html')
    return render_template('error_page_not_found.html')


@app.route('/register/discription/3')
def info3():
    if 'loggedin' in session:
        return render_template('info3.html')
    return render_template('error_page_not_found.html')


@app.route('/register/discription/4')
def info4():
    if 'loggedin' in session:
        session.clear()
        return render_template('info4.html')
    return render_template('error_page_not_found.html')


@app.route('/user/AdminPortal')
def Admindashboard():
    if 'AloggedIn' in session:
        usercount=gettotalusers()
        userdetails=getuserdetails()
        return render_template('admin.html',usercount=usercount,userdetails=userdetails)
    else:
        return render_template('error_page_not_found.html')


@app.route('/user/AdminPortal/listen')
def ListeningDetails():
    if 'AloggedIn' in session:
        return render_template('adminl.html',CommentsDetails=getAudioComments())
    else:
        return render_template('error_page_not_found.html')
@app.route('/user/AdminPortal/reading')
def ReadingDetails():
    if 'AloggedIn' in session:
        return render_template('adminr.html',CommentsDetails=getReadingComments())
    else:
        return render_template('error_page_not_found.html')
    
app.run(debug=True)