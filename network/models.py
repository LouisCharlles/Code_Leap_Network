from django.db import models


class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True,null=False,blank=False)

    username = models.CharField(max_length=50,null=False,blank=False)

    created_datetime = models.DateTimeField(auto_now_add=True,null=False,blank=False)

    title = models.CharField(max_length=250,null=False,blank=False)

    content = models.CharField(max_length=500,null=False,blank=False)
