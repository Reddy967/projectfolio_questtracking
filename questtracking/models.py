
import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class registerdetails(models.Model):
    Firstname = models.CharField(max_length=40)
    Lastname = models.CharField(max_length=40)
    Positiontitle = models.CharField(max_length=40)
    Gender = models.CharField(max_length=20)
    Dateofbirth = models.DateField()
    Address = models.CharField(max_length=30)
    Postalcode = models.IntegerField()
    Phonenumber = models.CharField(max_length=100)
    Email = models.EmailField()
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)



class projectmodel(models.Model):
    IT = 'IT'
    ELECTRONIC = 'EC'
    BANK = 'BK'
    OTHER = 'OT'
    DOMAIN_CHOICES = [
        (IT, 'It'),
        (ELECTRONIC, 'Electronic'),
        (BANK, 'Bank'),
        (OTHER, 'Other')

    ]


    Domain = models.CharField(
        max_length=30,
        choices=DOMAIN_CHOICES,
        default='IT',
    )
    Title = models.TextField()
    Startdate = models.DateField(auto_now=False, auto_now_add=False)
    Enddate = models.DateField(auto_now=False, auto_now_add=False )

    TEAM = 'TM'
    INDIVIDUAL = 'IND'
    OTHER = 'OT'
    BATCH_CHOICES = [
        (TEAM, 'Team'),
        (INDIVIDUAL, 'Individual'),
        (OTHER, 'Other')

    ]
    Batch = models.CharField(max_length=30, choices=BATCH_CHOICES, default='Team')

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    VERYHIGH = 'Veryhigh'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
        (VERYHIGH, 'Veryhigh')
    ]
    Priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default='Low')


class information(models.Model):
    Email = models.EmailField(max_length=200)
    Subject = models.CharField(max_length=100)
    Description = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)


class report(models.Model):
    Projectname = models.CharField(max_length=50)
    Teamname = models.CharField(max_length=50)
    Analysis = models.CharField(max_length=50)
    Design = models.CharField(max_length=50)
    Development = models.CharField(max_length=50)
    Testing = models.CharField(max_length=50)
    Documentation = models.CharField(max_length=50)

class show(models.Model):
    Teamname = models.CharField(max_length=50)
    Projectname = models.CharField(max_length=50)
    Progresstasks = models.CharField(max_length=50)
    Description = models.TextField()
    Tasks = models.CharField(max_length=50)

class load(models.Model):
    Projectname = models.CharField(max_length=50)
    Employeename = models.CharField(max_length=50)
    Completedwork = models.CharField(max_length=100)
    Remainingwork = models.CharField(max_length=50)
    Overduework = models.CharField(max_length=100)

class group(models.Model):
    PRODUCTOWNER = 'PO'
    PRODUCTMANAGER = 'PM'
    SOFTWAREARCHITECT = 'SA'
    DEVELOPER = 'DV'
    DESIGNER = 'DS'
    QUALITYASSURANCE = 'QA'
    BUSINESSANALYST = 'BA'
    EMPLOYEEROLE_CHOICES = [
        (PRODUCTOWNER, 'Product Owner'),
        (PRODUCTMANAGER, 'Product Manager'),
        (SOFTWAREARCHITECT, 'Software Architect'),
        (DEVELOPER, 'Developer'),
        (DESIGNER, 'Designer'),
        (QUALITYASSURANCE, 'Quality Assurance'),
        (BUSINESSANALYST, 'Business Analyst'),

    ]
    Employeerole = models.CharField(max_length=50,choices=EMPLOYEEROLE_CHOICES,default='Developer')
    Employeename = models.CharField(max_length=50)
    Projectname = models.CharField(max_length=50)
    Teamname = models.CharField(max_length=50)
    Teamlength = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
