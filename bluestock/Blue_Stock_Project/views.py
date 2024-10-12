from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new user
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login.html')  # Redirect to login page after successful registration
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'signup.html')