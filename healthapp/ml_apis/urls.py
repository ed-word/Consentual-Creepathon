from django.conf.urls import url
from django.views.generic import RedirectView
from ml_apis.views import get_features, get_cluster_image

urlpatterns = [
    url(r'features_api/$', get_features),
    url(r'clusters/$', get_clusters),
    # url(r'^admin/', admin.site.urls),
]