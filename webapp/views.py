from django.shortcuts import render

def index(request):
    #template = loader.get_template('index.html')
    #context = RequestContext(request, {'testdata': 'Template Var Test'})
    #return HttpResponse(template.render(context))
    context = {'testdata' : 'Template Var Test'}
    return render(request, 'index.html', context)

