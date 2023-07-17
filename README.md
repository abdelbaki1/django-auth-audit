**Make your authentication logs more easy with django-auth-audit**
==================================================================
# Please note
``django-auth-audit`` still an experimental project that originated as a feature in one of my professional projects. Due to the specific requirements and lack of existing GitHub repositories targeting this particular situation, I decided to create it as a separate project. As a result, the app is still in its early stages and may undergo frequent updates and improvements. Feedback and contributions are welcome.

# Introduction
```django-auth-audit``` is a Django reusable app that provides functionality for tracking user authentication events, such as logins,logouts,password rest rate limit ...
It allows you to define custom mixins that override specific CRUD methods in your target class, send signals, and handle the flow back to your target class. Additionally, django-auth-audit includes a pre-defined mixins,that can be used to send signals and create authentication logs.

## Installation

To install ```django-auth-audit```, follow these steps:

1. Ensure you have Django installed in your project. If not, you can install it using pip:

```shell
pip install django
```
Download the ```django-auth-audit``` package from the GitHub repository or install it using pip:
```python
pip install django-auth-audit
```
Add ```django-auth-audit``` to the INSTALLED_APPS setting in your Django project's settings.py file:
```python
INSTALLED_APPS = [
   ...
   'django-auth-audit',
   ...
]
```
Run the database migrations to create the necessary tables for the app:
```shell
python manage.py migrate django-auth-audit
```
# Usage
```django-auth-audit``` allows you to create custom mixins that override specific CRUD methods in your target class, send signals, and handle the flow back to your target class.
Here's an example:

```python
from dj_auth_audit.mixins import FailedResetEmailSignalMixin

class CustomPasswordResetView(FailedResetEmailSignalMixin, PasswordResetView):
    class_name = 'PasswordResetView'
    serializer_class = CustomPasswordResetSerializer
    throttle_scope = 'reset_password_rate'
```
In this example, the `CustomPasswordResetView` class inherits from `FailedResetEmailSignalMixin` and `PasswordResetView`. The `FailedResetEmailSignalMixin` sends a signal and creates an authentication log in the database, indicating the time of the sent reset email and the user who requested the password reset. If the user reaches the rate limit, another signal is triggered to indicate that the user has exceeded the password reset rate.

The FailedResetEmailSignalMixin is hooked with the POST and throttled methods, which are typically defined in the target class. To use this mixin, you need to define the `class_name` attribute in the subclass alongside with the self.user to define the actor.
### Note
```django-auth-audit``` has a built-in mixin for all basic authentication logs you will need ,inclusing but not limited to : `Login` , `Logout`,`password change`,`password reset`,`verfication email` ... and if you define a throttle scope on the subclass , you will get rate limit signal the user have exceeded the allowed request rate.

You can also define your own mixin by inheriting from `AbstractSignalMixin` in the `mixin.py` file.

Note: The `FailedResetEmailSignalMixin` or any other mixin will raise an exception if:

- ***class_name*** is not defined.
- The target class doesn't have any of the required methods for sending requests **(`POST`,`GET`...)**
- The ***self.user*** is not defined.
Please refer to `mixin.py` for more information on creating custom mixins and using the provided mixins.
# Contributing
If you'd like to contribute to this project, please follow these guidelines:

Fork the repository on GitHub.
Create a new branch from the master branch for your feature or bug fix.
Make your changes and ensure they are properly tested.
Commit your changes with clear and descriptive commit messages.
Push your branch to your forked repository.
Submit a pull request to the master branch of the this repository.
Please refer to the Contribution Guidelines for more information.

# License
```django-auth-audit``` is released under the MIT License. See the LICENSE file for more details.

# Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.
