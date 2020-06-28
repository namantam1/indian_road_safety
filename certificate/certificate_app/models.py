import uuid
import string
import random
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegistrationNumber(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=8,editable=False,unique=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.registration_number}"

    def save(self, *args, **kwargs):
        self.registration_number = "".join(random.choices(string.digits,k=8))
        super(RegistrationNumber, self).save(*args, **kwargs)

class Certificate(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration = models.OneToOneField(RegistrationNumber,on_delete=models.CASCADE)
    certificate_number = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

    def __str__(self):
        return f'{self.certificate_number} {self.user.first_name}'


PROJECT_WORKED_CHOICE = [
    ('irsc','IRSC'),
    ('intellify','Intellify'),
    ('isafe','iSAFE Assisst'),
    ('solve','Solve(Multiple Projects)'),
]
PROFILE_CHOICE = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
TYPE_OF_INTERNSHIP = [
    ('wfh', 'work from home'),
    ('wfo', 'wrok from office')
]
TENURE_CHOICE = [(f'{i} Month', f'{i} month') for i in range(1,13)]

class ProfileChoice(models.Model):
    profile = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profile}"

class PersonalDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ph_contact_no = models.CharField(max_length=12)
    whatsapp_no = models.CharField(max_length=12)
    project = models.CharField(max_length=15, choices=PROJECT_WORKED_CHOICE)
    profile = models.ForeignKey(ProfileChoice,on_delete=models.CASCADE)
    type_of_internship = models.CharField(
        max_length=15, choices=TYPE_OF_INTERNSHIP)
    joining_date = models.DateField(auto_now_add=True)
    pan_number = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    emergency_contact_no = models.CharField(max_length=12)
    bank_account_no = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=10)
    dob = models.DateField()
    permanent_address = models.TextField()
    current_address = models.TextField()
    biometric_id_number = models.CharField(max_length=15)
    intership_tenure = models.CharField(max_length=10, choices=TENURE_CHOICE)
    resume = models.FileField(upload_to='media/resume')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


STATUS = [
    ('V', 'Volunteer'),
    ('I', 'Intern')
]

PROJECT_STATUS = [
    ('A', 'Approved'),
    ('P', 'Pending'),
    ('R', 'Rejected')
]


class Project(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(ProfileChoice,on_delete=models.CASCADE)
    project_worked_on = models.CharField(max_length=15,choices=PROJECT_WORKED_CHOICE)
    status = models.CharField(max_length=1, choices=STATUS)
    tenure = models.CharField(max_length=10,choices=TENURE_CHOICE)
    joining_data = models.DateField()
    end_date = models.DateField()
    upload_traker_link = models.URLField()
    mentor_or_leader = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} - {self.project_worked_on}"


class Report(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    upload_report = models.FileField(upload_to='media/files')
    status = models.CharField(choices=PROJECT_STATUS, max_length=2,default='P')

    def __str__(self):
        return f"{self.user.first_name} - {self.project_name} status: {self.status}"
