# add this 'rest_framework', on installed app(settings)
from rest_framework import serializers
# add this 'rest_framework', on installed app(settings)
from rest_framework import serializers
from myapp.models import tbl_employee,User
from django.views.decorators.csrf import csrf_exempt


from myapp.models import UserLevelEachEmployee
class UserLevelEachEmployee_Serializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = UserLevelEachEmployee
        fields = ('url','id','EmpCode','EmployeePerformance','ReportsModule','PerformanceEvaluationModule','SystemDashboardModule','FileMaintenanceModule','FileMaintenance_General','FileMaintenance_Accounts','FileMaintenance_EvaluationSheet','FileMaintenance_Departments','FileMaintenance_Offense','FileMaintenance_EvaluationGuide','FileMaintenance_PlaceofAssignment','FileMaintenance_JobLevelorAccessLevel','FileMaintenance_201File','DeliberationModule','CustomerConcern','Is_CallCenter','Is_CustomerService','Is_LegalDepartment','date_created','date_updated',)






from myapp.models import UploadProof
class UploadProof_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = UploadProof
        fields = ('url','id','CustomerConcernID','Proof','date_created','date_updated',)


#QRcode
from myapp.models import PlaceOfAssignmentQRCode
class PlaceOfAssignmentQRCode_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = PlaceOfAssignmentQRCode
        fields = ('url','id','LocationID','QrCode','Info','date_created','date_updated',)


#QRcode
from myapp.models import BusQRCode
class BusQRCode_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = BusQRCode
        fields = ('url','id','BusID','QrCode','Info','date_created','date_updated',)




from myapp.models import BusCategory
class BusCategory_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = BusCategory
        fields = ('url','id','BusCategoryName',)


from myapp.models import Busses
class Busses_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = Busses
        fields = ('url','id','BusNo','Type','PlaceOfAssignment','date_created','date_updated',)


#QRtype
from myapp.models import QrCodeGeneral
class QrCodeGeneral_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = QrCodeGeneral
        fields = ('url','id','QrCodeType','QrCodeImage','QrcodeUrl','QrCodePlaceofAssignment','date_created','date_updated',)


#QRtype
from myapp.models import QrCodeType
class QrCodeType_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = QrCodeType
        fields = ('url','id','Type','SystenLabel','date_created','date_updated',)


#Jobdescription
from myapp.models import JobDescription
class JobDescription_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = JobDescription
        fields = ('url','id','Department','JobTitle','Section','ReportsTo','Content','date_created','date_updated',)



#QRcode
from myapp.models import EmployeeQRCode
class EmployeeQRCode_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = EmployeeQRCode
        fields = ('url','id','EmpCode','QrCode','Info','date_created','date_updated',)




#Customer Concern
from myapp.models import CustomerConcern
class CustomerConcern_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = CustomerConcern
        fields = ('url','id','ConcernType','ConcernCategory','ConcernCategoryIDPlace','EmpCode','Name','MobileNumber','Email','Topic','OtherConcern','YourConcern','IsToCallCenter','IsToCustomerService','IsToLegal','IsDone','date_created','date_updated',)


#Customer Concern
from myapp.models import ConcernCategory
class ConcernCategory_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = ConcernCategory 
        fields = ('url','id','CategoryName','date_created','date_updated',)



#get score
from myapp.models import EvaluationScore
class EvaluationScore_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = EvaluationScore
        fields = ('url','id','evaluation_period','Criteria','Month','Score','ScoreFinal','date_created','date_updated',)




#department use the evaluation
from myapp.models import SystemUserInformation
class SystemUser_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = SystemUserInformation
        fields = ('url','id','account','FullName','Email','AccessLevel','date_created','date_updated',)


#department use the evaluation
from myapp.models import AccessLevel
class ACCESSLEVEL_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = AccessLevel
        fields = ('url','id','NameofUserLevel','EmployeePerformance','ReportsModule','PerformanceEvaluationModule','SystemDashboardModule','FileMaintenanceModule','FileMaintenance_General','FileMaintenance_Accounts','FileMaintenance_EvaluationSheet','FileMaintenance_Departments','FileMaintenance_Offense','FileMaintenance_EvaluationGuide','FileMaintenance_PlaceofAssignment','FileMaintenance_JobLevelorAccessLevel','FileMaintenance_201File','DeliberationModule','CustomerConcern','Is_CallCenter','Is_CustomerService','Is_LegalDepartment','date_created','date_updated',)




