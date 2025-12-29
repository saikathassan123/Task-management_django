from django.urls import path
from tasks.views import show_task , show_specific_tusk
urlpatterns = [
    path ("show-task/",show_task),
    path ('show_task/ <id>' , show_specific_tusk)
    ]
