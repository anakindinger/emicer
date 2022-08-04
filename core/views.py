from django.shortcuts import render

# 
#
def index (request):
    context = {
        'teste': 'Este é um teste'
    }
    return render(request, 'index.html', context)

