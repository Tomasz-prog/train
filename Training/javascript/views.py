from django.shortcuts import render

def MainJS(request):
    ctx = {}
    return render(request, 'main_js.html', ctx)