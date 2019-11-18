from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate,login,logout
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import random
from myapp.models import profile,tbl_employee
from myapp.models import SystemUserInformation
from myapp.models import AccessLevel
from myapp.models import EmployeeQRCode






from rest_framework.decorators import api_view
from rest_framework.response import Response

import pyqrcode
from django.http import JsonResponse
from django.core import serializers



import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.


# @api_view(['GET', 'POST'])
# def listnukiwa(request):
#     if request.method == 'POST':

        
#         data = tbl_nukiwa.objects.all()  
#         tmpJson = serializers.serialize("json",data)
#         tmpObj = json.loads(tmpJson)
#         return HttpResponse(json.dumps(tmpObj))
#     return Response({"message": "Hello, world!"})

from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def send_email_issue_resolved(request):
    data = {}
    if request.method == 'POST':
        print('ues')
        name_of_customer = request.POST['name']
        email = request.POST['email']
      

        message = Mail(
            from_email='vli.customercareph@gmail.com',
            to_emails= email,
            subject='Victory Liner Inc.',
            html_content=f'<p>Hi {name_of_customer}</p><p>&nbsp;</p><p style="color: green;">Our records show that your issue has been resolved.</p><p>Thanks for contacting us recently about your concern.However, if you still need our help, just hit &lsquo;reply&rsquo; to let us know and one of our team will be in touch shortly.</p><p>Best Regards</p><p>Customer Care Team.</p>')
        try:
            sg = SendGridAPIClient('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')
            print(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
            print(os.environ.get('SENDGRID_API_KEY'))

            
        data['statustxt'] = 'success'
        dump = json.dumps(data)
    
        return HttpResponse(dump,content_type='application/json')
    else:
        data['statustxt'] = 'method not allowed'
        dump = json.dumps(data)
        return HttpResponse(dump,content_type='application/json')




@csrf_exempt
def send_email(request):
    data = {}
    if request.method == 'POST':
        print('ues')
        name_of_customer = request.POST['name']
        issue = request.POST['issue']
        email = request.POST['email']
      

        message = Mail(
            from_email='vli.customercareph@gmail.com',
            to_emails= email,
            subject='Victory Liner Inc.',
            html_content=f'<p>Hey {name_of_customer},</p><p>I wanted to update you about the status of your issue.</p><p>Your {issue} is in progress and is being worked on by our product team. We are prioritizing your request, and I will make sure this issue is resolved. Thanks for your patience!</p><p>Best Regards</p><p>Customer Care Team.</p>')
        try:
            sg = SendGridAPIClient('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')
            print(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
            print(os.environ.get('SENDGRID_API_KEY'))
        

        data['statustxt'] = 'success'
        dump = json.dumps(data)
    
        return HttpResponse(dump,content_type='application/json')
    else:
        data['statustxt'] = 'method not allowed'
        dump = json.dumps(data)
        return HttpResponse(dump,content_type='application/json')
    
   

def CustomerConcernTerminalsOffice(request,id):
    ConcernFor = 'TerminalsOfficeShop'
    return render(request,'CustomerConcern.html',{
        'ConcernFor' : ConcernFor,
        'GlobalId' : id
    })


def CustomerConcern(request,id):
    ConcernFor = 'Bus'
    return render(request,'CustomerConcern.html',{
        'ConcernFor' : ConcernFor,
        'GlobalId' : id
    })




# sdd
def EmployeePerformance(request):
    return render(request,'EmployeePerformance.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'],
                'EmpCodeFinal' : request.session['empcode'] 

            } ,
           
    })




# sdd
def ConcernTopic(request):
    return render(request,'filemaintenance_concern.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            } ,
           
    })


def busses(request):
    return render(request,'busses.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            } ,
           
    })




def JobDescription(request):
    return render(request,'JobDescription.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            } ,
           
    })



