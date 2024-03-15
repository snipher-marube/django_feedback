from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import FeedbackForm, AnonymousFeedbackForm

def leave_feedback(request):
    form_class = FeedbackForm if request.user.is_authenticated else AnonymousFeedbackForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_id = request.user.id if request.user.is_authenticated else None
            feedback.save()

            messages.success(request, 'Your feedback submited success fully')
            return redirect(request.POST.get('next', request.META.get('HTTP_REFERER', '/')))
  
    context = {
        'form': form
    }
    return render(request, 'feedback/feedback_form.html', context)
