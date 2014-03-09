from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # url(r'^$', views. index, name='index'),
    url(r'^index', views.index, name='index'),
    # url(r'^twoInd', views.index2, name='indexTwo'),
    url(r'(?P<poll_id>\d+)/vote$', views.vote, name='vote'),
    url(r'(?P<poll_id>\d+)$', views.results, name='results'),
    url(r'(?P<poll_id>\d+)/voted$', views.voted, name='voted')

)

#TODO do urls for detail, result, vote

"""
If your view method takes more than the "request" parameter you
can assign values to the other parameters using "kwargs" as a dictionary,
where the parameter is a "key" and the value is the "key:value".

For example:

In views.py
def sample(request,foo):
    return HttpResponse("Hello %d" % foo)

In urls.py in your app
urlpatterns = patterns('',
    url(r'^$', views.sample, name='sample', kwargs = {"foo":1}))

"""



"""
Regular Expressions:
start with r''
^string1 : the input has to start with string1
string1$ : the input has to end with string1
\d+ : the input can be multiple digits
?P<useThisVariableLater>\d+ : any digits given in input
                 will be saved in useThisVariableLater
"""