from django.shortcuts import render,redirect,HttpResponse,Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .models import Registration,User,Project,Certificate
from datetime import datetime,timedelta
from django.conf import settings
import os
from django.contrib.sites.shortcuts import get_current_site
from PIL import Image,ImageDraw,ImageFont

def make_certificate(renumber,name,cnumber,domain):
    name = name
    cerficate_no = f'certificate no. - {cnumber}'
    url = f'{domain}/certificates/{cnumber}'
    url_name = 'url - ' + url
    registration_no = f'{renumber}'

    path = os.path.join(settings.BASE_DIR,'media/certificates')
    im = Image.open(path+'/certificate.jpg','r')
    d = ImageDraw.Draw(im)
    location = (603,600)
    location1 = (231,1380)
    location2 = (231,1427)
    text_color = (0,137,209)
    font = ImageFont.truetype("arial.ttf",72)
    font1 = ImageFont.truetype("arial.ttf",20)
    font2 = ImageFont.truetype("arial.ttf",20)
    d.text(location,name,fill=text_color,font=font)
    d.text(location1,cerficate_no,fill=text_color,font=font1)
    d.text(location2,url_name,fill=text_color,font=font2)
    im.save(f'{path}/certificate_'+registration_no+'.pdf')

    return url

@login_required
def adminpage(request):
    if request.user.is_staff:
        get = request.GET.get
        if(get('reg_number')):
            # user = Registration.objects.filter(registration_number=get('reg_number'))[0].user
            user = User.objects.filter(registration__registration_number=get('reg_number').strip())
            print(get('reg_number'),user)
        elif(get('first_name')):
            user = User.objects.filter(first_name__iexact=get('first_name').strip())
        elif(get('last_name')):
            user = User.objects.filter(last_name__iexact=get('last_name').strip())
        elif(get('days_from_now')):
            days = int(get('days_from_now').strip())
            # project = Project.objects.filter(end_date__lt=datetime.now()+timedelta(days=days)\
            #     ,end_date__gte=datetime.now())
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
    print(request.META.get('HTTP_REFERER'))
    return render(request,'certificate_app/interndetail.html',context=context)

def create_certificate(request,pk):
    intern = User.objects.get(id=pk)
    if not hasattr(intern,'certificate') and hasattr(intern,'report'):
        # c = Certificate.objects.create(user=intern)
        c = Certificate(user = intern)

        renumber = intern.registration.registration_number
        name = intern.get_full_name()
        cnumber = c.certificate_number
        domain = get_current_site(request)

        url = make_certificate(renumber,name,cnumber,domain)
        c.certificate_url = url
        c.save()
        return HttpResponse(f'<div>certificate created successfully with cf no - <a href="{url}" >{cnumber}</a></div>')
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
        if url:
            return redirect(url)
        return redirect('interndetail',pk=pk)
    raise PermissionDenied