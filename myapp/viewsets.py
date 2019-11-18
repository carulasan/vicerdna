
from rest_framework import  viewsets,filters

from rest_framework.permissions import IsAuthenticated

from myapp.models import tbl_employee,User


from myapp.serializer import EmployeeSerializers




from myapp.serializer import UserLevelEachEmployee_Serializer
from myapp.models import  UserLevelEachEmployee
class UserLevelEachEmployee_Viewset(viewsets.ModelViewSet):
    queryset =  UserLevelEachEmployee.objects.all()
    serializer_class =  UserLevelEachEmployee_Serializer


from myapp.serializer import UploadProof_Serializers
from myapp.models import UploadProof
class UploadProof_Viewsets(viewsets.ModelViewSet):
    queryset =  UploadProof.objects.all()
    serializer_class = UploadProof_Serializers

from myapp.serializer import PlaceOfAssignmentQRCode_Serializers
from myapp.models import PlaceOfAssignmentQRCode
class PlaceOfAssignmentQRCode_Viewsets(viewsets.ModelViewSet):
    queryset =  PlaceOfAssignmentQRCode.objects.all()
    serializer_class = PlaceOfAssignmentQRCode_Serializers



from myapp.serializer import BusQRCode_Serializers
from myapp.models import BusQRCode
class BusQRCode_Viewsets(viewsets.ModelViewSet):
    queryset =  BusQRCode.objects.all()
    serializer_class = BusQRCode_Serializers



from myapp.serializer import BusCategory_Serializers
from myapp.models import BusCategory
class BusCategory_Viewsets(viewsets.ModelViewSet):
    queryset =  BusCategory.objects.all()
    serializer_class =  BusCategory_Serializers


from myapp.serializer import Busses_Serializers
from myapp.models import  Busses
class Busses_Viewsets(viewsets.ModelViewSet):
    queryset =  Busses.objects.all()
    serializer_class = Busses_Serializers


from myapp.serializer import JobDescription_Serializers
from myapp.models import  JobDescription
class JobDescription_Viewsets(viewsets.ModelViewSet):
    queryset =  JobDescription.objects.all()
    serializer_class = JobDescription_Serializers


from myapp.serializer import EmployeeQRCode_Serializers
from myapp.models import  EmployeeQRCode
class EmployeeQRCode_Viewsets(viewsets.ModelViewSet):
    queryset =  EmployeeQRCode.objects.all()
    serializer_class = EmployeeQRCode_Serializers


from myapp.serializer import GET_CustomerConcern_Serializers
from myapp.models import  CustomerConcern
class GET_CustomerConcern_Viewsets(viewsets.ModelViewSet):
    queryset =  CustomerConcern.objects.all()
    serializer_class =  GET_CustomerConcern_Serializers




from myapp.serializer import CustomerConcern_Serializers
from myapp.models import  CustomerConcern
class CustomerConcern_Viewsets(viewsets.ModelViewSet):
    queryset =  CustomerConcern.objects.all()
    serializer_class =   CustomerConcern_Serializers



from myapp.serializer import ConcernCategory_Serializers
from myapp.models import ConcernCategory
class ConcernCategory_Viewsets(viewsets.ModelViewSet):
    queryset =  ConcernCategory.objects.all()
    serializer_class =   ConcernCategory_Serializers


#system user
from myapp.serializer import EvaluationScore_Serializers
from myapp.models import  EvaluationScore
class EvaluationScoreViewsets(viewsets.ModelViewSet):
    queryset =  EvaluationScore.objects.all()
    serializer_class =  EvaluationScore_Serializers

#system user
from myapp.serializer import SystemUser_Serializers
from myapp.models import  SystemUserInformation



class SystemUser_Viewset(viewsets.ModelViewSet):
    queryset =  SystemUserInformation.objects.all()
    serializer_class =  SystemUser_Serializers
    


#accesslevel probationary
from myapp.serializer import ACCESSLEVEL_Serializers
from myapp.models import  AccessLevel
class ACCESSLEVEL_Viewset(viewsets.ModelViewSet):
    queryset =  AccessLevel.objects.all()
    serializer_class =  ACCESSLEVEL_Serializers
    


#which department use ths kind of evaluation
from myapp.serializer import WHICH_DEPARTMENT_USE_Serializers
from myapp.models import  whichdepartment

