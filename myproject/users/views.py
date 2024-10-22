from django.shortcuts import render

# Create your views here.
def registration(request):
    context = {
        'active_link': 'users',
    }
    return render(request, 'register/register.html', context)