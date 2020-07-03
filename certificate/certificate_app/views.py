from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.auth import login,authenticate

from .models import Registration
from .forms import UserCreationForm,SignupForm,User,PersonalDetailForm,ProjectForm
from .token import emailactivationtokengenarator

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = emailactivationtokengenarator.make_token(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate Your account.'

            message = render_to_string('certificate_app/activationmail.html',{
                'user':user,
                'domain': current_site,
                'uid':str(uid),
                'token':str(token)
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[to_email])
            email.send()

            return HttpResponse('An email has been sent to you with instructions further')
        return render(request,'certificate_app/signup.html',{'form':form})
    form = SignupForm()
    return render(request,'certificate_app/signup.html',{'form':form})

def useractivation(request,uibd64,token):
    if request.method == 'GET':
        try:
            uid = force_text(urlsafe_base64_decode(uibd64))
            user = User.objects.get(id=uid)
        except(TypeError,ValueError,OverflowError,
    User.DoesNotExist):
            user = None

        if user is not None and \
            emailactivationtokengenarator.check_token(user,token):
            # user.is_active = True
            form = UserCreationForm(instance = user)
            return render(request,'certificate_app/usercreation.html',{'form':form})
        return HttpResponse('invalid token')
    elif request.method == 'POST':
        uid = force_text(urlsafe_base64_decode(uibd64))
        user = User.objects.get(id=uid)
        user.is_active = True
        form = UserCreationForm(request.POST,instance = user)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'certificate_app/usercreation.html',{'form':form})


def personal_detail(request):
    form = PersonalDetailForm()
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personal_form')
    return render(request,'certificate_app/personal_form.html',{'form':form})

def project_detail(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personal_form')
    return render(request,'certificate_app/project_form.html',{'form':form})


def test(request):
    if request.is_ajax():
        data = render_to_string('certificate_app/test.html')
        return JsonResponse(data, safe=False)
    # return render(request,'certificate_app/reportview.html')
    return JsonResponse({'data':None})
