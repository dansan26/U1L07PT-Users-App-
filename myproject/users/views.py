from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(request):
    # Check if the form is submitted
    if request.method == "POST":
        form = UserCreationForm(request.POST) # Submitted with data
        # Validate Form
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else: #Get method (Empty form)
        form = UserCreationForm()
    context = {
        'active_link': 'users',
        'form': form,
    }
    return render(request, 'register/register.html', context)