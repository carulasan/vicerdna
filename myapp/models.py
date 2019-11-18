from django.db import models
from django.contrib.auth.models import User
# # Create your models here.


# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )


# class UserManager(BaseUserManager):
#     def create_user(self, username, password):
#         """
#         Creates and saves a User with the given username and password.
#         """ 
        

#         user = self.model(
#             username=username,
#             password=password,
#         )

#         user.first_time_login = True
#         user.save(using=self._db)
#         return uservr
        
#     def create_staffuser(self, username, password):
#         """
#         Creates and saves a staff user with the given username and password.
#         """
#         user = self.create_user(
#             username=username,
#             password=password,
#         )
#         user.first_time_login = True
#         user.staff = True
#         user.save(using=self._db)
#         return user

    

#     def create_superuser(self, username, password):
#         """
#         Creates and saves a superuser with the given username and password.
#         """
#         user = self.create_user(
#             username=username,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.first_time_login = True
#         user.save(using=self._db)
#         return user

#     def create_employee(self, username,password,empcode):
#         """
#         Creates and saves a staff user with the given username and password.
#         """
#         user = self.create_user(
#             username=username,
#             password=password,
#         )
#         user.staff= False
#         user.admin= False
#         user.first_time_login = True
#         user.save(using=self._db)
#         return user

    

   
   


# class User(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True,verbose_name='username')    
#     admin = models.BooleanField(default=False) # a superuser hr
#     staff = models.BooleanField(default=False)
#     active = models.BooleanField(default=True)
#     first_time_login = models.BooleanField(default=True)
   

#     def __str__(self):
#         return f'{self.id}'

   
#     # notice the absence of a "Password field", that's built in.
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = [] # username & Password are required by default.



#     objects = UserManager()

   
#     def __str__(self):              # __unicode__ on Python 2
#         return self.username

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#     def has_perms(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

    

#     @property
#     def is_admin(self):
#         "Is the user a admin member?"
#         return self.admin

#     @property
#     def is_staff(self):
#         "Is the user a staff member?"
#         return self.staff

#     @property
#     def is_active(self):
#         "Is the user active?"
#         return self.active


#     def __str__(self):
#         return self.username

class SystemUserInformation(models.Model):
    account = models.OneToOneField(User,on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255,null=True)
    Email = models.EmailField(null=True)
    AccessLevel = models.CharField(null=True,max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.FullName}'


class AccessLevel(models.Model):
    NameofUserLevel = models.CharField(max_length=255,null=True)
    ReportsModule = models.BooleanField(default=False)
    PerformanceEvaluationModule = models.BooleanField(default=False)
    DeliberationModule = models.BooleanField(default=False)
    SystemDashboardModule =models.BooleanField(default=False)
    FileMaintenanceModule = models.BooleanField(default=False)
    FileMaintenance_General = models.BooleanField(default=False)
    FileMaintenance_Accounts = models.BooleanField(default=False)
    FileMaintenance_EvaluationSheet = models.BooleanField(default=False)
    FileMaintenance_Departments = models.BooleanField(default=False)
    FileMaintenance_Offense = models.BooleanField(default=False)
    FileMaintenance_EvaluationGuide = models.BooleanField(default=False)
    FileMaintenance_PlaceofAssignment = models.BooleanField(default=False)
    FileMaintenance_JobLevelorAccessLevel = models.BooleanField(default=False)
    FileMaintenance_201File = models.BooleanField(default=False)
    CustomerConcern = models.BooleanField(default=False)
    EmployeePerformance = models.BooleanField(default=False)
    Is_CallCenter = models.BooleanField(default=False)
    Is_CustomerService =  models.BooleanField(default=False)
    Is_LegalDepartment = models.BooleanField(default=False)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.NameofUserLevel}'


class employee_201_document(models.Model):
    category = models.ForeignKey('employee_201_file',on_delete = models.CASCADE)
    empcode = models.CharField(max_length=255,null=True)
    classification =  models.CharField(max_length=255,null=True)
    Description = models.CharField(max_length=255,null=True)
    files =  models.FileField(upload_to='media/') 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.category}'

class employee_201_file(models.Model):
    category =models.CharField(max_length=255) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.category}'


class profile(models.Model):
    account = models.OneToOneField(User,on_delete=models.CASCADE)
    empcode=models.CharField(max_length=255)
    markasread = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.account}'

