from django.db import models

# Create your models here.
class Videos(models.Model):
    video_title = models.CharField(max_length=200)
    video_description = models.TextField()
    youtube_video_embed_code = models.TextField()
    video_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.video_title
    
class Comments(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='videos_comments')
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment}: {self.video.video_title}"