class WhichDepartment_Use_Kind_of_EvaluationViewset(viewsets.ModelViewSet):
    queryset =  whichdepartment.objects.all()
    serializer_class =  WHICH_DEPARTMENT_USE_Serializers
    






#HRCOPY

from myapp.serializer import  EVALUATION_COPY_HR_Serializers
from myapp.models import  evaluationresult_hr_copy

class  EVALUATION_HR_COPY_Viewset(viewsets.ModelViewSet):
    queryset =  evaluationresult_hr_copy.objects.all()
    serializer_class =  EVALUATION_COPY_HR_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id',)


from myapp.serializer import  PARTICIPANTS_VOTE_Serializers
from myapp.models import   partipantsvote

class  PARTICIPANTS_VOTE_Viewset(viewsets.ModelViewSet):
    queryset =   partipantsvote.objects.all()
    serializer_class =  PARTICIPANTS_VOTE_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id',)


from myapp.serializer import BOOT_CHATS_Serializers
from myapp.models import    bootchats

class  BOOT_CHATS_Viewset(viewsets.ModelViewSet):
    queryset =   bootchats.objects.all()
    serializer_class =  BOOT_CHATS_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id',)




from myapp.serializer import  EVALUATION_PERIOD_Serializers
from myapp.models import  tbl_evaluation_period

class  EVALUATION_PERIODViewset(viewsets.ModelViewSet):
    queryset =  tbl_evaluation_period.objects.all()
    serializer_class = EVALUATION_PERIOD_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id',)


from myapp.serializer import  PER_MONTHSerializers
from myapp.models import  tbl_evaluation_period_per_month
class  PER_MONTHViewset(viewsets.ModelViewSet):
    queryset =  tbl_evaluation_period_per_month.objects.all()
    serializer_class = PER_MONTHSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')


from myapp.serializer import  PER_CRITERIASerializers
from myapp.models import  tbl_period_of_evaluation_per_criteria
class PER_CRITERIAViewset(viewsets.ModelViewSet):
    queryset =  tbl_period_of_evaluation_per_criteria.objects.all()
    serializer_class =  PER_CRITERIASerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')







# ,UserSerializers






from myapp.serializer import  JOBSTATUS_USESerializers
from myapp.models import  evaluationsheetuse
class  JOBSTATUS_USEViewset(viewsets.ModelViewSet):
    queryset =  evaluationsheetuse.objects.all()
    serializer_class = JOBSTATUS_USESerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('jobtstatus__jobtstatus','id')


from myapp.serializer import  JobLevelSerializers
from myapp.models import joblevel
class  JobLevelViewset(viewsets.ModelViewSet):
    queryset =  joblevel.objects.all()
    serializer_class = JobLevelSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('joblevel','id')


from myapp.serializer import  Employee_201_DocumentSerializers
from myapp.models import employee_201_document
class  Employee_201_DocumentViewset(viewsets.ModelViewSet):
    queryset =  employee_201_document.objects.all()
    serializer_class = Employee_201_DocumentSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('Description','id')



from myapp.serializer import  Employee_201_Serializers
from myapp.models import employee_201_file
class  Employee_201_Viewset(viewsets.ModelViewSet):
    queryset =  employee_201_file.objects.all()
    serializer_class =  Employee_201_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category','id')


from myapp.serializer import ProfileSerializers
from myapp.models import profile
class ProfileViewset(viewsets.ModelViewSet):
    queryset =  profile.objects.all()
    serializer_class = ProfileSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')





from myapp.serializer import LocationSerializers
from myapp.models import place_of_assignment_location
class LocationViewset(viewsets.ModelViewSet):
    queryset =  place_of_assignment_location.objects.all()
    serializer_class = LocationSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('location','id')


from myapp.serializer import CategorySerializers
from myapp.models import place_of_assignment_category
class CategoryViewset(viewsets.ModelViewSet):
    queryset = place_of_assignment_category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category','id')


from myapp.serializer import DepartmentSerializers
from myapp.models import department
class  DepartmentViewset(viewsets.ModelViewSet):
    queryset = department.objects.all()
    serializer_class = DepartmentSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('department','id')



from myapp.serializer import Minor_GraveSerializers
from myapp.models import minor_grave
class  Minor_GraveViewset(viewsets.ModelViewSet):
    queryset = minor_grave.objects.all()
    serializer_class = Minor_GraveSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('typeofviolation','id')  


