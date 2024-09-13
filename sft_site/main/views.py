from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Service, Advantage, TeamMember, Certificate, Project
from .tasks import send_contact_email
from .forms import ContactForm


def home(request):
    services = Service.objects.all()
    advantages = Advantage.objects.all()
    projects = Project.objects.all()
    team_members = TeamMember.objects.all()
    certificates = Certificate.objects.all()
    certificate_chunks = [certificates[i:i + 3] for i in range(0, len(certificates), 3)]
    return render(request, 'main/home.html', {'services': services, 'advantages': advantages,
                                              'projects': projects, 'team_members': team_members,
                                              'certificates': certificates})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка email асинхронно
            send_contact_email.delay(name, email, message)
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