def concern(request):
    return render(request,'concern.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
        'Is_CallCenter' :  request.session['Is_CallCenter'],
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'Is_CallCenter' :  request.session['Is_CallCenter'],
                'Is_CustomerService' : request.session['Is_CustomerService'],
                'Is_LegalDepartment' :  request.session['Is_LegalDepartment'],
                                     
                'empcode' : request.session['empcode'] 

            } ,
           
    })



def show201file(request,empcode):
    return render(request,'show_201file.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'],
                'empcode' : request.session['empcode']  

            } ,
            'empcode' : empcode

    })
def report(request):
    return render(request,'report.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
   'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            } 
    })

def settings_joblevel(request):
    return render(request,'settings_joblevel.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 

     'JobLevel' : request.session['JobLevel'],
        'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'],
                'empcode' : request.session['empcode']  

            }


    
     })

def settings_accounts(request):
    return render(request,'settings_accounts.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
        'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
    
     }) 

def settings_place_of_assignment(request):
    return render(request,'settings_place_of_assignment.html',{'JobLevel' : request.session['JobLevel'] ,
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
    
    }) 


def settings_evaluation_guide(request):
    return render(request,'settings_evaluationguide.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
            
             }) 


def settings_department(request):
    return render(request,'settings_departments.html',{'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
    
    }) 


def settings_violations(request):
    return render(request,'settings_violations.html',{'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }

    })


def settings_evaluation_sheet(request):
    return render(request,'settings_evaluation_sheet.html',{ 'JobLevel' : request.session['JobLevel'],
      'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 

    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            } })

def settings_general(request):
    return render(request,'settings_general.html',{ 'JobLevel' : request.session['JobLevel'] ,
    'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
             })