#department use the evaluation
from myapp.models import whichdepartment
class WHICH_DEPARTMENT_USE_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = whichdepartment
        fields = ('url','id','kind_of_evaluation','department','date_created','date_updated',)





#hrcopy


from myapp.models import evaluationresult_hr_copy
class EVALUATION_COPY_HR_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = evaluationresult_hr_copy
        fields = ('url','id','empcode','evaluation_sheet','employeefullname','datehired','jobstatus','supervisorrater','send','designation','departmentsection','placeofassignment','readyfordeliberation','delibationisdone','date_created','date_updated',)


from myapp.models import partipantsvote
class PARTICIPANTS_VOTE_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = partipantsvote
        fields = ('url','id','evaluation_sheet','participants','finaldecision','date_created','date_updated',)



from myapp.models import bootchats
class BOOT_CHATS_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = bootchats
        fields = ('url','id','evaluation_sheet','messages','who','avatar','date_created','date_updated',)




#evaluation period
from myapp.models import tbl_evaluation_period
class EVALUATION_PERIOD_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = tbl_evaluation_period
        fields = ('url','id','empcode','employeefullname','datehired','designation','departmentsection','placeofassignment','supervisorrater','evaluation_period','length_period','date_created','date_updated',)


    


#evaluation period
from myapp.models import tbl_evaluation_period_per_month
class PER_MONTHSerializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = tbl_evaluation_period_per_month
        fields = ('url','id','empcode','evaluation_period','month_name','remarks','date_created','date_updated',)


#evaluation period
from myapp.models import tbl_period_of_evaluation_per_criteria
class PER_CRITERIASerializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = tbl_period_of_evaluation_per_criteria
        fields = ('url','id','empcode','evaluation_period_per_month','criteria','score','remarks','evaluator','date_created','date_updated',)




from myapp.models import evaluationsheetuse
class JOBSTATUS_USESerializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = evaluationsheetuse
        fields = ('url','id','kind_of_evaluation','jobtstatus','date_created','date_updated',)


from myapp.models import joblevel
class JobLevelSerializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = joblevel
        fields = ('url','id','joblevel','date_created','date_updated',)



from myapp.models import employee_201_document
class Employee_201_DocumentSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = employee_201_document
        fields = ('url','id','category','classification','Description','empcode','files','date_created','date_updated',)

from myapp.models import employee_201_file
class Employee_201_Serializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = employee_201_file
        fields = ('url','id','category','date_created','date_updated',)




from myapp.models import profile
class ProfileSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = profile
        fields = ('url','id','account','empcode','markasread','date_created','date_updated',)






from myapp.models import place_of_assignment_location
class LocationSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = place_of_assignment_location
        fields = ('url','id','location','category','date_created','date_updated',)


from myapp.models import place_of_assignment_category
class CategorySerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = place_of_assignment_category
        fields = ('url','id','category','date_created','date_updated',)


from myapp.models import department

class DepartmentSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = department
        fields = ('url','id','department','date_created','date_updated',)

from myapp.models import minor_grave
class Minor_GraveSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = minor_grave
        fields = ('url','id','typeofviolation','percentage','date_created','date_updated',)

from myapp.models import violations
class ViolationsSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model =  violations
        fields = ('url','id','NatureofOffense','graveofminor','date_created','date_updated',)





from myapp.models import violation_department_percriteria
class Violation_Department_PercriteriaSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model =  violation_department_percriteria
        fields = ('url','id','kind_of_evaluation','department','criteria','offense','date_created','date_updated',)






from myapp.models import passing_grade
class Passing_GradeSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = passing_grade
        fields = ('url','id','passing_grades',)


class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = tbl_employee
        fields = ('url','id','EmpCode','PlaceOfAssignment','JobStatus','LastName','FirstName','MiddleName','Suffix','NickName','JobLevel','Department','Designation','ContactNumber','Email','datehired')



