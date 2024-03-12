from django.db import models

class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
