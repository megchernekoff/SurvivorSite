from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirects to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
