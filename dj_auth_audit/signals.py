from django.dispatch import Signal

# Regular Signals
user_logged_in = Signal()
user_logged_out = Signal()


user_signed_up = Signal()

password_set = Signal()
password_changed = Signal()
password_reset = Signal()

email_confirmed = Signal()
email_confirmation_sent = Signal()

password_reset_email_sent = Signal()
file_uploaded = Signal()


# ######### Signals for failing operations

rate_limit_password_reset_email_sent = Signal()
rate_limit_password_change = Signal()

rate_limit_password_reset = Signal()

mobile_upload_rate_limit = Signal()

AUTH_SIGNALS_CLASSES = [
    user_logged_in,
    user_logged_out,
    user_signed_up,
    password_set,
    password_changed,
    password_reset,
    email_confirmed,
    email_confirmation_sent,
    rate_limit_password_change,
    rate_limit_password_reset,
    rate_limit_password_reset_email_sent,
    password_reset_email_sent,
    file_uploaded,
    mobile_upload_rate_limit,
]
