from django.urls import path
from .views import (
    RestaurantList, RestaurantCreate, RestaurantUpdate, RestaurantDelete,
    MenuItemList, MenuItemCreate, MenuItemUpdate, MenuItemDelete
)

urlpatterns = [
    # Restaurant URLs
    path('restaurants/', RestaurantList.as_view(), name='restaurant-list'),  # GET (List all restaurants)
    path('restaurants/create/', RestaurantCreate.as_view(), name='restaurant-create'),  # POST (Create a new restaurant)
    path('restaurants/<int:pk>/update/', RestaurantUpdate.as_view(), name='restaurant-update'),  # PATCH (Update a restaurant)
    path('restaurants/<int:pk>/delete/', RestaurantDelete.as_view(), name='restaurant-delete'),  # DELETE (Delete a restaurant)

    # MenuItem URLs
    path('menu-items/', MenuItemList.as_view(), name='menu-item-list'),  # GET (List all menu items)
    path('menu-items/create/', MenuItemCreate.as_view(), name='menu-item-create'),  # POST (Create a new menu item)
    path('menu-items/<int:pk>/update/', MenuItemUpdate.as_view(), name='menu-item-update'),  # PATCH (Update a menu item)
    path('menu-items/<int:pk>/delete/', MenuItemDelete.as_view(), name='menu-item-delete'),  # DELETE (Delete a menu item)
]
