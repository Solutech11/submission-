from django.shortcuts import render,redirect
from .models import student
from django.views.generic import CreateView,TemplateView

# Create your views here.
class submission_view(CreateView):
    model=student
    fields = ['Name', 'subject', 'Assignment_name', 'Large_text', 'Task_Type', 'semester', 'Year', 'Image_Attachment', 'File_Attachment']
    template_name="Submit.html"
    success_url="/"

class mainView(TemplateView):
    template_name = "index.html"