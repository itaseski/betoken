from django.db import models


class Publisher(models.Model):
    """A company that publishes books."""
    name=models.CharField(max_length=50, help_text='The name of Publisher')
    web_site=models.URLField(max_length=200, help_text="The Publisher's website.")
    email = models.EmailField(max_length=254, help_text="The Publisher's email address.")
