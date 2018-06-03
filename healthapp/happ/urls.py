from django.conf.urls import url
from . import views


urlpatterns = [url(r'^game/$', views.game, name='game'),
			url(r'^chatbot/$', views.chatbot, name='chatbot'),
			url(r'^myadmin/$', views.myadmin, name='myadmin'),
			url(r'^charts/$', views.charts, name='charts'),
			url(r'^home/$', views.home, name='home'),
]
