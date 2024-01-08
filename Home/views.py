from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'Home/home.html')


def base_page(request):
    return render(request, 'common_code/base.html')
