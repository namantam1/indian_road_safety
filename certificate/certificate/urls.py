from django.conf import settings
from django.conf.urls.static import  static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import TemplateView,PasswordResetView,LoginView,LogoutView
from certificate_app.views import signup,useractivation,personal_detail,project_detail,test
from certificate_app.reportsubmissionview import reportview,reportupdate
from certificate_app.certificateview import adminpage,intern_detail,create_certificate,change_status

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.default.urls')),
    path('',TemplateView.as_view(template_name='certificate_app/index.html'),name='home'),
    path('signup',signup,name='signup'),
    path('activate/<uibd64>/<token>',useractivation,name='activate'),
    path('login',LoginView.as_view(template_name='certificate_app/usercreation.html'),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),

    # report submissiion view
    # path('report',reportsumission,name='report'),
    path('reportview',reportview,name='reportview'),
    path('report/update',reportupdate,name='reportupdate'),

    # certificate view urls
    path('adminpage',adminpage,name='adminpage'),
    path('interdetail/<pk>',intern_detail,name='interndetail'),
    path('createcertificate/<pk>',create_certificate,name='create_certificate'),
    path('interndetail/<pk>',change_status,name='change_status'),


    #personal detail
    path('personalform',personal_detail,name="personal_form"),
    path('projectform',project_detail,name="project_form"),
    path('test',test,name="test"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
