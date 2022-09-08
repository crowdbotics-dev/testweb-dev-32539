from django.conf import settings
from django.db import models


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class CustomText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"
