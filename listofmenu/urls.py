from django.conf.urls import patterns, url
from listofmenu import views

urlpatterns = patterns( '',
	url( r'^search/$', views.temp_page, name = 'temppage'),
	url( r'stats.html', views.stats_page, name = 'statspage'),
	url( r'newstars.html', views.MainPage, name = 'main_again'),
	url( r'about.html', views.about_page, name = 'aboutpage'),
	url( r'^$', views.MainPage, name = 'main'),
)
