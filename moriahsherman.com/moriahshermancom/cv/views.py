from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File

def home(request):
    image_data = open('/home/mo/Projects/websites/moriahsherman.com/documents/Test_document_PDF.pdf', 'rb') as pdf
    return HttpResponse(image_data, mimetype=application/pdf)

