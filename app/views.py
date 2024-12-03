from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'Jyothsna','age':20}
    return render(request,'jinja.html',context=d)
