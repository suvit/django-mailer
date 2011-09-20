import logging

from django.conf import settings
from django.core.management.base import NoArgsCommand

from mailer.engine import send_all

logger = logging.getLogger(__name__)

# allow a sysadmin to pause the sending of mail temporarily.
PAUSE_SEND = getattr(settings, "MAILER_PAUSE_SEND", False)


class Command(NoArgsCommand):
    help = "Do one pass through the mail queue, attempting to send all mail."
    
    def handle_noargs(self, **options):
        # if PAUSE_SEND is turned on don't do anything.
        if not PAUSE_SEND:
            send_all()
        else:
            logger.info("sending is paused, quitting.")
