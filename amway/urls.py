from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'amway.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'inventario.views.inicio'), #index
    url(r'^logout/$','inventario.views.cerrar_sesion'),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/$','inventario.views.admin_index'),
    url(r'^admin/usuario/$','inventario.views.admin_index'),
    url(r'^admin/producto/$','inventario.views.nuevo_producto'),
    url(r'^admin/inventario/$','inventario.views.lista_productos'),
    url(r'^admin/reporte/$','inventario.views.admin_index'),

    url(r'^user/$','inventario.views.user_index'),
    url(r'^user/inventario/$', 'inventario.views.lista_productos'),
    url(r'^user/ticket/$', 'inventario.views.crear_ticket'),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),

    
)