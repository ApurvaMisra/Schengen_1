
from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns=[
    #/measurement/
    url(r'^$', views.index, name='index'),
    #/measurement/start/
    url(r'^start/$', views.startf, name='startf'),
    #/measurement/current/
    url(r'^current/$', views.currenth, name='currenth'),
    #/measurement/probe/
    url(r'^probe/$', views.probefill, name='probefill'),
    #/measurement/target/
    url(r'^target/$', views.targetfill, name='targetfill'),
    # /measurement/create/
    url(r'^create/$', views.create, name='create'),
    #/measurement/msm_id/
    url(r'^(?P<msm_idvar>[0-9]+)/$',views.option, name='option'),
    #measurement/stop
    url(r'^stop/(?P<msm_idvar>[0-9]+)/$',views.stop, name='stop'),
    #measurement/result
    url(r'^result/(?P<msm_idvar>[0-9]+)/$',views.result, name='result'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



