from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
def landing_page:
	return TemplateView.as_view(template_name='landing_page.html')