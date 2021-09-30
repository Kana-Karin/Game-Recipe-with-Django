from django.db import models

# Create your models here.

class Recipe (models.Model):
    class Meta:
        verbose_name = "レシピ"
        verbose_name_plural = "レシピ"
        
    def __str__(self):
        return self.title
    title = models.CharField(max_length=50, verbose_name="タイトル")
    content = models.TextField(verbose_name="内容")
    
    description = models.TextField(blank=True,default="")

    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)