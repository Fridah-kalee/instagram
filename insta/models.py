from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='posts/', blank = 'true')
    bio = models.TextField()

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()

    def __str__(self):
     return f'{self.username}Profile'    


class Post(models.Model):
    image = models.ImageField(upload_to='posts/', blank=True)
    title = models.CharField(max_length=30)
    caption = models.TextField(max_length=300)
    # pub_date = models.DateTimeField(auto_now_add=True,default='')

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title    