class tbl_employee(models.Model): #gagawn ko pa ng table contract
    EmpCode = models.CharField(max_length=30)
    JobStatus =  models.CharField(max_length=30)
    LastName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    Suffix     = models.CharField(max_length=50,null=True)
    NickName = models.CharField(max_length=50,null=True)
    JobLevel = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Designation = models.CharField(max_length=50)
    PlaceOfAssignment = models.CharField(max_length=50)
    ContactNumber = models.CharField(max_length=15)
    Email= models.EmailField(null=True)
    datehired = models.DateField()
    #user account to be follow / create new tbloe 
    
   
    
    def __str__(self):
        return f'{self.EmpCode}'


class joblevel(models.Model):
    joblevel = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
      
    def __str__(self):
        return f'{self.joblevel}'
    

    
   
class time_keeping(models.Model):
    EmpCode = models.CharField(max_length=30)
    Name = models.CharField(max_length=255)
    DateIn = models.DateField()
    TimeIn = models.CharField(max_length=50)
    DateOut = models.DateField()
    TimeOut = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Position = models.CharField(max_length=50,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'Attendance :{self.EmpCode} {Name}'
    
    



class tvr(models.Model):
    EmpCode = models.CharField(max_length=30)
    CaseNO = models.CharField(max_length=255)
    IncidentDate = models.DateField()
    Type = models.CharField(max_length=50)
    NatureofOffense = models.CharField(max_length=255)
    Decision  = models.CharField(max_length=255,null=True)
    DateofDecision = models.CharField(max_length=255,null=True)
    ReportedBy=  models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'EmpCode {self.EmpCode}'

    # Code = models.CharField(max_length=255,null=True)
    # startdate = models.DateField()
    # Numberofdayssched = models.IntegerField(blank=True, null=True)
    # enddate = models.DateField()
    # Numberofdays = models.IntegerField(blank=True, null=True)
    # Name = models.CharField(max_length=255,null=True)
    # Position = models.CharField(max_length=255,null=True)
    # Type = models.CharField(max_length=50,null=True)
    # NatureofOffense = models.CharField(max_length=255,null=True)
    # MemoDate = models.DateField()
    # BEGINNINGBALANCEofSuspnDays = models.IntegerField(blank=True, null=True)
    # REMAININGSuspnDays = models.IntegerField(blank=True, null=True)
    # Issuedby = models.CharField(max_length=255,null=True)
    # DateSignedRcvd = models.CharField(max_length=255,null=True)
    # Penalty = models.CharField(max_length=255,null=True)
    # PrevIssued = models.CharField(max_length=255,null=True) 
    # WithClearance = models.CharField(max_length=255,null=True)
    
    


class dispatch(models.Model):
    EmpCode = models.CharField(max_length=30,null=True)
    FullName = models.CharField(max_length=255,null=True)
    EmpPosition = models.CharField(max_length=255,null=True)
    Location = models.CharField(max_length=255,null=True)
    Active =  models.BooleanField(default=False)
    DepartureTime = models.CharField(max_length=255,null=True)
    ArrivalTime = models.CharField(max_length=255,null=True)
    KMRun = models.CharField(max_length=255,null=True)
    Busno = models.CharField(max_length=255,null=True)
    Route = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
       
    #note pwede umulit kasi yung pabalik tapos yung system magbilangkung ilang balik
    
    def __str__(self):
        return f' {self.DepartureTime}'
    






    
  

class evaluationsheetuse(models.Model):
    kind_of_evaluation = models.ForeignKey('evaluation_sheet',on_delete = models.CASCADE)
    jobtstatus = models.ForeignKey('tbl_jobtstatus',on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.tbl_jobtstatus}'

class whichdepartment(models.Model):
    kind_of_evaluation = models.ForeignKey('evaluation_sheet',on_delete = models.CASCADE)
    department = models.ForeignKey('department',on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
class evaluation_sheet(models.Model):
    kind_of_evaluation = models.CharField(max_length=255,null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.kind_of_evaluation}'

class criteria(models.Model):
    kind_of_evaluation = models.ForeignKey('evaluation_sheet',on_delete = models.CASCADE)
    criteria = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    percentage = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.criteria}'


class tbl_jobtstatus(models.Model):
    for_employee_status = models.CharField(max_length=255) #probationary
    month_period = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.for_employee_status}'
    
class evaluation_period_headername(models.Model):
    for_employee_status = models.ForeignKey('tbl_jobtstatus',on_delete = models.CASCADE)
    header_content = models.CharField(max_length=255) #firstmonth
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'for employee status content : {self.header_content}'
    





