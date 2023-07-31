from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import DriverRegistrationForm
from .models import DriverRegistrationModel,FattigueInfoModel


# Create your views here.
def DriverRegisterActions(request):
    if request.method == 'POST':
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = DriverRegistrationForm()
            return render(request, 'AutoistRegister.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = DriverRegistrationForm()
    return render(request, 'AutoistRegister.html', {'form': form})
def AutoistLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = DriverRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                request.session['vehiclenumber'] = check.vehiclenumber
                print("User id At", check.id, status)
                return render(request, 'autoist/AutoistHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'AutoistLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'AutoistLogin.html', {})
def AutoistHome(request):
    return render(request, 'autoist/AutoistHome.html', {})

def DetectFatigueDriver(request):
    from users.utility.detections import FatigueDetections
    obj = FatigueDetections()
    flag = obj.start_process()
    import geocoder
    g = geocoder.ip('me')
    import datetime
    l = g.latlng
    lattitude = l[0]
    longitude = l[1]
    if flag:
        print('Fatigue Detetcted')
        user_name = request.session['loggeduser']
        logged_user = request.session['loginid']
        email = request.session['email']
        vehiclenumber = request.session['vehiclenumber']
        c_date = datetime.datetime.now()
        rslt_dict = {
            'user_name': user_name,
            'login_user': logged_user,
            'email': email,
            'vehiclenumber': vehiclenumber,
            'lattitude': lattitude,
            'longitude': longitude,
            'fatigue': 'Fatigue',
            'c_date': c_date
        }
        FattigueInfoModel.objects.create(user_name=user_name, login_user=logged_user, email=email,vehiclenumber=vehiclenumber,lattitude=lattitude,longitude = longitude,fatigue='Fatigue',c_date=c_date)



    else:
        print('No Fatigue')
    return render(request, 'autoist/DetectionImage.html', rslt_dict)

def StartTraining(request):
    from users.utility import model
    return render(request, 'autoist/TrainingComplete.html', {})

def Autoisthistory(request):
    logged_user = request.session['loginid']
    qs = FattigueInfoModel.objects.filter(login_user=logged_user)
    return render(request, 'autoist/FastAutoistHistory.html',{'data':qs})
