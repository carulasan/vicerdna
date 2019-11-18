from django.urls import path

from . import views

urlpatterns = [
    path('login_user/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('', views.index, name='loading_panel'),
    path('login/', views.login_credential, name='login_panel'),
    path('viewme/', views.viewme, name='test'),
    path('createaccount/',views.createaccount,name='user_createaccount'),
    path('qrcode/',views.qrcode_generate,name='qr'),
    path('qrcode_general/',views.qrcode_generate_general,name='qrcode'),
    path('Employee/',views.employee_module,name='employee_panel'),
    path('Employee/<int:id>',views.employee_information,name='employee_information'),
    path('Performance/Evaluation',views.performance_evaluation,name='performance_evaluation_panel'),
    path('Deliberation/', views.deliberation, name='deliberation_panel'),
    path('Dashboard/', views.dashboard, name='dashboard_panel'),
    path('Settings/', views.settings, name='settings_panel'),
    path('Settings/General/', views.settings_general, name='settings_general_panel'),
    path('Settings/Evaluation_Sheet/', views.settings_evaluation_sheet, name='settings_evaluation_sheet_panel'),
    path('Settings/violations/', views.settings_violations, name='settings_violation_panel'),
    path('Settings/Department/', views.settings_department, name='settings_department_panel'),
    path('Settings/Evalution_Guide/', views.settings_evaluation_guide, name='settings_evaluation_guide_panel'),
    path('Settings/Place_of_Assignment/', views.settings_place_of_assignment, name='settings_place_of_assignment_panel'),
    path('Settings/Accounts/', views.settings_accounts, name='settings_accounts_panel'),
    path('Settings/JobLevel/', views.settings_joblevel, name='settings_joblevel_panel'),
    path('Evaluation/Report/', views.report, name='report_panel'),
    path('Employee/show_201File/<str:empcode>/', views.show201file, name='201File'),
    path('Concern/', views.concern, name='concern'),
    path('JobDescription/', views.JobDescription, name='JobDescription'),
    path('Busses/', views.busses, name='Busses'),
    path('PasengerConcern/Bus/', views.Bus_qrcode_generate, name='BussesConcern'),
    path('CustomerConcern/Bus/<int:id>/', views.CustomerConcern, name='CustomerConcern'),
    path('PasengerConcern/PlaceofAssignments/', views.Place_qrcode_generate, name='Place_qrcode_generate'),
    path('CustomerConcern/ByPlaceOfAssignment/<int:id>/', views.CustomerConcernTerminalsOffice, name='CustomerConcernTerminalsOffice'),

    path('FileMaintenance/Concern/', views.ConcernTopic, name='ConcernTopic'),
    path('EmployeePerformance/', views.EmployeePerformance, name='EmployeePerformance'),
    path('ChangePassword/', views.updatePasswordAdmin, name='ChangePassword'),
    path('sendemail/', views.send_email, name='sendemail'),
    path('sendemail/issue/resolved/', views.send_email_issue_resolved, name='sendemailresponse'),
    
    
        
]
