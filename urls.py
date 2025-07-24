from django.urls import path
from .views import signup, create_assignment, submit_assignment, view_submissions,login_view

urlpatterns = [
    path('signup/', signup),
    path('login/', login_view),
    path('assignments/create/', create_assignment),
    path('assignments/submit/', submit_assignment),
    path('assignments/view/', view_submissions),
]