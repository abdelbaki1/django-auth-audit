from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AuthLogEntry(models.Model):
    class Action:
        LOGIN = 0
        LOGIN_FAILURE = 1
        LOGOUT = 2
        LOGOUT_FAILURE = 3
        PASSWORD_CHANGE_SUCCESS = 4
        PASSWORD_CHANGE_FAILURE = 5
        PASSWORD_RESET_SUCCESS = 6
        PASSWORD_RESET_FAILURE = 7
        EMAIL_VALIDATION_SUCCESS = 8
        EMAIL_VALIDATION_FAILURE = 9
        EMAIL_REST_PASSWORD_SUCCESS = 10
        EMAIL_REST_PASSWORD_FAILURE = 11
        UPLOAD_SUCCESS = 12
        UPLOAD_FAILURE = 13

        choices = (
            (LOGIN, _("login")),
            (LOGIN_FAILURE, _("login_failure")),
            (LOGOUT, _("logout")),
            (LOGOUT_FAILURE, _("logout_failure")),
            (PASSWORD_CHANGE_SUCCESS, _("password_change_success")),
            (PASSWORD_CHANGE_FAILURE, _("password_change_failure")),
            (PASSWORD_RESET_SUCCESS, _("password_reset_success")),
            (PASSWORD_RESET_FAILURE, _("password_reset_failure")),
            (EMAIL_VALIDATION_SUCCESS, _("email_validation_success")),
            (EMAIL_VALIDATION_FAILURE, _("email_validation_failure")),
            (EMAIL_REST_PASSWORD_SUCCESS, _("email_reset_password_success")),
            (EMAIL_REST_PASSWORD_FAILURE, _("email_reset_password_failure")),
            (UPLOAD_SUCCESS, _('upload_success')),
            (UPLOAD_FAILURE, _("upload_failure")),
        )

    action = models.PositiveSmallIntegerField(
        choices=Action.choices, verbose_name=_("action"), db_index=True
    )
    cid = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        null=True,
        verbose_name=_("Correlation ID"),
    )
    changes = models.JSONField(null=True, verbose_name=_("change message"))
    actor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
        verbose_name=_("actor"),
    )
    timestamp = models.DateTimeField(
        default=timezone.now,
        db_index=True,
        verbose_name=_("timestamp"),
    )

    class Meta:
        get_latest_by = "timestamp"
        ordering = ["-timestamp"]
        verbose_name = _("authlog entry")
        verbose_name_plural = _("authlog entries")

    def __str__(self) -> str:
        return f"authlog of {self.actor} with action {self.Action.choices[self.action][1]}"