from myapp.models import time_keeping
class TimeKeepingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = time_keeping
        fields = ('url','id','EmpCode','Name','DateIn','TimeIn','DateOut','TimeOut','Department','Position','date_created','date_updated')

from myapp.models import tvr
class tvrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tvr
        fields = ('url','id','EmpCode','CaseNO','IncidentDate','Type','NatureofOffense','Decision','DateofDecision','ReportedBy','date_created','date_updated')



from myapp.models import dispatch
class DispatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dispatch
        fields = ('url','id','EmpCode','FullName','EmpPosition','Location','Active','DepartureTime','ArrivalTime','KMRun','Busno','Route','date_created','date_updated')





from django.contrib.auth.models import User
class UserSerializers(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = User
        fields = ('url','id','username','password','is_staff','is_superuser','is_active',)


# class UserSerializers(serializers.HyperlinkedModelSerializer):
   
#     class Meta:
#         model = User
#         fields = ('url','id','empcode','username','password','admin','staff','active','first_time_login')




from myapp.models import evaluation_score
class evaluation_score_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = evaluation_score
        fields = ('url','id','kind_of_evaluation','criteria','description','percentage','employee','score','monthname','identifier','date_created','date_updated',)

from myapp.models import evaluation_sheet
class evaluation_sheet_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = evaluation_sheet
        fields = ('url','id','kind_of_evaluation','description','date_created','date_updated',)


from myapp.models import criteria
class criteria_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = criteria
        fields = ('url','id','kind_of_evaluation','criteria','description','percentage','date_created','date_updated',)


from myapp.models import tbl_jobtstatus
class evaluation_period_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tbl_jobtstatus
        fields = ('url','id','for_employee_status','month_period','description','date_created','date_updated',)


from myapp.models import evaluation_period_headername
class evaluation_period_headername_serialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = evaluation_period_headername
        fields = ('url','id','for_employee_status','header_content','date_created','date_updated',)


# use get ===============================================================


from myapp.models import evaluation_period_headername
class Get_evaluation_period_headername_serialize(serializers.HyperlinkedModelSerializer):
    for_employee_status =  serializers.StringRelatedField()
    class Meta:
        model = evaluation_period_headername
        fields = ('url','id','for_employee_status','header_content','date_created','date_updated',)



from myapp.models import criteria
class Get_criteria_serialize(serializers.HyperlinkedModelSerializer):
    kind_of_evaluation =  serializers.StringRelatedField()
    class Meta:
        model = criteria
        fields = ('url','id','kind_of_evaluation','criteria','description','percentage','date_created','date_updated',)



from myapp.models import evaluation_score
class Get_evaluation_score_serialize(serializers.HyperlinkedModelSerializer):
    kind_of_evaluation =  serializers.StringRelatedField()
    employee = serializers.StringRelatedField()
    class Meta:
        model = evaluation_score
        fields = ('url','id','kind_of_evaluation','criteria','description','percentage','employee','score','monthname','identifier','date_created','date_updated',)



from myapp.models import violations
class Get_ViolationsSerializers(serializers.HyperlinkedModelSerializer):
    graveofminor =  serializers.StringRelatedField()
    class Meta:
        model =  violations
        fields = ('url','id','NatureofOffense','graveofminor','date_created','date_updated',)



from myapp.models import violation_department_percriteria
class GET_Violation_Department_PercriteriaSerializers(serializers.HyperlinkedModelSerializer):
    kind_of_evaluation =  serializers.StringRelatedField()
    department =  serializers.StringRelatedField()
    criteria =  serializers.StringRelatedField()
    offense =  serializers.StringRelatedField()
    class Meta:
        model =  violation_department_percriteria
        fields = ('url','id','kind_of_evaluation','department','criteria','offense','date_created','date_updated',)



from myapp.models import place_of_assignment_location
class Get_LocationSerializers(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = place_of_assignment_location
        fields = ('url','id','location','category','date_created','date_updated',)



from myapp.models import profile
class Get_ProfileSerializers(serializers.HyperlinkedModelSerializer):
    account = serializers.StringRelatedField()
    class Meta:
        model = profile
        fields = ('url','id','account','empcode','markasread','date_created','date_updated',)




from myapp.models import employee_201_document
class Get_Employee_201_DocumentSerializers(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = employee_201_document
        fields = ('url','id','category','classification','Description','empcode','files','date_created','date_updated',)


from myapp.models import evaluationsheetuse
class GET_JOBSTATUS_USESerializers(serializers.HyperlinkedModelSerializer):  
    kind_of_evaluation = serializers.StringRelatedField()
    jobtstatus = serializers.StringRelatedField()
    class Meta:
        model = evaluationsheetuse
        fields = ('url','id','kind_of_evaluation','jobtstatus','date_created','date_updated',)



#evaluation period
from myapp.models import tbl_evaluation_period_per_month
class GET_PER_MONTHSerializers(serializers.HyperlinkedModelSerializer):
    evaluation_period = serializers.StringRelatedField()
    class Meta:
        model = tbl_evaluation_period_per_month
        fields = ('url','id','empcode','evaluation_period','month_name','remarks','date_created','date_updated',)



from myapp.models import evaluationresult_hr_copy
class GET_EVALUATION_COPY_HR_Serializers(serializers.HyperlinkedModelSerializer):  
    evaluation_sheet = serializers.StringRelatedField()
    class Meta:
        model = evaluationresult_hr_copy
        fields = ('url','id','empcode','evaluation_sheet','employeefullname','datehired','jobstatus','supervisorrater','send','designation','departmentsection','placeofassignment','readyfordeliberation','delibationisdone','date_created','date_updated',)




from myapp.models import tbl_period_of_evaluation_per_criteria
class GET_PER_CRITERIASerializers(serializers.HyperlinkedModelSerializer): 
    evaluation_period_per_month = serializers.StringRelatedField()

    class Meta:
        model = tbl_period_of_evaluation_per_criteria
        fields = ('url','id','empcode','evaluation_period_per_month','criteria','score','remarks','evaluator','date_created','date_updated',)

from myapp.models import partipantsvote
class GET_PARTICIPANTS_VOTE_Serializers(serializers.HyperlinkedModelSerializer):  
    evaluation_sheet  = serializers.StringRelatedField()
    class Meta:
        model = partipantsvote
        fields = ('url','id','evaluation_sheet','participants','finaldecision','date_created','date_updated',)


from myapp.models import whichdepartment
class GET_WHICH_DEPARTMENT_USE_Serializers(serializers.HyperlinkedModelSerializer): 
    kind_of_evaluation = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    class Meta:
        model = whichdepartment
        fields = ('url','id','kind_of_evaluation','department','date_created','date_updated',)




from myapp.models import CustomerConcern
class GET_CustomerConcern_Serializers(serializers.HyperlinkedModelSerializer):  
    ConcernCategory = serializers.StringRelatedField()
    class Meta:
        model = CustomerConcern
        fields = ('url','id','ConcernType','ConcernCategory','ConcernCategoryIDPlace','EmpCode','Name','MobileNumber','Email','Topic','OtherConcern','YourConcern','IsToCallCenter','IsToCustomerService','IsToLegal','IsDone','date_created','date_updated',)


#Jobdescription
from myapp.models import JobDescription
class GET_JobDescription_Serializers(serializers.HyperlinkedModelSerializer): 
    Department = serializers.StringRelatedField() 
    class Meta:
        model = JobDescription
        fields = ('url','id','Department','JobTitle','Section','ReportsTo','Content','date_created','date_updated',)





from myapp.models import QrCodeGeneral
class GET_QrCodeGeneral_Serializers(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = QrCodeGeneral
        fields = ('url','id','QrCodeType','QrCodeImage','QrcodeUrl','QrCodePlaceofAssignment','date_created','date_updated',)




from myapp.models import UploadProof
class GET_UploadProof_Serializers(serializers.HyperlinkedModelSerializer): 
    CustomerConcernID = serializers.StringRelatedField()
    class Meta:
        model = UploadProof
        fields = ('url','id','CustomerConcernID','Proof','date_created','date_updated',)




from myapp.models import Busses
class GET_Busses_Serializers(serializers.HyperlinkedModelSerializer):  
    Type = serializers.StringRelatedField()
    class Meta:
        model = Busses
        fields = ('url','id','BusNo','Type','PlaceOfAssignment','date_created','date_updated',)
