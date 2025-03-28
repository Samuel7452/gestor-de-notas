import json
from django.db import models
from apps.categories.models import Categories

class Notes(models.Model):

    title = models.CharField(max_length=255, null=True)
    content = models.CharField(max_length=10000000, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'notes'
        verbose_name = 'Notes'

    def __str__(self):

        data = {
            'id': self.id,
            'name': self.name,
        }
        return json.dumps(data)

