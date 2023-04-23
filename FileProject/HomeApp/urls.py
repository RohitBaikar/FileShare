from django.urls import path
from . import views

urlpatterns = [
    path('handle/',views.HandleFileUpload.as_view()),
    path('',views.home_view.as_view()),
    path('download/<uid>',views.download_view,name='download'),
]