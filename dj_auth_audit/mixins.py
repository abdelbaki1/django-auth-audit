from dj_auth_audit.exceptions import ClassNameUnavailbleException, PostUnavailableException, SignalUnavailable, ViewUnavailable
from .signals import *
from abc import ABC
from django.utils.translation import ugettext_lazy as _


class AbstractSignalMixin(ABC):
    host_class: object
    class_name: str
    post_action: int
    user = None

    def get_host_class(self):
        if not hasattr(self, 'host_class'):
            self.search_class()
        return self.host_class

    def get_class_name(self):
        if not hasattr(self, 'class_name'):
            raise ClassNameUnavailbleException("class_name undefined")
        return self.class_name.lower()

    def search_class(self):
        classes = self.__class__.mro()
        for cls in classes:
            if cls.__name__.lower() == self.get_class_name():
                self.host_class = cls
                return

        else:
            raise ViewUnavailable('class name does not matches any existing view')

    def send_post_signal(self):
        self.get_post_signal().send(sender=self.user, action=self.post_action)

    def get_post_signal(self):
        raise SignalUnavailable('get_signal must be implemented')

    def post(self, request, *args, **kwargs):
        if not hasattr(self.get_host_class(), 'post'):
            raise PostUnavailableException(
                'unable to find post method in {}'.format(self.get_host_class()))
        if request.user.is_authenticated:
            self.user = request.user
        res = self.get_host_class().post(self, request, *args, **kwargs)
        self.send_post_signal()
        return res


class LoginSignalMixin(AbstractSignalMixin):
    post_action = 0

    def get_post_signal(self):
        return user_logged_in


class LogoutSignalMixin(AbstractSignalMixin):
    post_action = 2

    def get_post_signal(self):
        return user_logged_out


class AbstractThrottleSignalMixin(AbstractSignalMixin):
    def get_throttle_signal(self):
        raise SignalUnavailable()
    throttle_action: int
    message: str

    def send_throttle_signal(self, request):
        self.get_throttle_signal().send(sender=request.user, action=self.throttle_action, changes={
            'detail': "user" + request.user.username + "have " + self.message
        })

    def throttled(self, request, wait):
        self.send_throttle_signal(request=request)
        return self.get_host_class().throttled(self, request, wait)


class FailedPasswordResetSignalMixin(AbstractThrottleSignalMixin):
    """
    triggered when password reset limit is passed
    """
    message = "exceeded his password reset limit"
    throttle_action = 7
    post_action = 6

    def get_post_signal(self):
        return password_reset

    def get_throttle_signal(self):
        return rate_limit_password_reset


class FailedResetEmailSignalMixin(AbstractThrottleSignalMixin):
    message = "exceeded his email sent for reset password"
    throttle_action = 12
    post_action = 10

    def get_post_signal(self):
        return password_reset_email_sent

    def get_throttle_signal(self):
        return rate_limit_password_reset_email_sent


class FailedPasswordChangeSignalMixin(AbstractThrottleSignalMixin):
    """triggered when password change limit is passed"""
    message = "exceeded his password change limit"
    throttle_action = 5
    post_action = 4

    def get_signal(self):
        return password_changed

    def get_throttle_signal(self):
        return rate_limit_password_change


class FailedUploadImageRateSignal(AbstractThrottleSignalMixin):
    message = "exceeded his mobile upload  limit"
    throttle_action = 13
    post_action = 12

    def get_post_signal(self):
        return file_uploaded

    def get_throttle_signal(self):
        return mobile_upload_rate_limit
