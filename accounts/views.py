from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#Log the user in
			return redirect('articles:list')
	elif request.method=='GET':
	    form = UserCreationForm()
	return render(request, 'accounts/signup.html', { 'form': form })