class evaluation_score(models.Model):
    kind_of_evaluation = models.ForeignKey('evaluation_sheet',on_delete = models.CASCADE)
    criteria = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    percentage = models.IntegerField(blank=True, null=True) 
    employee = models.ForeignKey('tbl_employee',on_delete = models.CASCADE)
    score = models.FloatField(blank=True,null=True)
    monthname = models.CharField(max_length=255,null=True)
    identifier = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.score}'


class passing_grade(models.Model):
    passing_grades = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.passing_grades}'


#9/10/2019
class department(models.Model):
    department = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.department}'

class minor_grave(models.Model):
    typeofviolation = models.CharField(max_length=255,null=True)
    percentage = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
      
    def __str__(self):
        return f'{self.typeofviolation}'
  


class violations(models.Model):
    NatureofOffense = models.CharField(max_length=255,null=True)
    graveofminor = models.ForeignKey('minor_grave',on_delete = models.CASCADE) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.NatureofOffense}'


class violation_department_percriteria(models.Model):
    kind_of_evaluation = models.ForeignKey('evaluation_sheet',on_delete = models.CASCADE)
    department = models.ForeignKey('department',on_delete = models.CASCADE)
    criteria = models.ForeignKey('criteria',on_delete = models.CASCADE)
    offense = models.ForeignKey('violations',on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.score}'


class place_of_assignment_category(models.Model):
    category = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.category}'


class place_of_assignment_location(models.Model):
    location = models.CharField(max_length=255)
    category = models.ForeignKey('place_of_assignment_category',on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.location}'


class tbl_evaluation_period(models.Model):
    empcode = models.CharField(max_length=50)
    employeefullname = models.CharField(max_length=255)
    datehired = models.DateField()
    designation = models.CharField(max_length=50,null=True)
    departmentsection = models.CharField(max_length=50,null=True)
    placeofassignment = models.CharField(max_length=50,null=True)
    supervisorrater = models.CharField(max_length=255,null=True)
    evaluation_period = models.CharField(max_length=50)#1 2 3 4
    length_period = models.IntegerField() #5
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}'

class EvaluationScore(models.Model):
    evaluation_period = models.ForeignKey('tbl_evaluation_period',on_delete = models.CASCADE)
    Criteria = models.CharField(max_length=255,null=True)
    Month = models.CharField(max_length=255,null=True)
    Score = models.CharField(max_length=255,null=True)
    ScoreFinal = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    
    
    def __str__(self):
        return f'{self.Criteria}'

class tbl_evaluation_period_per_month(models.Model):
    evaluation_period = models.ForeignKey('tbl_evaluation_period',on_delete = models.CASCADE) 
    empcode = models.CharField(max_length=50)
    month_name = models.CharField(max_length=50)#first month second monrh
    # score = models.IntegerField(default=0)
    remarks = models.TextField(max_length=1020,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}'


class tbl_period_of_evaluation_per_criteria(models.Model):
    evaluation_period_per_month = models.ForeignKey('tbl_evaluation_period_per_month',on_delete = models.CASCADE)
    empcode = models.CharField(max_length=50)
    criteria = models.CharField(max_length=50)
    score = models.FloatField(null=True)
    remarks = models.TextField(max_length=1020,null=True)
    evaluator = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.evaluation_period_per_month}'




class evaluationresult_hr_copy(models.Model):
    empcode = models.CharField(max_length=50)
    evaluation_sheet = models.ForeignKey('tbl_evaluation_period',on_delete = models.CASCADE)
    employeefullname = models.CharField(max_length=255)
    jobstatus = models.CharField(max_length=50)
    datehired = models.CharField(max_length=50)
    designation = models.CharField(max_length=50,null=True)
    departmentsection = models.CharField(max_length=50,null=True)
    placeofassignment = models.CharField(max_length=50,null=True)
    supervisorrater = models.CharField(max_length=255,null=True)
    send = models.BooleanField(default=False)
    readyfordeliberation = models.BooleanField(default=False)
    delibationisdone = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}'

class partipantsvote(models.Model):
    evaluation_sheet = models.ForeignKey('evaluationresult_hr_copy',on_delete = models.CASCADE)
    participants = models.CharField(max_length=255)
    finaldecision = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.evaluation_sheet}'



class bootchats(models.Model):
    evaluation_sheet = models.CharField(max_length=255,null=True)
    messages = models.TextField(max_length=1024)
    who = models.CharField(max_length=255)
    avatar = models.CharField(max_length=1025,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.who}'


class ConcernCategory(models.Model):
    CategoryName = models.CharField(max_length=255,null=True) #concenrn driver
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.CategoryName}'

