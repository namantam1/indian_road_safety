import uuid
import string
import random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# PROJECT_WORKED_CHOICE = [
#     ('irsc','IRSC'),
#     ('intellify','Intellify'),
#     ('isafe','iSAFE Assisst'),
#     ('solve','Solve(Multiple Projects)'),
# ]
# PROFILE_CHOICE = [
#     ('FR', 'Freshman'),
#     ('SO', 'Sophomore'),
#     ('JR', 'Junior'),
#     ('SR', 'Senior'),
#     ('GR', 'Graduate'),
# ]
# TYPE_OF_INTERNSHIP = [
#     ('wfh', 'work from home'),
#     ('wfo', 'wrok from office')
# ]

# STATUS = [
#     ('V', 'Volunteer'),
#     ('I', 'Intern')
# ]
# TENURE_CHOICE = [(f'{i} Month', f'{i} month') for i in range(1,13)]
class ProjectWorkedChoice(models.Model):
    project_worked = models.CharField(max_length=225)

    def __str__(self):
        return "{}".format(self.project_worked)

class ProfileChoice(models.Model):
    profile = models.CharField(max_length=225)

    def __str__(self):
        return "{}".format(self.profile)

class StatusChoice(models.Model):
    status = models.CharField(max_length=225)

    def __str__(self):
        return "{}".format(self.status)

class TypeOfInternChoice(models.Model):
    type_of_intern = models.CharField(max_length=225)

    def __str__(self):
        return "{}".format(self.type_of_intern)

class TenureChoice(models.Model):
    tenure = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.tenure)

class Registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=225,editable=False,unique=True)

    def save(self, *args, **kwargs):
        self.registration_number = "".join(random.choices(string.digits,k=8))
        super(Registration, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(),self.registration_number)

class Certificate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    certificate_number = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    certificate_pdf = models.FileField(upload_to='certificates/pdf',default='default.pdf')
    certificate_png = models.FileField(upload_to='certificates/png',default='default.png')

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(),self.certificate_number)


REPORT_STATUS = [
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('R', 'Rejected')
]

class PersonalDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ph_contact_no = models.CharField(max_length=15)
    whatsapp_no = models.CharField(max_length=15)
    project = models.ForeignKey(ProjectWorkedChoice,on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileChoice,on_delete=models.CASCADE)
    type_of_internship = models.ForeignKey(TypeOfInternChoice,on_delete=models.CASCADE)
    joining_date = models.DateField(auto_now_add=True)
    pan_number = models.CharField(max_length=20)
    aadhaar = models.CharField(max_length=20)
    emergency_contact_no = models.CharField(max_length=15)
    bank_account_no = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=15)
    dob = models.DateField()
    permanent_address = models.TextField()
    current_address = models.TextField()
    biometric_id_number = models.CharField(max_length=225)
    internship_tenure = models.ForeignKey(TenureChoice,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume')

    def __str__(self):
        return "{}".format(self.user.get_full_name())

class Project(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileChoice,on_delete=models.CASCADE)
    project_worked_on = models.ForeignKey(ProjectWorkedChoice,on_delete=models.CASCADE)
    status = models.ForeignKey(StatusChoice,on_delete=models.CASCADE)
    tenure = models.ForeignKey(TenureChoice,on_delete=models.CASCADE)
    joining_date = models.DateField()
    end_date = models.DateField()
    upload_traker_link = models.URLField()
    mentor_or_leader = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.user.first_name,self.project_worked_on)


class Report(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=500)
    upload_report = models.FileField(upload_to='reports')
    status = models.CharField(choices=REPORT_STATUS, max_length=2,default='P')

    def __str__(self):
        return "{} - Project: {}, status: {}".format(self.user.first_name,self.project_name,self.status)
