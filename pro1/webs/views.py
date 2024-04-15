from django.shortcuts import render

def data_view(request):
    return render(request, 'data.html')