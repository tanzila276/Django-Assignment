from django.shortcuts import render

def index (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def userinput(request):
    return render(request, 'userinput.html')

def viewdata(request):
    email= request.GET ['email']
    pas= request.GET ['pass']
    data={
        'email' : email,
        'password' : pas
    }
    return render(request, 'viewdata.html')