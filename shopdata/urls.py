from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from shopdata.common.views import ProfileView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopdata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^login/$', TemplateView.as_view(template_name="login.html")),
    url(r'^products/', TemplateView.as_view(template_name="products.html")),
    url(r'^profile/', ProfileView.as_view(), name="profile"),
#    url(r'^profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)
