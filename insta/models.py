from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='post/', blank = 'true')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()

    def __str__(self):
     return f'{self.user.name}Profile'    


class Post(models.Model):
    image = models.ImageField(upload_to='post/', blank=True)
    title = models.CharField(max_length=30)
    caption = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    # pub_date = models.DateTimeField(auto_now_add=True,default='')

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def search_by_title(cls,search_term):
        insta=cls.objects.filter(title_icontains=search_term)    

    def __str__(self):
        return self.title    