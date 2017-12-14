from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user$', views.new_user),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^dump_users$', views.dump_users),
    url(r'^logout$', views.logout),
    url(r'^add_book$', views.add_book),
    url(r'^review/(?P<review_id>\d+)$', views.review),
    url(r'^process$', views.process)

]
