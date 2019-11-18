"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
#urls.py
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers




router = routers.DefaultRouter()



from myapp.viewsets import UserLevelEachEmployee_Viewset
router.register(r'UserLevelEachEmployee',UserLevelEachEmployee_Viewset)


from myapp.viewsets import UploadProof_Viewsets,GET_UploadProof_Viewsets
router.register(r'UploadProof',UploadProof_Viewsets)
router.register(r'GET_UploadProof',GET_UploadProof_Viewsets)

from myapp.viewsets import PlaceOfAssignmentQRCode_Viewsets
router.register(r'QRCodePlaceOfAssingment',PlaceOfAssignmentQRCode_Viewsets)


from myapp.viewsets import  BusQRCode_Viewsets
router.register(r'QRBusses',BusQRCode_Viewsets)

from myapp.viewsets import  BusCategory_Viewsets
router.register(r'BusCategory',BusCategory_Viewsets)

from myapp.viewsets import   Busses_Viewsets
router.register(r'Busses',Busses_Viewsets)

from myapp.viewsets import   GET_Busses_Viewsets
router.register(r'GET_Busses',GET_Busses_Viewsets)


from myapp.viewsets import  JobDescription_Viewsets,GET_JobDescription_Viewsets
router.register(r'POST_JobDescription',JobDescription_Viewsets)
router.register(r'GET_JobDescription',GET_JobDescription_Viewsets)

from myapp.viewsets import  EmployeeQRCode_Viewsets
router.register(r'EmployeeQRCode',EmployeeQRCode_Viewsets)


from myapp.viewsets import  ConcernCategory_Viewsets
router.register(r'CategoryConcern', ConcernCategory_Viewsets)
from myapp.viewsets import  CustomerConcern_Viewsets
router.register(r'POST_CustomerConcern', CustomerConcern_Viewsets)
from myapp.viewsets import GET_CustomerConcern_Viewsets
router.register(r'GET_CustomerConcern', GET_CustomerConcern_Viewsets)





# EvaluationScore





from myapp.viewsets import  EvaluationScoreViewsets,SystemUser_Viewset
router.register(r'EvaluationScore', EvaluationScoreViewsets)




router.register(r'SystemUser',SystemUser_Viewset)

from myapp.viewsets import ACCESSLEVEL_Viewset
router.register(r'AccessLevel',ACCESSLEVEL_Viewset)


from myapp.viewsets import WhichDepartment_Use_Kind_of_EvaluationViewset,GET_WhichDepartment_Use_Kind_of_EvaluationViewset
router.register(r'GET_DEPARTMENT_USE_THE_EVALUATION_SHEET',GET_WhichDepartment_Use_Kind_of_EvaluationViewset)
router.register(r'POST_DEPARTMENT_USE_THE_EVALUATION_SHEET',WhichDepartment_Use_Kind_of_EvaluationViewset)

from myapp.viewsets import EVALUATION_HR_COPY_Viewset,PARTICIPANTS_VOTE_Viewset,BOOT_CHATS_Viewset,GET_EVALUATION_HR_COPY_Viewset,GET_PARTICIPANTS_VOTE_Viewset
router.register(r'GET_HR_COPY_EVALUATION_RESULT',GET_EVALUATION_HR_COPY_Viewset)

router.register(r'HR_COPY_EVALUATION_RESULT',EVALUATION_HR_COPY_Viewset)
router.register(r'PARTICIPANTS_VOTE',PARTICIPANTS_VOTE_Viewset)
router.register(r'GET_PARTICIPANTS_VOTE',GET_PARTICIPANTS_VOTE_Viewset)
router.register(r'CHAT_BOOTS_FOR_DELIBERATION',BOOT_CHATS_Viewset)

from myapp.viewsets import EVALUATION_PERIODViewset,PER_MONTHViewset,PER_CRITERIAViewset,GET_PER_MONTHViewset,GET_PER_CRITERIAViewset
router.register(r'POST_EVALUATION_PERIOD',EVALUATION_PERIODViewset)
router.register(r'POST_PER_MONTH',PER_MONTHViewset)
router.register(r'GET_PER_MONTH',GET_PER_MONTHViewset)
router.register(r'POST_PER_CRITERIA',PER_CRITERIAViewset)

router.register(r'POST_PER_CRITERIA',PER_CRITERIAViewset)
router.register(r'GET_PER_CRITERIA',GET_PER_CRITERIAViewset)


