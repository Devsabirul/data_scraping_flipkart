from django.db import models


class ScrapingData(models.Model):
    thumbnail = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    details = models.CharField(max_length=500,null=True)
    rating = models.CharField( max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
