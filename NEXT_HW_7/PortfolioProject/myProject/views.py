from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainPage.html')

def project(request):
    return render(request, 'myProject.html')