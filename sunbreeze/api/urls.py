from django.urls import path
from .views import AllProducts, GetCSRFToken, Inventory, post_product,cart

urlpatterns = [
    path('', Inventory.as_view()),
    path('post/', post_product.as_view()),
    path('product/', AllProducts.as_view()),
    path('cart/', cart, name="cart"),
    path('getcsrf/', GetCSRFToken.as_view())
    ]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)