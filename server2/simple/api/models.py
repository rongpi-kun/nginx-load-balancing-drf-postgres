from django.db import models

from django.db import models

class Books(models.Model):
    bookname = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'

