from django.shortcuts import render

# Create your views here.
def jinja_cs(request):
    d={'a':200}
    return render(request,'commands.html',context=d)
def max_ab(request):
    d={'a':200,'b':20}
    return render(request,'commands.html',context=d)
def max(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'commands.html',d)
def max_ne_if(request):
    d={'a':20,'b':300,'c':40}
    return render(request,'commands.html',d)
def loop(request):
    d={'name':'ANANDH'}
    return render(request,'looping.html',d)
def loop1(request):
    d={'name':''}
    return render(request,'looping.html',d)