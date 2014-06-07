from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.response import TemplateResponse
from listofmenu.models import Menu
import urllib2
from datetime import datetime

# Create your views here.


# Adam, burada bu applicationa ait bir template kullanacagimizda, onu pathi vererek kullaniyoruz. Yani, index.html olsa bizim template'de, onu listofmenu/index.html diye cagiriyoruz.


def MainPage( request):
	m = Menu()
	m.date = datetime.now()
	m.mealName = 'Kuru Fasulye'
	m.save()
        #page = urllib2.urlopen('http://kafemud.bilkent.edu.tr/monu_tr.html')
        #soup = BeautifulSoup(page)
        #at = soup.body.findAll('td')
        #print at
	#if request.method == 'GET':
		#print request.GET
	if request.method == 'GET':
		print 'GET piyasada..'
	elif request.method == 'POST':
		print 'POST buralarda..'
	else:
		print 'Pek daha farkli bir mecra..'
        return render_to_response( 'listofmenu/newstars.html', { 'date':m.date, 'mealName':m.mealName})

def temp_page( request):
	if 'q' in request.GET:
		print request.GET['q']
		voted_meal = Menu.objects.get(id=1)
		total = voted_meal.total_point + int(request.GET['q'])
		print 'Total: ', total
		voted_meal.total_point = total
		voted_meal.total_vote += 1
		voted_meal.save()
		m = 'Input: %r' % request.GET['q']
	else:
		m = 'I dont know what it is'
	return HttpResponse( "The current average is %.2f" % voted_meal.average_point())

def star_selected( request):
	return HttpResponse( 'listofmenu/stats.html')

def about_page( request):
	return HttpResponse( 'listofmenu/about.html')

def stats_page( request):
	return TemplateResponse( request, 'listofmenu/home.html')
