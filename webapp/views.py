from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'testdata' : 'Template Var Test'}
    return render(request, 'index.html', context)

def map(request):
    image_data = open('templates/ScavengerMapDraft3.png', 'rb').read()
    return HttpResponse(image_data, content_type="image/png")

