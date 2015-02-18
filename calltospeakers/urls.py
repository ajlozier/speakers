from django.conf.urls import include, url
from django.contrib import admin

from cfp import views, forms


urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(
        r'^login/$',
        views.LoginView.as_view(),
        name='login'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='logout'),
    url(
        r'^signup/$',
        views.SignupView.as_view(),
        name='signup'),
    url(
        r'^password_change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(
        r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(
        r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        name='password_reset'),
    url(
        r'^password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(
        r'^reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
    url(
        r'^admin/',
        include(admin.site.urls)),
    url(
        r'^conferences/new$',
        views.ConferenceCreate.as_view(),
        name='conference_create'),
    url(
        r'^feed$',
        views.LatestCallsFeed(),
        name='call_feed'),
    url(
        r'^profile$',
        views.ProfileEdit.as_view(),
        name='profile'),
    url(
        r'^talks/(?P<pk>\d+)$',
        views.TalkDetail.as_view(),
        name='talk_read'),
    url(
        r'^submissions/(?P<pk>\d+)$',
        views.SubmissionDetail.as_view(),
        name='submission_read'),
    url(
        r'^submissions$',
        views.SubmissionList.as_view(),
        name='submission_list'),

    url(
        r'^(?P<year>\d+)/(?P<slug>[\w-]+)$',
        views.legacy,
        name='legacy_redirect'),
    url(
        r'^(?P<slug>[\w-]+)/(?P<year>\d+)/call/new$',
        views.CallCreate.as_view(),
        name='call_create'),
    url(
        r'^(?P<slug>[\w-]+)/(?P<year>\d+)/call/edit$',
        views.CallEdit.as_view(),
        name='call_edit'),
    url(
        r'^(?P<slug>[\w-]+)/(?P<year>\d+)/edit$',
        views.ConferenceEdit.as_view(),
        name='conference_edit'),
    url(
        r'^(?P<slug>[\w-]+)/(?P<year>\d+)$',
        views.call_detail_and_form,
        name='call_read'),
    url(
        r'^$',
        views.CallList.as_view(),
        name='call_list'),
]
