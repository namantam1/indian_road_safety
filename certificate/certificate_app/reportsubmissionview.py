from django.shortcuts import render,redirect
from .models import Report
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required

# Model will be like for this --------

# class Report(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     project_name = models.CharField(max_length=100)
#     upload_report = models.FileField(upload_to='media/files')
#     status = models.CharField(choices=PROJECT_STATUS, max_length=2,default='P')

#     def __str__(self):
#         return f"{self.user.first_name} - {self.project_name} status: {self.status}"

class ReportSubmissionForm(ModelForm):
    class Meta():
        model = Report
        fields = ['project_name','upload_report']

# @login_required
# def reportsumission(request):
#     if request.method == 'POST':
#         form = ReportSubmissionForm(request.POST,request.FILES)
#         if form.is_valid:
#             form.instance.user = request.user
#             form.save()
#             report = request.user.report.id
#             return redirect('reportview',pk=report)
#         return render(request,'certificate_app/report.html',{'from':form})
#     form = ReportSubmissionForm()
#     # try:
#     #     status = Report.objects.filter(user=request.user)
#     # except:
#     #     status = None
#     return render(request,'certificate_app/report.html',{'form':form})

@login_required
def reportview(request):
    if request.method == 'POST':
        form = ReportSubmissionForm(request.POST,request.FILES)
        if form.is_valid:
            form.instance.user = request.user
            form.save()
            return redirect('reportview')
        return render(request,'certificate_app/reportview.html',{'from':form})
    form = ReportSubmissionForm()
    return render(request,'certificate_app/reportview.html',{'form':form})

@login_required
def reportupdate(request):
    if request.method == 'GET':
        report = request.user.report
        form = ReportSubmissionForm(instance=report)
        return render(request,'certificate_app/report.html',{'form':form})
    elif request.method == 'POST':
        report = request.user.report
        form = ReportSubmissionForm(request.POST,request.FILES,instance=report)
        if form.is_valid():
            form.instance.status = "P"
            form.save()
            return redirect('reportview')
        return render(request,'certificate_app/report.html',{'form':form})

# Query for checking of report exists
# if hasattr(request.user,'report'):
# ...     print(True)