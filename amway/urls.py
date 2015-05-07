from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amway.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'inventario.views.inicio'), #index
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/$','inventario.views.inicio'),
    url(r'^test/$', 'inventario.views.test'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
	url(r'^productos/$', 'inventario.views.productos'),
    url(r'^productos/nuevo$', 'inventario.views.nuevo_producto'),

    url(r'^inventario/$', 'inventario.views.lista_productos'),
)
