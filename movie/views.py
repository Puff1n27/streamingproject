from django.shortcuts import render, redirect
from .models import Movie, Movie2, Upcoming
from .forms import ContactForm
from django.contrib import messages as inquiry_msg
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def movie_detail(request, pk, movie_type='marvel'):
    if movie_type == 'dc':
        movie = get_object_or_404(Movie2, pk=pk)
    else:
        movie = get_object_or_404(Movie, pk=pk)

    return render(request, "movie_detail.html", {"movie": movie})
def home(request):
    movies = Movie.objects.all()
    movies2 = Movie2.objects.all()
    upcoming = Upcoming.objects.all()
    contact_msg = ""  # initialize empty

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            title = form.cleaned_data["title"]
            message_text = form.cleaned_data["message"]

            subject = f"Inquiry: {title}"
            body = f"From: {name}\nMail: {email}\nTitle: {title}\nMessage:\n{message_text}"

            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email="admin@example.com",
                to=["admin@example.com"],
            )
            email_message.send()

            contact_msg = "Message was sent successfully!"
            form = ContactForm() 

    else:
        form = ContactForm()

    context = {
        "movies": movies,
        "movies2": movies2,
        "upcoming": upcoming,
        "form": form,
        "contact_msg": contact_msg, 
    }

    return render(request, "home.html", context)