from myapp.viewsets import  Employee_201_Viewset,Employee_201_DocumentViewset
from myapp.viewsets import  JOBSTATUS_USEViewset,GET_JOBSTATUS_USEViewset

router.register(r'POST_EVALUATION_SHEET_USED_BY_JOBSTATUS',JOBSTATUS_USEViewset)
router.register(r'GET_EVALUATION_SHEET_USED_BY_JOBSTATUS',GET_JOBSTATUS_USEViewset)




router.register(r'DOCUMENT_201_COLUMN',Employee_201_Viewset)
router.register(r'DOCUMENT_201_CONTENT',Employee_201_DocumentViewset)
from myapp.viewsets import  Get_Employee_201_DocumentViewset
router.register(r'GET_DOCUMENT_201_CONTENT',Get_Employee_201_DocumentViewset)

from myapp.viewsets import Passing_GradeViewset
router.register(r'PassingGrade',Passing_GradeViewset)


from myapp.viewsets import JobLevelViewset
router.register(r'JOBLEVEL',JobLevelViewset)

from myapp.viewsets import CategoryViewset
router.register(r'PLACE_OF_ASSIGNMENT_CATEGORY',CategoryViewset)

from myapp.viewsets import ProfileViewset
router.register(r'POST_PROFILE',ProfileViewset)



from myapp.viewsets import Get_ProfileViewset
router.register(r'GET_PROFILE',Get_ProfileViewset)



from myapp.viewsets import EmployeeViewset
from myapp.viewsets import UserViewset
router.register(r'User',UserViewset)

from myapp.viewsets import GET_LocationViewset
router.register(r'GET_PLACE_OF_ASSIGNMENT_LOCATION',GET_LocationViewset)


from myapp.viewsets import LocationViewset
router.register(r'POST_PLACE_OF_ASSIGNMENT_LOCATION',LocationViewset)

from myapp.viewsets import DepartmentViewset,Minor_GraveViewset
from myapp.viewsets import ViolationsViewset,Violation_Department_PercriteriaViewset
router.register(r'DEPARTMENT',DepartmentViewset)
router.register(r'MINOR_OR_GRAVE',Minor_GraveViewset)
router.register(r'POST_Violation_Per_Department_Per_Criteria',Violation_Department_PercriteriaViewset)
from myapp.viewsets import GET_Violation_Department_PercriteriaViewset
router.register(r'GET_Violation_Per_Department_Per_Criteria',GET_Violation_Department_PercriteriaViewset)
router.register(r'POST_VIOLATIONS',ViolationsViewset)
from myapp.viewsets import Get_ViolationsViewset
router.register(r'Get_VIOLATIONS',Get_ViolationsViewset)

router.register(r'Employee',EmployeeViewset)
from myapp.viewsets import TvrViewset,TimeKeepingViewset,DispatchViewset
router.register(r'TVR',TvrViewset)
router.register(r'DISPATCH',DispatchViewset)
router.register(r'TIMEKEEPING',TimeKeepingViewset)







from myapp.viewsets import evaluation_sheet_Viewset
router.register(r'EvaluationSheet_Kind',evaluation_sheet_Viewset)
from myapp.viewsets import criteria_Viewset
router.register(r'POST_EvaluationSheet_Criteria',criteria_Viewset)


from myapp.viewsets import evaluation_score_Viewset
router.register(r'POST_EvaluationScore',evaluation_score_Viewset)



from myapp.viewsets import Evaluation_period_Viewset, Evaluation_period_headername_Viewset
router.register(r'JOBSTATUS',Evaluation_period_Viewset)
router.register(r'Evaluation_content',Evaluation_period_headername_Viewset)


# use get ===============================================
from myapp.viewsets import get_Evaluation_period_headername_Viewset
router_get = routers.DefaultRouter()
router_get.register(r'Get_Evaluation_content',get_Evaluation_period_headername_Viewset)
from myapp.viewsets import Get_criteria_Viewset,Get_evaluation_score_Viewset

router_get.register(r'Get_EvaluationSheet_Criteria',Get_criteria_Viewset)
router_get.register(r'GET_EvaluationScore',Get_evaluation_score_Viewset)
# http://127.0.0.1:8000/api/EvaluationSheet_Criteria/ POST METHOD






from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/get/', include(router_get.urls)),
   
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













   




