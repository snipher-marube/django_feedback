Django Feedback
===============

Django Feedback is a simple Django application designed to facilitate the collection of user feedback within your Django project. It allows authenticated users to submit feedback easily, and optionally supports anonymous feedback submissions as well.

Installation
------------

1. **Add `feedback` to your INSTALLED_APPS in `settings.py`:**

    ```python
    INSTALLED_APPS = [
    ...
    'feedback',
    ...
    ]
    ```

2. **Define `FEEDBACK_CHOICES` in your Django project's settings (settings.py):**

    ```python
    FEEDBACK_CHOICES = (
    ('bug', 'Bug'),
    ('feature_request', 'Feature Request')
    )
    ```
3. **Include `feedback.urls` in your `urls.py`:**
    ```python
    urlpatterns = [
    ...
    path('feedback/', include('feedbak.urls')),
    ...
    ]
    ```


4. **Add `feedback.context_processors.feedback_form` to `TEMPLATE_CONTEXT_PROCESSORS` in settings.py:**

    ```python
    TEMPLATE_CONTEXT_PROCESSORS = [
    ...
    'feedbak.context_processors.feedback_form',
    ...
    ]
    ```

5. **Enable anonymous feedback (optional):**

    To allow anonymous users to provide feedback, set `ALLOW_ANONYMOUS_FEEDBACK` to `True` in your Django project's settings:

    ```python
    ALLOW_ANONYMOUS_FEEDBACK = True
    ```

    This setting allows both authenticated and anonymous users to submit feedback.

Note: After adding `feedback` to your `INSTALLED_APPS`, be sure to run migrations using `python manage.py migrate` to apply any necessary database changes.

Contributing
------------

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request on GitHub.
