from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('submission/', views.submission_view.as_view()),
    path('', views.mainView.as_view() )
    # path('success', views.)


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)