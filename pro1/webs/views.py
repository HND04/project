from django.shortcuts import render
def test(request):
    return render(request,'ex.html')
def data_view(request):
    return render(request, 'data.html')