from myapp.serializer import ViolationsSerializers
from myapp.models import violations
class  ViolationsViewset(viewsets.ModelViewSet):
    queryset =violations.objects.all()
    serializer_class = ViolationsSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('NatureofOffense','graveofminor','id')  



from myapp.serializer import  Violation_Department_PercriteriaSerializers
from myapp.models import violation_department_percriteria
class  Violation_Department_PercriteriaViewset(viewsets.ModelViewSet):
    queryset = violation_department_percriteria.objects.all()
    serializer_class = Violation_Department_PercriteriaSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('kind_of_evaluation__kind_of_evaluation','id')  




from myapp.serializer import Passing_GradeSerializers
from myapp.models import passing_grade
class  Passing_GradeViewset(viewsets.ModelViewSet):
    queryset = passing_grade.objects.all()
    serializer_class = Passing_GradeSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('passing_grades','id')


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = tbl_employee.objects.all()
    serializer_class = EmployeeSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('EmpCode','id')


from myapp.serializer import TimeKeepingSerializer
from myapp.models import time_keeping
class TimeKeepingViewset(viewsets.ModelViewSet):
    queryset = time_keeping.objects.all()
    serializer_class = TimeKeepingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('EmpCode','id')


from myapp.serializer import tvrSerializer
from myapp.models import tvr
class TvrViewset(viewsets.ModelViewSet):
    queryset = tvr.objects.all()
    serializer_class = tvrSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('EmpCode','id')

from myapp.serializer import DispatchSerializer
from myapp.models import dispatch
class DispatchViewset(viewsets.ModelViewSet):
    queryset = dispatch.objects.all()
    serializer_class = DispatchSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('EmpCode','id')




from django.contrib.auth.models import User
from myapp.serializer import  UserSerializers
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','id')

    

# class UserViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('username','id')



from myapp.serializer import evaluation_score_serialize
from myapp.models import evaluation_score
class evaluation_score_Viewset(viewsets.ModelViewSet):
    queryset = evaluation_score.objects.all()
    serializer_class = evaluation_score_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('score','kind_of_evaluation','criteria','id')


from myapp.serializer import evaluation_sheet_serialize
from myapp.models import evaluation_sheet
class evaluation_sheet_Viewset(viewsets.ModelViewSet):
    queryset = evaluation_sheet.objects.all()
    serializer_class = evaluation_sheet_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('score','kind_of_evaluation','id')


from myapp.serializer import criteria_serialize
from myapp.models import criteria
class criteria_Viewset(viewsets.ModelViewSet):
    queryset = criteria.objects.all()
    serializer_class = criteria_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('score','kind_of_evaluation','criteria','description','id')



from myapp.serializer import evaluation_period_serialize
from myapp.models import tbl_jobtstatus
class Evaluation_period_Viewset(viewsets.ModelViewSet):
    queryset = tbl_jobtstatus.objects.all()
    serializer_class = evaluation_period_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('for_employee_status','id')


from myapp.serializer import evaluation_period_headername_serialize
from myapp.models import evaluation_period_headername
class Evaluation_period_headername_Viewset(viewsets.ModelViewSet):
    queryset = evaluation_period_headername.objects.all()
    serializer_class = evaluation_period_headername_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('header_content','id',)


# use get ====================================

from myapp.serializer import Get_evaluation_period_headername_serialize
from myapp.models import evaluation_period_headername
class get_Evaluation_period_headername_Viewset(viewsets.ModelViewSet):
    queryset = evaluation_period_headername.objects.all()
    serializer_class = Get_evaluation_period_headername_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('for_employee_status__for_employee_status','header_content','id',)

from myapp.serializer import Get_criteria_serialize
from myapp.models import criteria
class Get_criteria_Viewset(viewsets.ModelViewSet):
    queryset = criteria.objects.all()
    serializer_class = Get_criteria_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('kind_of_evaluation__kind_of_evaluation','criteria','description','id')



from myapp.serializer import Get_evaluation_score_serialize
from myapp.models import evaluation_score
class Get_evaluation_score_Viewset(viewsets.ModelViewSet):
    queryset = evaluation_score.objects.all()
    serializer_class = Get_evaluation_score_serialize
    filter_backends = (filters.SearchFilter,)
    search_fields = ('score','kind_of_evaluation__kind_of_evaluation','employee__EmpCode','id')




