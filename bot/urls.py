from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from bot.views import BotAPIView

urlpatterns = [
    path('', csrf_exempt(BotAPIView.as_view()))
]