# Picture =  models.FileField(upload_to='media/') 
class CustomerConcern(models.Model):
    ConcernType = models.CharField(max_length=50,null=True)#complain complement
    ConcernCategory = models.CharField(max_length=50,null=True)#bus
    ConcernCategoryIDPlace = models.IntegerField(default=0)
    EmpCode = models.CharField(max_length=50,null=True)
    Name = models.CharField(max_length=255,null=True)
    MobileNumber = models.CharField(max_length=15,null=True)
    Email = models.EmailField(null=True)
    Topic = models.CharField(max_length=255,null=True)#about what
    OtherConcern = models.CharField(max_length=255,null=True)#Other concern
    YourConcern = models.TextField(max_length=1020,null=True) #message  
    IsToCallCenter = models.BooleanField(default=False)
    IsToCustomerService = models.BooleanField(default=False)
    IsToLegal = models.BooleanField(default=False)
    IsDone =  models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id}'

class QrCodeType(models.Model):
    Type =  models.CharField(max_length=255,null=True)
    SystenLabel = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.Type}'

class QrCodeGeneral(models.Model):
    QrCodeType = models.ForeignKey('QrCodeType',on_delete = models.CASCADE)#fk
    QrCodeImage = models.CharField(max_length=255,null=True)   #image pathh
    QrcodeUrl = models.CharField(max_length=255,null=True) #info or 127.0.0.0:8000/id
    QrCodeIdettifier = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.QrCodeType}'



    
    

class EmployeeQRCode(models.Model):
    EmpCode = models.CharField(max_length=255,null=True)
    QrCode = models.CharField(max_length=255,null=True)
    Info = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.EmpCode}'
    
    
    
    
class JobDescription(models.Model):
    Department = models.ForeignKey('Department',on_delete = models.CASCADE)
    JobTitle= models.CharField(max_length=255,null=True)
    ReportsTo = models.CharField(max_length=255,null=True)
    Section = models.CharField(max_length=255,null=True)
    Content = models.TextField(max_length=65535,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.JobTitle}'


class Busses(models.Model):
    BusNo = models.CharField(max_length=255,null=True)
    PlaceOfAssignment = models.CharField(max_length=255,null=True)
    Type = models.ForeignKey('BusCategory',on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.BusNo}'

class BusCategory(models.Model):
    BusCategoryName = models.CharField(max_length=255,null=True)
    def __str__(self):
        return f'{self.BusCategoryName}'

class BusQRCode(models.Model):
    BusID = models.CharField(max_length=255,null=True)
    QrCode = models.CharField(max_length=255,null=True)#image
    Info = models.CharField(max_length=255,null=True)#QRinformation
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.BusID}'

class PlaceOfAssignmentQRCode(models.Model):
    LocationID = models.CharField(max_length=255,null=True)
    QrCode = models.CharField(max_length=255,null=True)#image
    Info = models.CharField(max_length=255,null=True)#QRinformation
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.LocationID}'
    
class UploadProof(models.Model):
    CustomerConcernID = models.ForeignKey('CustomerConcern',on_delete = models.CASCADE)
    Proof = models.FileField(upload_to='media/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.CustomerConcernID}'
    
    


    
class UserLevelEachEmployee(models.Model):
    EmpCode = models.CharField(max_length=255,null=True)
    ReportsModule = models.BooleanField(default=False)
    PerformanceEvaluationModule = models.BooleanField(default=False)
    DeliberationModule = models.BooleanField(default=False)
    SystemDashboardModule =models.BooleanField(default=False)
    FileMaintenanceModule = models.BooleanField(default=False)
    FileMaintenance_General = models.BooleanField(default=False)
    FileMaintenance_Accounts = models.BooleanField(default=False)
    FileMaintenance_EvaluationSheet = models.BooleanField(default=False)
    FileMaintenance_Departments = models.BooleanField(default=False)
    FileMaintenance_Offense = models.BooleanField(default=False)
    FileMaintenance_EvaluationGuide = models.BooleanField(default=False)
    FileMaintenance_PlaceofAssignment = models.BooleanField(default=False)
    FileMaintenance_JobLevelorAccessLevel = models.BooleanField(default=False)
    FileMaintenance_201File = models.BooleanField(default=False)
    CustomerConcern = models.BooleanField(default=False)
    EmployeePerformance = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 
    Is_CallCenter = models.BooleanField(default=False)
    Is_CustomerService =  models.BooleanField(default=False)
    Is_LegalDepartment = models.BooleanField(default=False)
    


    
    
    
        
    








    
    
    
    

    
    
    
    
    
    
    




