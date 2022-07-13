"""sample_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from site_admin import views as adminview
from site_user import views as userview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',adminview.index,name='index'),
    url(r'^register/$',adminview.register,name='register'),
    url(r'^registerAction/$',adminview.registerAction,name='registerAction'),
    url(r'^login/$',adminview.login,name='login'),
    url(r'^loginAction/$',adminview.loginAction,name='loginAction'),
    url(r'^viewAllUsers/$',adminview.viewAllUsers,name='viewAllUsers'),
    url(r'^delete/(?P<uid>\d+)/$',adminview.delete,name='delete'),
    url(r'^edit/(?P<uid>\d+)/$',adminview.edit,name='edit'),
    url(r'^editAction/$',adminview.editAction,name='editAction'),
    url(r'^imageUpload/$',adminview.imageUpload,name='imageUpload'),
    url(r'^imageUploadAction/$',adminview.imageUploadAction,name='imageUploadAction'),
    url(r'^viewImages/$',adminview.viewImages,name='viewImages'),
    url(r'^JqueryExample/$',adminview.JqueryExample,name='JqueryExample'),
    url(r'^dropDownBinding/$',adminview.dropDownBinding,name='dropDownBinding'),
    url(r'^getstate/$',adminview.getstate,name='getstate'),
    url(r'^placeAddAction/$',adminview.placeAddAction,name='placeAddAction'),
    url(r'^checkUsername/$',adminview.checkUsername,name='checkUsername'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
