from django.conf.urls.defaults import *
from django.conf import settings

# You may have to replace 'views' with 'apps.(package).views below.'
# this is a known issue

urlpatterns = patterns('apps.bottomlessPit.views',
                       (r'crawl_test/abs/(?P<page_seed>.*)$', 'abs_crawl_test'),
                       (r'crawl_test/(?P<page_seed>.*)$', 'crawl_test'),
                       (r'get_page/$', 'test_get_page'),
                       (r'^$','index'),
)
