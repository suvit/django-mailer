import logging

from django.core.management.base import NoArgsCommand

from mailer.models import Message

logger = logging.getLogger(__name__)

class Command(NoArgsCommand):
    help = "Attempt to resend any deferred mail."
    
    def handle_noargs(self, **options):
        count = Message.objects.retry_deferred() # @@@ new_priority not yet supported
        logger.info("%s message(s) retried" % count)
