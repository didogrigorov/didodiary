from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from diary.views import BlogListView, SingleBlogPostView, ContactFormView, SuccessForm, AboutPage

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('success/', SuccessForm.as_view(), name='success'),
    path('<slug:slug>/', SingleBlogPostView.as_view(), name='single-blog'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
