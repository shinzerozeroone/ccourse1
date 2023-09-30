from photoalbum.decorators import unauthenticated_user
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ReviewSerializer
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Post, PostImage, PremAlbum, Premium, Vip, VipAlbum, Category, FullAlbum, Full, Author, Review
from .forms import ContactForm, CreateUserForm
from .filters import CategotyFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

class ReviewViewSet(viewsets.ModelViewSet):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class SingleReviewView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@allowed_users(['admin'])
def react(request):
    return render(request, 'index.html')

@login_required(login_url='login')
@admin_only
def main_view(request):
    return render(request, 'main.html')

def pie_chart(request):
    labels = ['BASIC', 'PRO', 'VIP', 'FULL']
    data = [post_count, prems_count, vips_count, full_count]

    posts = Post.objects.all()
    post_count = posts.count()
    prems = Premium.objects.all()
    prems_count = prems.count()
    vips = Vip.objects.all()
    vips_count = vips.count()
    fulls = Full.objects.all()
    full_count = fulls.count()
    counts = [post_count, prems_count, vips_count, full_count]
    print(post_count)

    for co in counts:
        data.append(co)

    return render(request, 'blog.html', {
        'labels': labels,
        'data': data,
    })

@login_required(login_url="login")
@allowed_users(['admin', 'customer', 'viewer'])
def blog_view(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    post_count = posts.count()
    prems = Premium.objects.all()
    prems_count = prems.count()
    vips = Vip.objects.all()
    vips_count = vips.count()
    fulls = Full.objects.all()
    full_count = fulls.count()
    myFilter = CategotyFilter(request.GET, queryset=categories)
    categories = myFilter.qs
    return render(request, 'blog.html', {'categories': categories, 'posts': posts, 'prems': prems, 'vips': vips, 'fulls': fulls, 
    'myFilter': myFilter, 'post_count': post_count, 'prems_count': prems_count, 'vips_count': vips_count, 'full_count': full_count})

@login_required(login_url="login")
def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {
        'post': post,
        'photos': photos
    })

@login_required(login_url="login")
@allowed_users(['admin', 'customer'])
def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'create-post.html')

def premdetail_view(request, id):
    prem = get_object_or_404(Premium, id=id)
    photos = PremAlbum.objects.filter(post=prem)
    return render(request, 'detail.html', {
        'prem': prem,
        'photos': photos
    })

@allowed_users(['admin', 'customer'])
def create_prem_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        prem = Premium.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            PremAlbum.objects.create(
                post=prem,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createprem-post.html')


def vipdetail_view(request, id):
    vip = get_object_or_404(Vip, id=id)
    photos = VipAlbum.objects.filter(post=vip)
    return render(request, 'vipdetail.html', {
        'vip': vip,
        'photos': photos
    })


@allowed_users(['admin', 'customer'])
def create_vip_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        vip = Vip.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            VipAlbum.objects.create(
                post=vip,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createvip-post.html')


def fulldetail_view(request, id):
    full = get_object_or_404(Full, id=id)
    photos = FullAlbum.objects.filter(post=full)
    return render(request, 'fulldatail.html', {
        'vip': full,
        'photos': photos
    })


@allowed_users(['admin', 'customer'])
def create_full_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        full = Full.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            FullAlbum.objects.create(
                post=full,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'createfull-post.html')

@login_required(login_url="login")
def catalog_view(request):
    categories = Category.objects.all()

    return render(request, 'catalog.html', {'categories': categories})

def contact_view(request):
    return render(request, 'contacts.html')

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Пользователь" + username + " был успешно зарегистрирован")
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('main')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def userPage(request):
    context = {}
    return render(request, 'user.html', context)

def viewPage(request):
    context = {}
    return render(request, 'viewer.html', context)

class AddContact(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

