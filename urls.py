from django.conf.urls import url, include
from . import views
from . import view2
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.MyView.as_view(), name='index'),
    url(r'^v2/$', views.MyView2.as_view(greeting="Good day mate",
                                        name="John"), name='index2'),
    url(r'^publishers/$', views.Publisher.as_view(), name="publishers"),
    url(r'^books/(?P<pk>[0-9]+)/$',
        views.BookDetail.as_view(), name="details"),
    url(r'^books2/([\w-]+)/$', views.AuthorBookList.as_view(),
        name="book-by-author"),
    url(r'^authors/(?P<pk>[0-9]+)/$',
        views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^create$', views.EmployeeRegister.as_view(), name='register'),
    url(r'^superadmin/$', view2.SuperAdminPage.as_view(), name='superadmin'),
    url(r'^staff/$', view2.StaffPage.as_view(), name='staff'),
    url(r'^mail/$', view2.EmailPage.as_view(), name='mail'),
    url(r'^only-me/$', view2.UserNameSpecificPage.as_view(), name='only-me'),
    url(r'^permission/$', view2.OnlyViewQuestions.as_view(), name='permission'),
]
