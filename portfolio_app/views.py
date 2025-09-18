from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Home, About, Skill, Project, ContactInfo
from .forms import ContactForm

def portfolio(request):
    home = Home.objects.first()
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    contact_info = ContactInfo.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # stored in DB

            # try sending email to admin / contact_info.email
            recipient = contact_info.email if contact_info and contact_info.email else settings.DEFAULT_FROM_EMAIL
            subject = f"New message: {contact_message.subject}"
            body = f"From: {contact_message.name} <{contact_message.email}>\n\n{contact_message.message}"
            try:
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
                messages.success(request, "Your message has been sent successfully!")
            except Exception:
                # if email fails, still show a message but saved in DB
                messages.warning(request, "Message saved, but email couldn't be sent. Check your email settings.")
            return redirect('portfolio')
    else:
        form = ContactForm()

    context = {
        "home": home,
        "about": about,
        "skills": skills,
        "projects": projects,
        "contact_info": contact_info,
        "form": form,
    }
    return render(request, "portfolio.html", context)
