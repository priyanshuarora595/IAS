from import_export import resources
from .models import Items

class ItemResources(resources.ModelResource):
    class Meta:
        model = Items
        