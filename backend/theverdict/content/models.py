from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    summary = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=255) #A slug field for SEO-friendly URLs.
    published = models.BooleanField(default=False) #Is the post published or in a draft.
    tags = models.ManyToManyField('Tag', related_name='posts')
    featured_image = models.ImageField(upload_to='images/', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('content.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"

class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    

    