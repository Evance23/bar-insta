from django.shortcuts import render
from django.http  import HttpResponse, Http404 
from django.contrib.auth.decorators import login_required
from .models import Profile,Follow,Image,Comments
from django.contrib.auth.models import User 
from .forms import UnfollowForm,FollowForm,CreateProfileForm,UpdateProfile,CreatePost 
from django.urls import reverse 


# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Insta')



def index(request):
    return render(request, "index.html") 


#@login_required
def index(request):
  current_user=request.user
  try:
    profile= Profile.objects.get(user=current_user)
  except Profile.DoesNotExist:
    raise Http404()

  index_timeline=[]
  images = Image.objects.filter(profile=profile)
  for image in images:
    index_timeline.append(image.id)

  followers_posts=Follow.objects.filter(follower=profile)
  for follower in followers_posts:
    followed_profiles=follower.followed
    followed_images=Image.profile_images(followed_profiles)
    for images in followed_images:
      index_timeline.append(images.id)
  timeline_images=Image.objects.filter(pk__in=index_timeline).order_by('-pub_date')

  all_profiles=Profile.objects.all()
  comments=Comments.objects.all()[:5]
  count=comments.count()
  follow_suggestions=Profile.objects.all()[:6]
  title = "Instagramex"

  return render(request,'index.html',{"all_profiles":all_profiles,"title":title,"profile":profile,"timeline_images":timeline_images,"follow_suggestions":follow_suggestions,"image_comments":comments})