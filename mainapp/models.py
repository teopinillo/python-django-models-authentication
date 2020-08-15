from django.db import models
from django.conf import settings

class BlogPost (models.Model):
    title = models.CharField ( max_length = 200, unique= True)
    author = models.ForeignKey (settings.AUTH_USER_MODEL, related_name="post", on_delete=models.CASCADE)
    body = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        self.title
    # Having a get_absolute_url method lets Django determine the canonical URL for a given model.
    # This will come in handy in our views.
    def get_absolute_url (self):
        return reverse('post', args=[str(self.id)])