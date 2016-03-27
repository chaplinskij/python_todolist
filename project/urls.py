from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^projects/$', 'project.views.show_all'),
    url(r'^project/add_project/$', 'project.views.add_project'),
    url(r'^project/add_task/$', 'project.views.add_task'),
    url(r'^project/delete_task/$', 'project.views.delete_task'),
    url(r'^project/change_project/$', 'project.views.change_project'),
    url(r'^project/change_task/$', 'project.views.change_task'),
    url(r'^$', 'project.views.home'),
]