from django.urls import path
from .views import *

urlpatterns = [
    path('', greetings),
    path('caesar/<str:plain_text>/<int:shift>', encode),

]