def settings(request):
    return render(request,'settings.html',{ 'JobLevel' : request.session['JobLevel'],
    'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }  })

def employee_information(request,id):
    return render(request,'dashboard.html',{ 
        'JobLevel' : request.session['JobLevel'] , 
        'FullName' : request.session['fullname'], 
        'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }
        
        })

def dashboard(request):
    if request.user.is_authenticated:
        print('yes')

    else:
        return redirect('/login/')
        
                     

    return render(request,'dashboard.html',{
        
        'JobLevel' : request.session['JobLevel'],
        'FullName' : request.session['fullname'], 
        'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }


    

        
    
     })

def deliberation(request):
    return render(request,'deliberation.html',{ 'empcode' : request.session['JobLevel'] ,
     'FullName' : request.session['fullname'], 
     'JobLevel' : request.session['JobLevel'],
      
        'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }

    
    
     })

def performance_evaluation(request):
    return render(request,'performance_evaluation.html',{ 
        
        'FullName' : request.session['fullname'], 
        'JobLevel' : request.session['JobLevel'] ,
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode'] 

            }


     })

def index(request):
    return render(request,'loading.html',{  })


def login_credential(request):
    return render(request,'login.html',{  })





def employee_module(request):
    return render(request,'employee.html',{'JobLevel' : request.session['JobLevel'],
    
        'FullName' : request.session['fullname'], 
    'UserLevel' : {
               
                'ReportsModule' : request.session['ReportsModule'],
                'EmployeePerformance' : request.session['EmployeePerformance'],
                'PerformanceEvaluationModule' : request.session['PerformanceEvaluationModule'],
                'DeliberationModule' :  request.session['DeliberationModule'],
                'SystemDashboardModule' : request.session['SystemDashboardModule'],
                'FileMaintenanceModule' : request.session['FileMaintenanceModule'],
                'FileMaintenance_General' : request.session['FileMaintenance_General'],
                'FileMaintenance_Accounts' : request.session['FileMaintenance_Accounts'],
                'FileMaintenance_EvaluationSheet' : request.session['FileMaintenance_EvaluationSheet'],
                'FileMaintenance_Departments' : request.session['FileMaintenance_Departments'],
                'FileMaintenance_Offense' : request.session['FileMaintenance_Offense'] ,
                'FileMaintenance_EvaluationGuide' : request.session['FileMaintenance_EvaluationGuide'],
                'FileMaintenance_PlaceofAssignment' : request.session['FileMaintenance_PlaceofAssignment'],
                'FileMaintenance_JobLevelorAccessLevel' : request.session['FileMaintenance_JobLevelorAccessLevel'],
                'FileMaintenance_201File' :  request.session['DeliberationModule'],
                'CustomerConcern' :  request.session['CustomerConcern'] ,
                'empcode' : request.session['empcode']

            }



    
     })




def viewme(request):
    url = 'http://127.0.0.1:8000/'
    client = requests.session()
    csrf = client.get(url).cookies['csrftoken']
    

    data = {
        'name': csrf,
        
     }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
    
    
    
    QrCodeType = models.ForeignKey('QrCodeType',on_delete = models.CASCADE)#fk
    QrCodeImage = models.CharField(max_length=255,null=True)   #image pathh
    QrcodeUrl = models.CharField(max_length=255,null=True) #info or 127.0.0.0:8000/id
    QrCodePlaceofAssignment = models.TextField(max_length=1020) #cubao    



import random
import datetime
from myapp.models import QrCodeGeneral,QrCodeType
@csrf_exempt  
def qrcode_generate_general(request):

        if request.method == 'POST':  
            #for single line
            randomval = random.randint(1, 10000)
            x = datetime.datetime.now()
            qrcodefilename = f'{x.day}{x.year}{randomval}'

            QRid= request.POST['QrCodeType_ID']
            placeofassignment = request.POST['PlaceofAssingment']
            hostname = request.POST['hostname']
            QRidentifier = qrcodefilename 

            qrimage = f'media/media/qrcode{qrcodefilename}.png'
            qrurlinformation = f'{hostname}CustomerConcern/{qrcodefilename}'
            big_code = pyqrcode.create(qrimage, error='L', version=5, mode='binary')
            big_code.png(f'{qrimage}', scale=6, module_color=[0, 0, 0, 128], )
            a = QrCodeType.objects.get(id = QRid)
            qr = QrCodeGeneral.objects.create(QrCodeType=a,QrCodeImage=qrimage,QrcodeUrl=qrurlinformation,QrCodePlaceofAssignment=placeofassignment)

            print(big_code)

            data = {
                                                'statustxt': 'success',
                                                'imagepath' : qrimage,
                                                'url' : qrurlinformation
                                               
                                                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        





@csrf_exempt  
def qrcode_generate(request):

        if request.method == 'POST':
            empcode = request.POST['empcode']
            hostname = request.POST['hostname']
            url = f'media/media/qrcode{empcode}.png'
            info = f'{hostname}CustomerConcern/{empcode}'
            big_code = pyqrcode.create(info, error='L', version=5, mode='binary')
            big_code.png(f'{url}', scale=6, module_color=[0, 0, 0, 128], )
            qr = EmployeeQRCode.objects.create(EmpCode=empcode,QrCode=url,Info=info)

            print(big_code)

            data = {
                                                'statustxt': 'success',
                                                'url' : url,
                                                'info' : info
                                                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        


from myapp.models import  BusQRCode
@csrf_exempt  
def Bus_qrcode_generate(request):

        if request.method == 'POST':
            busid = request.POST['busid']
            hostname = request.POST['hostname']
            url = f'media/media/busqrcode{busid}.png'
            info = f'{hostname}CustomerConcern/Bus/{busid}'
            big_code = pyqrcode.create(info, error='L', version=5, mode='binary')
            big_code.png(f'{url}', scale=6, module_color=[0, 0, 0, 128], )
            qr = BusQRCode.objects.create(BusID=busid,QrCode=url,Info=info)

            print(big_code)

            data = {
                                                'statustxt': 'success',
                                                'url' : url,
                                                'info' : info
                                                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')


from myapp.models import PlaceOfAssignmentQRCode
@csrf_exempt  
def Place_qrcode_generate(request): #placeofasignment
# http://127.0.0.1:8000/PasengerConcern/PlaceofAssignments/
        if request.method == 'POST':
            idplace = request.POST['id']
            hostname = request.POST['hostname']
            url = f'media/media/placeofassignmentqrcode{idplace}.png'
            info = f'{hostname}CustomerConcern/ByPlaceOfAssignment/{idplace}'
            big_code = pyqrcode.create(info, error='L', version=5, mode='binary')
            big_code.png(f'{url}', scale=6, module_color=[0, 0, 0, 128], )
            qr = PlaceOfAssignmentQRCode.objects.create(LocationID=idplace,QrCode=url,Info=info)

            print(big_code)

            data = {
                                                'statustxt': 'success',
                                                'url' : url,
                                                'info' : info
                                                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        


from myapp.models import UserLevelEachEmployee


@csrf_exempt
def user_login(request):
        #participant 1 = dpszhane 1478963
        #participant 2 = dpnukiwa 14563
        data ={}     
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username = username , password = password)
                if user:
                        login(request,user)
                        # data['user'] = user.username
                        # data['is_staff'] = user.is_staff
                        # data['is_superuser'] = user.is_superuser
                        # request.session['user'] = user.username
                        data['is_authenticated']  = user.is_authenticated
                        print(f'fasdfds fdfg {user.username}')
                        if user.username != 'admin' and user.username != 'Admin':
                            prof = profile.objects.get(account=user.id)
                            EmployeeAccessLevel = UserLevelEachEmployee.objects.get(EmpCode=prof.empcode)
                            print('success perdz')
                            employee = tbl_employee.objects.get(EmpCode=prof.empcode)
                            print(employee.EmpCode)
                            print(EmployeeAccessLevel.EmployeePerformance)
                            GetAccessModules = EmployeeAccessLevel
                            request.session['ReportsModule'] = GetAccessModules.ReportsModule
                            request.session['EmployeePerformance'] = GetAccessModules.EmployeePerformance
                            request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                            request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                            request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                            request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                            request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                            request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                            request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                            request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                            request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                            request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                            request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                            request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                            request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                            request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                            request.session['Is_CallCenter'] = GetAccessModules.Is_CallCenter
                            request.session['Is_CustomerService'] = GetAccessModules.Is_CustomerService
                            print(request.session['Is_CustomerService'])
                            request.session['Is_LegalDepartment'] = GetAccessModules.Is_LegalDepartment
                            request.session['empcode'] = employee.EmpCode
                            request.session['JobLevel'] = employee.JobLevel
                            request.session['fullname'] = f'{employee.FirstName}'

                        if user.username == 'admin':
                            request.session['JobLevel'] = 'Admin'
                            EmployeeAccessLevel = UserLevelEachEmployee.objects.get(EmpCode=user.username)
                            GetAccessModules = EmployeeAccessLevel
                            # GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                            request.session['fullname'] = 'Admin'
                            # GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                            
                            # get the modules
                            request.session['ReportsModule'] = GetAccessModules.ReportsModule
                            request.session['EmployeePerformance'] = GetAccessModules.EmployeePerformance
                            request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                            request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                            request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                            request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                            request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                            request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                            request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                            request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                            request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                            request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                            request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                            request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                            request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                            request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                            request.session['Is_CallCenter'] = GetAccessModules.Is_CallCenter
                            request.session['Is_CustomerService'] = GetAccessModules.Is_CustomerService
                            request.session['Is_LegalDepartment'] = GetAccessModules.Is_LegalDepartment
                            request.session['empcode'] = ''
                            request.session['JobLevel'] = 'admin'
                            request.session['fullname'] =''

                            dump = json.dumps(data)


                            return HttpResponse(dump, content_type='application/json')

                        
                        
                            

                        # print(user.username[0:3])
                        # if user.username[0:3] == 'sup':
                        #     # SystemUserInformation
                        #     request.session['JobLevel'] = 'supervisory'
                            
                           
                            
                        #     GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                        #     print(GetAccessLevel.id)
                        #     print(GetAccessLevel.AccessLevel)
                            
                        #     request.session['fullname'] = GetAccessLevel.FullName
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                        #     print(GetAccessModules.id)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                        #     request.session['empcode'] = 'NA'


                        # print(user.username[0:10])
                        # if user.username[0:10] == 'CallCenter':
                        #     # SystemUserInformation
                        #     request.session['JobLevel'] = 'CallCenter'
                           
                            
                        #     GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                        #     print(GetAccessLevel.id)
                        #     print(GetAccessLevel.AccessLevel)
                            
                        #     request.session['fullname'] = GetAccessLevel.FullName
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                        #     print(GetAccessModules.id)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                        #     request.session['empcode'] = 'NA'


                        # print(user.username[0:8])
                        # if user.username[0:8] == 'Customer':
                        #     # SystemUserInformation
                        #     request.session['JobLevel'] = 'CustomerService'
                        #     print('CustomerService')
                            
                        #     GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                        #     print(GetAccessLevel.id)
                        #     print(GetAccessLevel.AccessLevel)
                            
                        #     request.session['fullname'] = GetAccessLevel.FullName
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                        #     print(GetAccessModules.id)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                        #     request.session['empcode'] = 'NA'

                        # print(user.username)
                        # print(user.username[0:5])
                        # if user.username[0:5] == 'Legal':
                        #     # SystemUserInformation
                        #     request.session['JobLevel'] = 'LegalDepartment'
                        #     print('Legal Department')
                            
                        #     GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                        #     print(GetAccessLevel.id)
                        #     print(GetAccessLevel.AccessLevel)
                            
                        #     request.session['fullname'] = GetAccessLevel.FullName
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                        #     print(GetAccessModules.id)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern
                        #     request.session['empcode'] = 'NA'

                        # if user.username[0:2] == 'dp':
                        #     # SystemUserInformation
                        #     request.session['JobLevel'] = 'dbparticipant'
                        #     print('deliberation participant')
                            
                        #     GetAccessLevel = SystemUserInformation.objects.get(account=user.id)
                        #     print(GetAccessLevel.AccessLevel)
                        #     request.session['empcode'] = 'NA'
                        #     request.session['fullname'] = GetAccessLevel.FullName
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=GetAccessLevel.AccessLevel)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern

                        # prof = profile.objects.get(account=user.id)
                        # p = prof.empcode
                        # employee = tbl_employee.objects.get(EmpCode=p)
                        # print(f'adsfdsf {employee.JobLevel}')
                        # if  'rank' in employee.JobLevel or 'Rank' in employee.JobLevel: 
                            
                            
                        #     print(employee)
                        #     prof = profile.objects.get(account=user.id)
                        #     p = prof.empcode
                            
                        #     employee = tbl_employee.objects.get(EmpCode=p)
                        #     request.session['empcode'] = employee.EmpCode
                        #     aaa = request.session['empcode']

                        #     print(f'randprint-- {aaa  }')
                        #     JobLevel = employee.JobLevel.lower()
                        #     request.session['JobLevel'] = employee.JobLevel
                        #     request.session['fullname'] = employee.FirstName
                        #     print(JobLevel)
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=JobLevel)
                        #     # get the modules
                            
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern


                        #for new accounts-----------------
                        # #Only EMployee use this
                        
                        
                        # if  user.username != 'admin' and user.username[0:2] != 'dp' and  user.username[0:5] != 'Legal' and  user.username[0:8] != 'Customer' != user.username[0:8] == 'CallCenter': 
                        #     prof = profile.objects.get(account=user.id)
                        #     employee = tbl_employee.objects.get(EmpCode=prof.empcode)
                        #     print(employee)
                        #     print('randprint')
                        #     JobLevel = employee.JobLevel
                        #     request.session['JobLevel'] = employee.JobLevel
                        #     request.session['fullname'] = employee.FirstName
                        #     print(JobLevel)
                        #     GetAccessModules = AccessLevel.objects.get(NameofUserLevel=JobLevel)
                        #     # get the modules
                        #     request.session['ReportsModule'] = GetAccessModules.ReportsModule
                        #     request.session['PerformanceEvaluationModule'] = GetAccessModules.PerformanceEvaluationModule
                        #     request.session['SystemDashboardModule'] =GetAccessModules.SystemDashboardModule
                        #     request.session['FileMaintenanceModule'] = GetAccessModules.FileMaintenanceModule
                        #     request.session['FileMaintenance_General'] = GetAccessModules.FileMaintenance_General
                        #     request.session['FileMaintenance_Accounts'] = GetAccessModules.FileMaintenance_Accounts
                        #     request.session['FileMaintenance_EvaluationSheet'] = GetAccessModules.FileMaintenance_EvaluationSheet
                        #     request.session['FileMaintenance_Departments'] = GetAccessModules.FileMaintenance_Departments
                        #     request.session['FileMaintenance_Offense'] = GetAccessModules.FileMaintenance_Offense
                        #     request.session['FileMaintenance_EvaluationGuide'] = GetAccessModules.FileMaintenance_EvaluationGuide
                        #     request.session['FileMaintenance_PlaceofAssignment'] = GetAccessModules.FileMaintenance_PlaceofAssignment
                        #     request.session['FileMaintenance_JobLevelorAccessLevel'] = GetAccessModules.FileMaintenance_JobLevelorAccessLevel
                        #     request.session['FileMaintenance_201File'] = GetAccessModules.FileMaintenance_201File
                        #     request.session['DeliberationModule'] = GetAccessModules.DeliberationModule
                        #     request.session['CustomerConcern'] = GetAccessModules.CustomerConcern



                       
                        

                        dump = json.dumps(data)


                        return HttpResponse(dump, content_type='application/json')

                      
                else:   
                        request.session['JobLevel'] = 'none'

                        data['user'] = 'none'
                        data['is_authenticated'] = False
                        dump = json.dumps(data)

                        return HttpResponse(dump, content_type='application/json')
        
@csrf_exempt
def user_logout(request):
        if request.method == 'POST':
               
                data ={}
                logout(request)
                data['user'] = 'logout'
                return redirect('/login/')
                dump = json.dumps(data)

                return HttpResponse(dump, content_type='application/json')
      

       
@csrf_exempt
def createaccount(request):
        if request.method == 'POST':
                data = {}
                empcode = request.POST['empcode']
                firstname = request.POST['firstname']
                firstlettername = firstname[0:1]     
                username = f'{empcode}{firstlettername.lower()}'
                password = 'victoryliner'
               
                userinstance = User.objects.create_user(username = username, password = password,is_staff=True)
                if userinstance :
                    print(userinstance.username)
                    print(f'id : {userinstance.id}')
                    print(f'pass: {password}')
                    data['id'] = userinstance.id   
                    data['statustxt'] = 'success'
                    profile.objects.create(account = userinstance , empcode = empcode)



                else:
                     data['statustxt'] = 'error'
                
                        
                                           
                

                dump = json.dumps(data)
                return HttpResponse(dump,content_type='application/json')
                

                
                # create_superuser
                # create_rankandfile
                # create_managerial
                # create_supervisory
                # create_staffus

from django.contrib.auth.models import User

@csrf_exempt
def updatePasswordAdmin(request):
    if request.method == 'POST':
        print('check')
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        u = User.objects.get(username__exact=username)
        u.set_password(newpassword)
        u.save()
        if u:
            print('password change')
            data = {}
            data['statustxt'] = 'success'
            dump = json.dumps(data)
            return HttpResponse(dump,content_type='application/json')
       
        
        

    

