from django.shortcuts import render,HttpResponse,redirect
from django.contrib.sessions.backends.db import SessionStore
from .models import registerdetails
from .models import projectmodel
from .models import information
from .models import report
from .models import show
from .models import load
from .models import group
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import logout as logout

# Create your views here.
def registerpage(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        positiontitle = request.POST.get('positiontitle')
        gender = request.POST.get('gender')
        dateofbirth = request.POST.get('dateofbirth')
        address = request.POST.get('address')
        postalcode = request.POST.get('postalcode')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = registerdetails()
        users.Firstname = firstname
        users.Lastname = lastname
        users.Positiontitle = positiontitle
        users.Gender = gender
        users.Dateofbirth = dateofbirth
        users.Address = address
        users.Postalcode = postalcode
        users.Phonenumber = phonenumber
        users.Email = email
        users.Username = username
        users.Password = password
        users.save()
    return render(request,'register.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = registerdetails.objects.get(Username=username,Password=password)
            user_id = user.id
            request.session['user.id'] = user_id
            print(user_id)
            return redirect('/homepage')
        except:
            return HttpResponse('Invalid')
    return render(request,'userlogin.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'questtracker' and password == 'authority':
            return redirect('/access')
        else:
            return HttpResponse('Invalid')
    return render(request,'adminlogin.html')

def portfolio(request):
    return render(request,'portfolio.html')

def homepage(request):
    if request.session.get('user.id'):
        user_id = request.session.get('user.id')
        context = {
            'user_id' : user_id
        }
    return render(request,'homepage.html', context)


def entrypage(request):
    if request.method == 'POST':
        domain = request.POST.get('domain')
        title = request.POST.get('title')
        startdate = request.POST.get('startdate','%y-%m-%d')
        enddate = request.POST.get('enddate','%y-%m-%d')
        batch = request.POST.get('batch')
        priority = request.POST.get('priority')
        data = projectmodel()
        print(domain,"this is the domain")
        print(title,'this is the title')
        print(startdate, 'this is the startdate')
        print(enddate, 'this is the enddate')
        print(batch, "this is the batch")
        print(priority, "this is the priority")
        data.Domain = domain
        data.Title = title
        data.Startdate = startdate
        data.Enddate = enddate
        data.Batch = batch
        data.Priority = priority
        data.save()
    return render(request,'entrypage.html')

def tickets(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        created = request.POST.get('created')
        message = information()
        message.Email = email
        message.Subject = subject
        message.Description = description
        message.Created = created
        message.save()
    return render(request,'tickets.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')

def projectdetails(request):
    details = projectmodel.objects.filter()
    return render(request,'projectdetails.html',{'value':details})

def projectdetails_delete(request,id):
    data = projectmodel.objects.filter(id=id).delete()
    return redirect('/entrypage')

def projectstatus(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        teamname = request.POST.get('teamname')
        analysis = request.POST.get('analysis')
        design = request.POST.get('design')
        development = request.POST.get('development')
        testing = request.POST.get('testing')
        documentation = request.POST.get('documentation')
        data = report()
        data.Projectname = projectname
        data.Teamname = teamname
        data.Analysis = analysis
        data.Design = design
        data.Development = development
        data.Testing = testing
        data.Documentation = documentation
        data.save()
    return render(request,'projectstatus.html')

def projectreport(request):
    details = report.objects.filter()
    return render(request,'projectreport.html',{'value':details})


def projectreport_delete(request,id):
    data = report.objects.filter(id=id).delete()
    return redirect('/projectstatus')

def tasks(request):
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        projectname = request.POST.get('projectname')
        progresstasks = request.POST.get('progresstasks')
        description = request.POST.get('description')
        tasks = request.POST.get('tasks')
        data = show()
        data.Teamname = teamname
        data.Projectname = projectname
        data.Progresstasks = progresstasks
        data.Description = description
        data.Tasks = tasks
        data.save()
    return render(request,'tasks.html')

def workload(request):
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        employeename = request.POST.get('employeename')
        completedwork = request.POST.get('completedwork')
        remainingwork = request.POST.get('remainingwork')
        overduework = request.POST.get('overduework')
        data = load()
        data.Projectname = projectname
        data.Employeename = employeename
        data.Completedwork = completedwork
        data.remainingwork = remainingwork
        data.Overduework = overduework
        data.save()
    return render(request,'workload.html')

def taskreport(request):
    data = show.objects.filter()
    return render(request,'taskreport.html',{'value':data})

def taskreport_delete(request,id):
    data = show.objects.filter(id=id).delete()
    return redirect('/tasks')

def profile(request,id):
    user = registerdetails.objects.filter(id=id)
    return render(request,'profile.html',{'value':user})



def profile_delete(request,id):
    user = registerdetails.objects.filter(id=id).delete()
    return redirect('/userlogin')

def teamsentry(request):
    if request.method == 'POST':
        employeerole = request.POST.get('employeerole')
        employeename = request.POST.get('employeename')
        projectname = request.POST.get('projectname')
        teamname = request.POST.get('teamname')
        teamlength = request.POST.get('teamlength')
        data = group()
        data.Employeerole = employeerole
        data.Employeename = employeename
        data.Projectname = projectname
        data.Teamname = teamname
        data.Teamlength = teamlength
        data.save()

    return render(request,'teamsentry.html')

def teams(request):
    data = group.objects.filter()
    return render(request,'teams.html',{'value':data})

def teams_delete(request,id):
    data = group.objects.filter(id=id).delete()
    return redirect('/teamsentry')

def notifications(request):
    data = information.objects.filter()
    return render(request,'notifications.html',{'value':data})

def notifications_delete(request,id):
    data = information.objects.filter(id=id).delete()

def home(request):
    return render(request,'home.html')

def access(request):
    return render(request,'access.html')

