import random
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegisterForm, PhotoForm, AvatarForm
from images.forms import ImageForm
from .models import User
from images.models import Image, Categorie
from pages.models import Page
import datetime
import jwt


# Create your views here.
max_age = 365*24*60*60

def index(request):
    user = get_user(request)
    if user is not None:
        context = {
            'user': True,
            'name': user.name,
            'username': user.username,
            'email':  user.email,
            'avatar':  user.avatar,
        }
        return render(request, 'index.html', context)        
    return render(request, 'index.html')

def images(request):
    categories = Categorie.objects.all()
    page = Page.objects.get(name='images')
    images = Image.objects.all()
    context = {
        'icon': page.icon,
        'categories': categories,
        'images': images,
    }
    return render(request, 'images.html', context)    


def image_category(request, category):
    


@csrf_protect
def login(request):
    msg = ''
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            user = User.objects.filter(email=email).first()
            token = create_token(user.id)
            response = HttpResponseRedirect(reverse('users:user'))
            response.set_cookie(key='jwt', value=token, max_age=max_age, httponly=True)
            return response
        return render(request, 'login.html', {'msg': 'invalid user'})
    return render(request, 'login.html', {'msg': msg})

@csrf_protect
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = UserRegisterForm(request.POST)
        if form.is_valid() == True:
            user = User.objects.create_user(username, email, password)
            user.name = name
            user.save()
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                user = User.objects.filter(email=email).first()
                token = create_token(user.id)
                response = HttpResponseRedirect(reverse('users:user'))
                response.set_cookie(key='jwt', value=token, max_age=max_age, httponly=True)
                return response
    return render(request, 'register.html')

@csrf_protect
def recover(request):
    if request.method == "POST":
        email = request.POST.get('email')
        auth_token = request.POST.get('auth_token')
        password = request.POST.get('password')
        if email is not None:
            try:
                user = User.objects.get(email=email)
                send_mail(user, 'recover')
                token = create_token(id=user.email)
                response = render(request, 'recover.html', {'status': 'token'})
                response.set_cookie(key='recover', value=token, max_age=5*60, httponly=True)
                return response
            except:
                return render(request, 'recover.html', {'status': '', 'msg': 'invalid email'})
                
        elif auth_token is not None:
            token = request.COOKIES.get('recover')
            payload = decode_token(token)
            if payload is None:
                return render(request, 'recover.html', {'status': ''})
            else: 
                try:
                    user = User.objects.get(email=payload['id'])
                    print(user)
                    if (user.token_valid() == False):
                        return render(request, 'recover.html', {'status': 'token', 'msg': 'token expired'})
                    else:
                        if (user.auth_type == 'recover') and (user.auth_token == str(auth_token)):
                            response = render(request, 'recover.html', {'status': 'password'})
                            response.set_cookie(key='auth', value=auth_token, max_age=5*60, httponly=True)
                            return response
                        else:
                            return render(request, 'recover.html', {'status': 'token', 'msg': 'invalid token'})
                except:
                    pass
        elif password is not None:
            token = request.COOKIES.get('recover')
            auth_token = request.COOKIES.get('auth')
            payload = decode_token(token)
            if payload is None:
                return render(request, 'recover.html', {'status': ''})
            else:
                user = User.objects.filter(email=payload['id']).first()
                if (user.token_valid() == True) and (user.auth_type == 'recover') and (user.auth_token == str(auth_token)):
                        user.auth_type = ''
                        user.auth_token = ''
                        user.set_password(password)
                        user.save()
                else:
                    return render(request, 'recover.html', {'status': 'password', 'msg': 'invalid token'})
            return HttpResponseRedirect(reverse('users:login'))

    return render(request, 'recover.html', {'status': ''})

def logout(request):
    response = HttpResponseRedirect(reverse('users:user'))
    response.delete_cookie('jwt')
    return response

def avatar_upload(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = get_user(request)
            user.avatar = form.instance
            user.save()
            img_obj = form.instance
            return render(request, 'avatar_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PhotoForm()
    return render(request, 'avatar_upload.html', {'form': form})

def image_upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_user(request)
            form.instance.client = user
            form.save()
            img_obj = form.instance
            return render(request, 'image_upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def get_user(request):
    token = request.COOKIES.get('jwt')
    payload = decode_token(token)
    try:
        user = User.objects.get(id=payload['id'])
        return user
    except:
        return None



# def authenticate(email, password):
#     msg = 'Success'
#     user = User.objects.filter(email=email).first()
#     if user is None:
#         msg = 'User not found'
#         return msg
#     elif not (user.password == password):
#         msg = 'Incorrect password'
#     return msg




def create_token(id):
    try:
        payload = {
            'id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=max_age),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        return token
    except:
        return None

def decode_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        return payload
    except:
        return None

def send_mail(user,auth_type ):
    if auth_type == 'recover':
        rand_auth = auth_code()
        user.auth_token = rand_auth
        user.auth_type = auth_type
        user.token_date = timezone.now()
        user.save()
        print(f'email: {user.email} | token: {rand_auth}')

def auth_code():
    return random.randint(100000, 999999)