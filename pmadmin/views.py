from django.shortcuts import render, redirect
import pyrebase
from django.http import HttpResponseForbidden, JsonResponse
from .models import UserPayments, Users, Profiles
from django_user_agents.utils import get_user_agent
import uuid
from django.db.models import Q,F


config = {
    "apiKey": "AIzaSyDNWXzX1f9lt_kId0PBVQDdBg5C67HtGsc",
    "authDomain": "paraiyar-matching.firebaseapp.com",
    "databaseURL": "https://paraiyar-matching-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "paraiyar-matching",
    "storageBucket": "paraiyar-matching.appspot.com",
    "messagingSenderId": "52739164199",
    "appId": "1:52739164199:web:baee8c7de875298bb2e602",
    "measurementId": "G-KE57QV8BZ3"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        context = {
        'title': 'Bumble Bees IT Solutions - Matrimony Website Application Management Service', 
        }
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            request.session['uid'] = user['localId']
            unique_id = uuid.uuid4().hex  # Generate a unique identifier for the session
            request.session['unique_id'] = unique_id
            request.session['email'] = user['email']
            return redirect(f'/o/secure/{unique_id}/admin-control/', context)
        except Exception as e:
            error_message = e.args[1]  # Extract the error message from Firebase exception
            return render(request, 'login.html', {'error': error_message})
        
    else:
        context = {
            'title': 'Bumble Bees IT Solutions - Matrimony Website Application Management Service'
        }
        return render(request, 'login.html', context)
        
       
   

def dashboard(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return HttpResponseForbidden("403 Forbidden: Unauthorized access.")
    
    # Query data from Profiles model
    total_profiles = Users.objects.count()
    male_profiles = Users.objects.filter(gender='Male').count()
    female_profiles = Users.objects.filter(gender='Female').count()
    paid_users = UserPayments.objects.filter(paid_status=1).count() 


    user_agent = get_user_agent(request) 
    os = user_agent.os.family

        # Retrieve email from session
    email = request.session.get('email', '')


    context = {
        'title': 'Dashboard - Matrimony Website Application - Bumble Bees IT Solutions',
        'total_profiles': total_profiles,
        'male_profiles': male_profiles,
        'female_profiles': female_profiles,
        'paid_users': paid_users,
        'os' : os,
        'browser_family': user_agent.browser.family,
        'browser_version': user_agent.browser.version_string,
        'email': email,
        
    }
    
    return render(request, 'dashboard.html', context)


def profile(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return HttpResponseForbidden("403 Forbidden: Unauthorized access.")
    
    user_agent = get_user_agent(request)
    os = user_agent.os.family

    search_query = request.GET.get('search', '')
    
    # Fetching user profiles and their related payments
    users_profiles = Users.objects.filter(
        Q(pmid__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(phone__icontains=search_query)
    )

    user_payments = UserPayments.objects.filter(user_pmid__in=users_profiles.values('pmid'))

    # Fetching marital_status from Profiles based on pmid
    user_pmid_list = users_profiles.values_list('pmid', flat=True)
    profiles_data = Profiles.objects.filter(user_pmid__in=user_pmid_list).values('user_pmid', 'marital_status')
    marital_status_dict = {profile['user_pmid']: profile['marital_status'] for profile in profiles_data}

    # Adding marital_status to each user profile
    for user in users_profiles:
        user.marital_status = marital_status_dict.get(user.pmid, '')

    context = {
        'title': 'Profile - Matrimony Website Application - Bumble Bees IT Solutions',
        'os': os,
        'browser_family': user_agent.browser.family,
        'browser_version': user_agent.browser.version_string,
        'users_profiles': users_profiles,
        'user_payments': user_payments,
        'search_query': search_query
    }
    
    return render(request, 'profile.html', context)



def update_marital_status(request):
    if request.method == 'POST':
        user_pmid = request.POST.get('user_pmid')
        marital_status = request.POST.get('marital_status')

        try:
            profile = Profiles.objects.get(user_pmid=user_pmid)
            profile.marital_status = marital_status
            profile.save()
            return JsonResponse({'status': 'success'})
        except Profiles.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profile not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


# Logout function 

def logout(request, unique_id):
    if not request.session.get('uid') or request.session.get('unique_id') != unique_id:
        return HttpResponseForbidden("403 Forbidden: Unauthorized access.")
    
    request.session.flush()  

    return redirect('index')  