from myapp.serializer import Get_ViolationsSerializers
from myapp.models import violations
class  Get_ViolationsViewset(viewsets.ModelViewSet):
    queryset =violations.objects.all()
    serializer_class = Get_ViolationsSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('NatureofOffense','graveofminor','id') 


from myapp.serializer import  GET_Violation_Department_PercriteriaSerializers
from myapp.models import violation_department_percriteria
class  GET_Violation_Department_PercriteriaViewset(viewsets.ModelViewSet):
    queryset = violation_department_percriteria.objects.all()
    serializer_class = GET_Violation_Department_PercriteriaSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('kind_of_evaluation__kind_of_evaluation','id')  



from myapp.serializer import Get_LocationSerializers
from myapp.models import place_of_assignment_location
class GET_LocationViewset(viewsets.ModelViewSet):
    queryset =  place_of_assignment_location.objects.all()
    serializer_class = Get_LocationSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('location','id')
    


from myapp.serializer import Get_ProfileSerializers
from myapp.models import profile
class Get_ProfileViewset(viewsets.ModelViewSet):
    queryset =  profile.objects.all()
    serializer_class = Get_ProfileSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')



from myapp.serializer import  Get_Employee_201_DocumentSerializers
from myapp.models import employee_201_document
class  Get_Employee_201_DocumentViewset(viewsets.ModelViewSet):
    queryset =  employee_201_document.objects.all()
    serializer_class = Get_Employee_201_DocumentSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')


from myapp.serializer import  GET_JOBSTATUS_USESerializers
from myapp.models import  evaluationsheetuse
class  GET_JOBSTATUS_USEViewset(viewsets.ModelViewSet):
    queryset =  evaluationsheetuse.objects.all()
    serializer_class = GET_JOBSTATUS_USESerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('jobtstatus__jobtstatus','id')


from myapp.serializer import  GET_PER_MONTHSerializers
from myapp.models import  tbl_evaluation_period_per_month
class  GET_PER_MONTHViewset(viewsets.ModelViewSet):
    queryset =  tbl_evaluation_period_per_month.objects.all()
    serializer_class = GET_PER_MONTHSerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')




from myapp.serializer import  GET_EVALUATION_COPY_HR_Serializers
from myapp.models import  evaluationresult_hr_copy

class  GET_EVALUATION_HR_COPY_Viewset(viewsets.ModelViewSet):
    queryset =  evaluationresult_hr_copy.objects.all()
    serializer_class =  GET_EVALUATION_COPY_HR_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id','readyfordeliberation',)


from myapp.serializer import  GET_PER_CRITERIASerializers
from myapp.models import  tbl_period_of_evaluation_per_criteria
class GET_PER_CRITERIAViewset(viewsets.ModelViewSet):
    queryset =  tbl_period_of_evaluation_per_criteria.objects.all()
    serializer_class =  GET_PER_CRITERIASerializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id')

from myapp.serializer import  GET_PARTICIPANTS_VOTE_Serializers
from myapp.models import   partipantsvote

class  GET_PARTICIPANTS_VOTE_Viewset(viewsets.ModelViewSet):
    queryset =   partipantsvote.objects.all()
    serializer_class =  GET_PARTICIPANTS_VOTE_Serializers
    filter_backends = (filters.SearchFilter,)
    search_fields = ('empcode','id',)


#which department use ths kind of evaluation
from myapp.serializer import GET_WHICH_DEPARTMENT_USE_Serializers
from myapp.models import  whichdepartment

class  GET_WhichDepartment_Use_Kind_of_EvaluationViewset(viewsets.ModelViewSet):
    queryset =  whichdepartment.objects.all()
    serializer_class =  GET_WHICH_DEPARTMENT_USE_Serializers
    

from myapp.serializer import GET_JobDescription_Serializers
from myapp.models import  JobDescription
class GET_JobDescription_Viewsets(viewsets.ModelViewSet):
    queryset =  JobDescription.objects.all()
    serializer_class = GET_JobDescription_Serializers


from myapp.serializer import GET_UploadProof_Serializers
from myapp.models import UploadProof
class GET_UploadProof_Viewsets(viewsets.ModelViewSet):
    queryset =  UploadProof.objects.all()
    serializer_class = GET_UploadProof_Serializers



from myapp.serializer import GET_Busses_Serializers
from myapp.models import  Busses
class GET_Busses_Viewsets(viewsets.ModelViewSet):
    queryset =  Busses.objects.all()
    serializer_class = GET_Busses_Serializers