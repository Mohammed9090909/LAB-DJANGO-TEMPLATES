from django.shortcuts import render

def home(request):
   
    return render(request, 'search/home.html')
def terms_view(request):
    
    return render(request, 'search/terms.html')
