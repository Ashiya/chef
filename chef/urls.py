from django.conf.urls import url, include
from chef.views import CreateChef, CreateRecipe

urlpatterns = [
	# url(r'^create_user/$', CreateUser.as_view()),
	url(r'^create_chef/$', CreateChef.as_view()),
	url(r'^create_recipe/(?P<pk>[0-9]+)/$', CreateRecipe.as_view()),
	]