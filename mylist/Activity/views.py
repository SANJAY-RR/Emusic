from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import  CreateUserForm
from django.contrib.auth.models  import User
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.save()
            messages.success(request,'Your Account As Been Created')
            return redirect('login')
        else:
            messages.warning(request,'password mismathching !!!')
            return redirect('register')
    else:
        form=CreateUserForm()
        return render(request,'register.html',{'form':form})
def logout(request):
    auth_logout(request)
    return render(request,'logout.html')
@login_required    
def profile(request):
    return render(request,'profile.html')
def about(request):
    return render(request,'about.html')
@login_required  
def subscription(request):
    return render(request,'subscription.html')
def contact(request):
    return render(request,'contact.html')

# views.py in the music app
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
from django.shortcuts import redirect

def spotify_auth(request):
    # Spotify OAuth setup
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope="user-library-read user-top-read",  # Adjust the scopes as per your needs
    )

    auth_url = sp_oauth.get_authorize_url()
    
    # Redirect the user to the Spotify login page
    return redirect(auth_url)

# views.py in the music app
from django.shortcuts import render
from django.conf import settings
from spotipy.oauth2 import SpotifyOAuth
import spotipy

def spotify_callback(request):
    sp_oauth = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
    )

    # Get the authorization token from the request
    token_info = sp_oauth.get_access_token(request.GET['code'])
    access_token = token_info['access_token']

    # You can use the access token to interact with Spotify API
    sp = spotipy.Spotify(auth=access_token)

    # Example: Get the current user's saved tracks
    results = sp.current_user_saved_tracks()

    # Render a page with the results
    return render(request, 'music/spotify_home.html', {'tracks': results['items']})


