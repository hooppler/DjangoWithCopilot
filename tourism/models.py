from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='village_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.village.name})"

class Event(models.Model):
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.village.name}"