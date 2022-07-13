from django.shortcuts import render,redirect
from site_admin.models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(name=name,dob=dob,gender=gender,address=address,country=country,phone=phone,username=username,password=password)
    user.save()
    messages.add_message(request,messages.INFO,"registration successful")
    return redirect('register')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(username=username,password=password)
    if len(user)>0:
        return render(request,'userhome.html',{'data':user})
    else:
        messages.add_message(request,messages.INFO,"Incorrect username or password")
        return redirect('login')
def viewAllUsers(request):
    user=register_tb.objects.all()
    return render(request,'viewAllUsers.html',{'data':user})
def delete(request,uid):
    user=register_tb.objects.filter(id=uid).delete()
    return redirect('viewAllUsers')
def edit(request,uid):
    user=register_tb.objects.filter(id=uid)
    return render(request,'edit.html',{'data':user})
def editAction(request):
    uid=request.POST['uid']
    print("uid=",uid)
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    user=register_tb.objects.filter(id=uid).update(name=name,dob=dob,gender=gender,address=address,country=country,phone=phone,username=username)
    print(user)
    messages.add_message(request,messages.INFO,"updated successfully")
    return redirect('viewAllUsers')
def imageUpload(request):
    return render(request,'imageUpload.html')
def imageUploadAction(request):
    name=request.POST['name']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image="no pic"
    images=image_tb(name=name,file=image)
    images.save()
    messages.add_message(request,messages.INFO,"Image uploaded successfully")
    return redirect('imageUpload')
def viewImages(request):
    image=image_tb.objects.all()
    return render(request,'viewImages.html',{'data':image})
def JqueryExample(request):
    return render(request,'JqueryExample.html')
def dropDownBinding(request):
    country=country_tb.objects.all()
    return render(request,'dropDownBinding.html',{'country':country})
def getstate(request):
    countryid=request.GET['countryid']
    states=state_tb.objects.filter(countryid=countryid)
    return render(request,'getstate.html',{'state':states})
def placeAddAction(request):
    countryid=request.POST['country']
    countryid_obj=country_tb.objects.get(id=countryid)
    stateid=request.POST['state']
    stateid_obj=state_tb.objects.get(id=stateid)
    place=request.POST['place']
    item=place_tb(countryid=countryid_obj,stateid=stateid_obj,place=place)
    item.save()
    messages.add_message(request,messages.INFO,"addedd successfully")
    return redirect('dropDownBinding')
def checkUsername(request):
    username=request.GET['username']
    user=register_tb.objects.filter(username=username)
    if len(user)>0:
        msg="exists"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
