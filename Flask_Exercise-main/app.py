from datetime import date
from operator import mod
from urllib import request
from flask import Flask, render_template, request
from datetime import datetime
date=datetime.now()
app = Flask(__name__)
global studentOrganisationDetails
studentOrganisationDetails = {
    'Name':[],
    'Organisation':[]
}
# Assign default 5 values to studentOrganisationDetails for Application  3.


@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate=date
    return render_template('index.html',currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    global evenOdd
    evenOdd='ERR'
    modNumber = mod(int(number),2)
    if modNumber==1:
        evenOdd='Odd'
    else:
        evenOdd='even'
    return render_template('result.html',evenOdd=evenOdd, number=number)
    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['org']
    global details
    details = {
        'Name': studentName,
        'Organisation' : studentOrg
    }
    studentOrganisationDetails['Name'].append(studentName)
    studentOrganisationDetails['Organisation'].append(studentOrg)
    # Append this value to studentOrganisationDetails
    return render_template('StudentDetails.html',studentOrganisationDetails = studentOrganisationDetails)
    # Display studentDetails.html with all students and organisations
