from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string


def base(request):
    if request.method == 'POST':
        to = request.POST['recipient_email_address']
        send_mail(
            'Test GA',
            'Here is the message.',
            'from@example.com',
            [to],
            html_message=render_to_string('email_template.html'),
            fail_silently=False,
        )
    return render(request, 'base.html', {})
