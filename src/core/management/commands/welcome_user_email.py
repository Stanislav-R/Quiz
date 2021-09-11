from datetime import datetime, time, timedelta

from accounts.models import CustomUser

from app import settings

from django.core.mail import send_mail
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware

from quiz.models import Result

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send welcome email to user if he didn't start testing"  # noqa

    def handle(self, *args, **options):

        users = CustomUser.objects.filter(is_activated=True).order_by('id')
        results = Result.objects.filter(update_timestamp__range=(today_start, today_end))
        for user in users:
            if not results:

                subject = "Welcome message"
                message = ""
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = user.email
                html_message = "<h1> Hello, let's start your testing! </h1>"

                send_mail(subject, message, from_email, recipient_list,
                          fail_silently=False, auth_user=None, auth_password=None,
                          connection=None, html_message=html_message)

                self.stdout.write("E-mail was sent.")
            else:
                self.stdout.write("No new registrations today.")
