=====
Usage
=====

To use dj-auth-audit in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_auth_audit.apps.DjAuthAuditConfig',
        ...
    )

Add dj-auth-audit's URL patterns:

.. code-block:: python

    from dj_auth_audit import urls as dj_auth_audit_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_auth_audit_urls)),
        ...
    ]
