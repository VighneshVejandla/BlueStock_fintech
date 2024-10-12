from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError
from .models import UserSign

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Received data - Username: {username}, Email: {email}, Password: {password}")  # Debugging line

        try:
            hashed_password = make_password(password)
            user_sign = UserSign(username=username, email=email, password=hashed_password)
            user_sign.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        except IntegrityError:
            if 'unique constraint' in str(e).lower():
                if 'username' in str(e).lower():
                    messages.error(request, 'Username already exists.')
                elif 'email' in str(e).lower():
                    messages.error(request, 'Email already exists.')
            else:
                messages.error(request, 'An error occurred while creating the account.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Fetch the user by username
            user = UserSign.objects.get(email=email)
            
            # Check if the password matches
            if check_password(password, user.password):
                request.session['username'] = user.username
                messages.success(request, f'Welcome, {user.username}! You have successfully logged in.')
                return redirect('dashboard')  # Redirect to home or dashboard
            else:
                messages.error(request, 'Incorrect password. Please try again.')
        except UserSign.DoesNotExist:
            messages.error(request, 'Username does not exist. Please check your username or sign up.')
    
    return render(request, 'login.html')


def forgot_password_view(request):
    return render(request, 'forgotpassword.html')




from django.shortcuts import render
from .models import IPOInfo
from django.db.models import F

def dashboard(request):
    # Fetch all IPO data from the database
    ipo_data = IPOInfo.objects.all()

    total_ipo = ipo_data.count()

    # Example for gain: status = 1
    ipo_in_gain = ipo_data.filter(status=1).count()  

    # Example for loss: status = 2
    ipo_in_loss = ipo_data.filter(status=2).count()

    # New listed: where listing price > IPO price
    ipo_new_listed = ipo_data.filter(listing_price__gt=F('ipo_price')).count()

    # Upcoming: No listing gain yet (empty or None)
    ipo_upcoming = ipo_data.filter(listing_gain='').count() + ipo_data.filter(listing_gain__isnull=True).count()

    # Ongoing: Positive listing gain
    ipo_ongoing = ipo_data.filter(listing_gain__gt='0').count()

    context = {
        'ipo_data': ipo_data,
        'ipo_total': total_ipo,
        'ipo_gain': ipo_in_gain,
        'ipo_loss': ipo_in_loss,
        'ipo_new_listed': ipo_new_listed,
        'ipo_upcoming': ipo_upcoming,
        'ipo_ongoing': ipo_ongoing,
    }
    return render(request, 'dashboard.html', context)

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import IPOInfo

def manageipo(request):
    # Fetch all IPO data from the database
    ipo_data = IPOInfo.objects.all()
    paginator = Paginator(ipo_data, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'ipo_data': ipo_data,
        'page_obj': page_obj,
    }

    return render(request, 'manageipo.html', context)

from django.shortcuts import render, redirect
from .forms import IPOInfoForm  # Import your form
from .models import IPOInfo

def register_ipo(request):
    if request.method == 'POST':
        # Handle form submission
        form = IPOInfoForm(request.POST, request.FILES)  # Add request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save the form to the database
            return redirect('manageipo')  # Redirect back to the Manage IPO page after saving
    else:
        # Display empty form for GET request
        form = IPOInfoForm()
    
    return render(request, 'register.html', {'form': form})


