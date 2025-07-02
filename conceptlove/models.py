from django.db import models

class PersonalPage(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    html_content = models.TextField()  

    def __str__(self):
        return f"{self.title} ({self.code})"