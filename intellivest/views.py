from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portefolje(request):
    return render(request, 'portefolje.html')

def omoss(request):
    return render(request, 'omoss.html')

def kontaktsendt(request):
    return render(request, 'kontaktsendt.html')

def kontakt(request):

	form_class = ContactForm(request.POST or None)

	# print form_class
	if request.method == 'POST':
	 	if form_class.is_valid():
			contact_name = form_class.cleaned_data['contact_name']
			contact_email = form_class.cleaned_data['contact_email']
			form_content= form_class.cleaned_data['content']

            # Email the profile with the 
            # contact information
	        template = get_template('contact_template.txt')
	        context = Context({
	            'contact_name': contact_name,
	            'contact_email': contact_email,
	            'form_content': form_content,
	        })

	        content = template.render(context)

	        email = EmailMessage(
	            "New contact form submission",
	            content,
	            "admin@intellivest.no",
	            ['admin@intellivest.no'],
	            headers = {'Reply-To': contact_email }
	            )
	        email.send()
	        return redirect('kontaktsendt')

	return render(request, 'kontakt.html', {
        'form': form_class,
    })

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

