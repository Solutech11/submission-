from django.db import models
from django import forms

subject_choice =(
    ('CSE 201','CSE 201 Programming Concepts (Advanced Programming)'),
    ('CSE 211','CSE 211 Computer Programming using VB.NET'),
    ('CSE 221','CSE 221 System Programming Concept (C, C++) (Embedded Systems)'), 
    ('CSE 231','CSE 231 Computer Application Packages II (Mobile Computing)'),
    ('CSE 241','CSE 241 Structured Query Language I (Cyber Security)'), ('CSE 251','CSE 251 Relational Database Management Systems (RDBMS) '),
    ('ENT 201','ENT 201 Entrepreneurship Development'),
)
task_choice = (('assignment','Assignment'),
    ('classwork','Classwork'),
    ('test','Test'),
)
semester_choice =(
    ('1st','1st Semester'), 
    ('2nd','2nd Semester'),
    ('3rd','3rd Semester'),
)
year_choice=(
    ('1 year','1st year'),
    ('2 year','2nd year'), 
    ('3 year','3rd year'),
    ('4 year','4th year'),
)
# Create your models here.
class student (models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    subject = models.CharField(choices=subject_choice ,max_length=300,blank=True, null=True)
    Assignment_name =models.CharField(max_length=255, blank=True, null=True )
    Task_description = models.TextField(blank=True, null=True)
    Task_Type = models.CharField(choices = task_choice,max_length=255, blank=True, null=True)
    semester =models.CharField(choices=semester_choice, max_length=255, blank=True, null=True)
    Year= models.CharField(choices=year_choice, max_length=255, blank=True, null=True)
    Image_Attachment = models.ImageField(upload_to ='media/',blank=True, null=True)
    File_Attachment =models.FileField(upload_to='%d/%m/%y/', blank=True, null=True)
    date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.Name +" " + self.subject +": "+ self.Assignment_name+": "+self.Task_Type +"---------------------------"+ str(self.date)
    





        