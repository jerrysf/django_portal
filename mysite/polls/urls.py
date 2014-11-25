from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<product_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<product_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<product_id>\d+)/vote/$', views.vote, name='vote'),
    # chart
    url(r'chart/(?P<chart_name>\w+)', views.chart_view_with_parameter, name='chart'),
    url(r'chart', views.chart_view, name='chart'),
)