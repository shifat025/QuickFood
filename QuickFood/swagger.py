from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Define the schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="QuickFood API",
        default_version='v1',
        description="Description of your API",
        contact=openapi.Contact(email="shifat58201@gmail.com"),
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)