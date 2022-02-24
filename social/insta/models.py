from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.fields import related
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here
class Profile(models.Model):
    prof_photo = CloudinaryField('image',null=True)
    name = models.CharField(max_length=250, blank=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    like_count = models.ManyToManyField(User,related_name='liked',default=0)
    comm_count = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image',null=True)
    class Meta:
        ordering = ["-pk"]

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def total_likes(self):
        return self.like_count.count()
    
    @classmethod
    def get_profile_posts(cls,profile):
        posts = Images.objects.filter(profile__pk= profile)
        return posts
    @classmethod
    def update_post_caption(cls,id,caption):
        update =cls.objects.filter(id=id).update(caption=caption)
        return update

    def __str__(self):
        return f'{self.user.name} Post'


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'

class Comments(models.Model):
    comment = models.CharField(max_length=250)
    post = models.ForeignKey(Images,on_delete = models.CASCADE,related_name='comments',null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
    published_at = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return f'{self.comment} Image'
    
    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()
    
    @classmethod
    def filter_comments_by_post_id(cls, id):
        comments = Comments.objects.filter(post__id=id)
        return comments
    

    class Meta:
        ordering = ["-pk"]