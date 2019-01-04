from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def signup_view(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#Log the user in
			user = form.save()
			login(request, user)
			return redirect('articles:list')
	elif request.method=='GET':
	    form = UserCreationForm()
	return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			login(request, user)
			return redirect('articles:list')
	elif request.method == 'GET':
		form = AuthenticationForm()

	return render(request, 'accounts/login.html', {'form':form})