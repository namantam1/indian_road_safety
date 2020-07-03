from django.shortcuts import render,redirect,HttpResponse,Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import Registration,Project,Certificate
from datetime import datetime,timedelta
from django.conf import settings
import os
from django.core.files import File
from django.template.loader import render_to_string
from .certificate import generate_certificate
from django.http import JsonResponse

# configuration for User model
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


@login_required
def adminpage(request):
    if request.user.is_staff:
        get = request.GET.get
        if(get('reg_number')):
            user = User.objects.filter(registration__registration_number=get('reg_number').strip())
        elif(get('first_name')):
            user = User.objects.filter(first_name__iexact=get('first_name').strip())
        elif(get('last_name')):
            user = User.objects.filter(last_name__iexact=get('last_name').strip())
        elif(get('days_from_now')):
            days = int(get('days_from_now').strip())
            user = User.objects.filter(project__end_date__gte=datetime.now(),project__end_date__lt=datetime.now()+timedelta(days=days))
        else:
            user = None
        return render(request,'certificate_app/adminpage.html',{'user':user})
    raise PermissionDenied()

def intern_detail(request,pk):
    intern = User.objects.get(id=pk)
    if hasattr(intern,'project'):
        project = intern.project
    else:
        project = None
    if hasattr(intern,'report'):
        report = intern.report
    else:
        report = None
    if hasattr(intern,'personaldetail'):
        details = intern.personaldetail
    else:
        details = None
    
    context = {
        'user':intern,
        'project':project,
        'report':report,
        'details':details
    }
    data = render_to_string('certificate_app/interndetail.html',context=context)
    return JsonResponse(data,safe=False)
    # return render(request,'certificate_app/interndetail.html',context=context)

def create_certificate(request,pk):
    intern = User.objects.get(id=pk)
    if not hasattr(intern,'certificate') and hasattr(intern,'report'):
        c = Certificate(user = intern)

        filepath = os.path.join(settings.BASE_DIR,'certificate_file')
        savepath = os.path.join(settings.MEDIA_ROOT,'certificates')
        name = intern.get_full_name()
        intertype = intern.personaldetail.type_of_internship
        profile = intern.personaldetail.profile
        start_date = intern.project.joining_date
        end_date = intern.project.end_date
        logo = intern.personaldetail.project
        print(logo)
        logo = 'logo'
        renumber = intern.registration.registration_number

        png,pdf = generate_certificate(filepath,name,intertype,profile,start_date,end_date,logo,renumber,savepath)

        c.certificate_pdf.save(f'certificate_{renumber}.pdf',File(open(pdf,'rb')),save=False)
        c.certificate_png.save(f'certificate_{renumber}.png',File(open(png,'rb')),save=True)
        os.remove(png)
        os.remove(pdf)
        # return HttpResponse(f'<div>certificate created successfully with cf no - <a href="{c.certificate_pdf.url}" >{c.certificate_pdf}</a></div>')
        data = {
            'pdfurl':c.certificate_pdf.url,
            'pngurl':c.certificate_png.url
        }
        return JsonResponse(data)
    else:
        raise Http404('either report not made or certificate already created')

@login_required
def change_status(request,pk):
    if request.user.is_staff:
        value = request.GET.get('status')
        url = request.GET.get('next')
        report = User.objects.get(id=pk).report
        report.status = value
        report.save()
        return JsonResponse('status changed successfully')
        # if url:
        #     return redirect(url)
        # return redirect('interndetail',pk=pk)
    raise PermissionDenied