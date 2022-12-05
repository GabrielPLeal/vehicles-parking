from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework import routers

from customer.view import CostumerViewSet
from park_movement.view import ParkMovementViewSet, ParkMovementExitViewSet
from vehicle.view import VehicleViewSet

# SWAGGER
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()

router.register("customer", CostumerViewSet, basename="customer")
router.register("vehicle", VehicleViewSet, basename="vehicle")
router.register("movement", ParkMovementViewSet, basename="movement")
router.register("movement-exit", ParkMovementExitViewSet, basename="movement-exit")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    ]
