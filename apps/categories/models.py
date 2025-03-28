import json
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categorie'

    def __str__(self):
        data = {
            'id': self.id,
            'name': self.name
        }
        return json.dumps(data)
