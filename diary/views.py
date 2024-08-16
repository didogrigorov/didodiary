from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView
from diary.forms import ContactForm
from diary.models import BlogPost, About


# Create your views here.
class BlogListView(ListView):
    context_object_name = 'posts'
    paginate_by = 3
    model = BlogPost
    template_name = 'index.html'
    ordering = ['-date_posted']


class SingleBlogPostView(DetailView):
    model = BlogPost
    template_name = 'single-blog.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Get the previous post
        previous_post = BlogPost.objects.filter(date_posted__lt=post.date_posted).order_by('-date_posted').first()

        # Get the next post
        next_post = BlogPost.objects.filter(date_posted__gt=post.date_posted).order_by('date_posted').first()

        context['previous_post'] = previous_post
        context['next_post'] = next_post
        return context

class ContactFormView(FormView):
    template_name = 'contact.html'  # Template to be used for rendering the form
    form_class = ContactForm  # Form class to use
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        # Process the data in form.cleaned_data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Sending the email
        send_mail(
            subject=f'Message from my diary',
            message=message,
            from_email=email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return super().form_valid(form)

class SuccessForm(TemplateView):
    template_name = 'contact-success.html'

class AboutPage(DetailView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'

    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        return queryset.first()