from import_export import resources
from .models import User


class UserResources(resources.ModelResource):
    class Meta:
        model = User
