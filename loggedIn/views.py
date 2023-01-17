from django.shortcuts import render, redirect
from loggedIn.forms import creatNewUser
# Create your views here.


def teacherPage(request):
    if request.user.is_staff:
    
        return render(request, "teacherPage.html")
    else:
        return redirect('home')

def manage(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = creatNewUser(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = creatNewUser()
        return render(request, "management.html", {'form': form})

    else:
        return redirect('home')