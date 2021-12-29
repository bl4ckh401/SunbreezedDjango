from django.urls import path
from .views import AddToCart, AllProducts, GetCSRFToken, Inventory, UserList, current_user, post_product
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', Inventory.as_view()),
    path('post/', post_product.as_view()),
    path('product/', AllProducts.as_view()),
    path('cart/', AddToCart.as_view(), name="cart"),
    path('getcsrf/', GetCSRFToken.as_view()),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('token-auth/', obtain_jwt_token)

    ]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)