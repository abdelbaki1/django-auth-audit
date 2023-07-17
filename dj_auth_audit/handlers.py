from .models import AuthLogEntry


def create_auth_log(sender, action, changes=None, *args, **kwargs):
    AuthLogEntry.objects.create(actor=sender, action=action, changes=changes)
