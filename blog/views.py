from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post,Images
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def home(request):
	all_posts = Post.objects.all()
	return render(request, "home.html",{'all_posts': all_posts})	

def create_post(request):
	if not request.user.is_authenticated:
		return redirect("/login/")
	if request.method == "POST":
		form_title = request.POST['title']
		form_body = request.POST['body']
		new_post = Post.objects.create(title = form_title, body = form_body)
		for i in request.FILES.getlist('image'):
			print(i)
			img = Images.objects.create(post=new_post,image=i)
			img.save()
		return redirect(f"/post/{new_post.id}/")		
	return render(request, "create_post.html")	

def post_page(request, post_id):
	post = Post.objects.get(id = post_id)	
	img =Images.objects.filter(post = post)
	return render(request, "page.html", {"post":post,"img":img})	

def sign_in(request):
	if request.method == "POST":
		username = request.POST.get('username', None)	
		password = request.POST.get('password', None)
		print(username, password)
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			print("Im in")
			login(request, user)
			return redirect("/")
	return render(request, "sign_in.html")

def sign_out(request):
	logout(request)
	return redirect("/")



def sign_up(request):
	if request.method == "POST":
		fullname = request.POST.get('fullname',None)
		email = request.POST.get('email',None)
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		user_exists = User.objects.filter(username=username).exists()
		if not user_exists:
			user = User.objects.create_user(
				username = username,
				password = password,
				email = email,
				first_name = fullname.split()[0],
				last_name = fullname.split()[1:]
				)
			login(request, user)
			return redirect("/")
		else:
			return HttpResponse("User already exists. Try new username.")
	return render(request, "sign_up.html")

 




 