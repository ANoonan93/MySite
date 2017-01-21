from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm

# Create your views here.
def home(request):
	return render(request, 'home.html')

def basicInfo(request):
	return render(request, 'basic_info.html')

def contact(request):
	form = contactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = from_email
		contact_message = "%s: %s via %s"%(
			form_full_name, form_message, form_email)

		send_mail(subject, contact_message, 
			from_email, to_email, fail_silently=False)
	context = {
		"form": form,
	}
	return render(request, "contact.html", context)