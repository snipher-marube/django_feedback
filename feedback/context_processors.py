from django.conf import settings

from .forms import FeedbackForm, AnonymousFeedbackForm

def feedback_form(request):
    feedback_form = None
    if request.user.is_authenticated:
        feedback_form = FeedbackForm
    elif getattr(settings, 'ALLOW_ANONYMOUS_FEEDBACK', True):
        feedback_form = AnonymousFeedbackForm
    
    context = {
        'fedback_form': feedback_form
    }
    return context