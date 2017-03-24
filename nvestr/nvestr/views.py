from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.views.generic import FormView
from forms import RegistrationForm
from django.contrib.auth.models import User

def landing_page(request):
	if request.method == 'GET':
		form = RegistrationForm()
		# template_name = 'landing_page.html'
		css_file = 'nvestr/landing_page.css'
		navbar_template = 'nav_bar.html'
		header_template = 'header.html'
		sidebar_template = 'sidebar.html'
		content_template = 'registration_form.html'
		return render(request, 'landing_page.html', {'form' : form, 
			'navbar_template' : navbar_template,
			'sidebar_template' : sidebar_template,
			'content_template' : content_template,
			'css_file' : css_file,
			'header_template' : header_template})

	else:
		form = RegistrationForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = User.objects.create_user(username=username,
											email=email,
											password=password)
			return render(request, 'registration_success.html')


	
	