from django.db import models

# Create your models here.

class SearchModel(models.Model):
    address = models.CharField(max_length=150,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
    # save the first letter of address as uppercase
    def save(self, *args, **kwargs):
        self.address = self.address.title()
        super(SearchModel, self).save(*args, **kwargs)