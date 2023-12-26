
from django.contrib import auth,messages
from django.contrib.auth.models import User
from .models import UserInfo
from django.shortcuts import render, redirect
from .models import Branch,Registration


def home(request):
    branches = Branch.objects.all()
    return render(request, 'home.html', {'branches': branches})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('banking_app:new_page')
        else:
            # Check if the user exists with the provided username
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html',
                              {'message':  "Incorrect Password"})
            else:
                return render(request, 'login.html', {'message': "Username is Invalid"})

    return render(request, "login.html")

def new_page(request):
    return render(request, 'new_page.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                return render(request, 'register.html',
                              {'message': "Username already exists. Please choose a different username."})
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                Registration.objects.create(username=username,password=password)
                messages.success(request, "User registered successfully.")

        else:
            return render(request, 'register.html', {'message': "Your passwords do not match."})
        return redirect('banking_app:login')

    return render(request, 'register.html')

# banking_app/views.py

def register_form(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('countryCode') + request.POST.get('phoneNumber')
        email_id = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_name')
        materials_provided = request.POST.getlist('material')


        user, created = User.objects.get_or_create(username=name, email=email_id)



        user_info = UserInfo.objects.create(
            user=user,
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
        )


        user_info.materials_provided.set(materials_provided)


        return redirect('banking_app:home')

    return render(request, 'register_form.html')

def submit_form(request):
    if request.method == 'POST':

        confirmation_message = 'Successfully registered'  # Confirmation message

        # Redirect to the home page after displaying the confirmation message
        return render(request, 'submit_form.html', {'confirmation_message': confirmation_message})
    else:
        return render(request, 'register_form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')