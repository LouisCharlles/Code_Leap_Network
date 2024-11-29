from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.http import JsonResponse
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt,name="dispatch")
class CreatePostView(View):
    
    def post(self,request):
        
        data = json.loads(request.body)
        username = data.get("username")
        title = data.get("title")
        content = data.get("content")

        new_post = Post.objects.create(username=username,title=title,content=content)

        return JsonResponse({
            "username": new_post.username,
            "title": new_post.title,
            "content": new_post.content,
        },
            status=201,)
    
@method_decorator(csrf_exempt,name="dispatch")
class GetPostsView(View):
    
    def get(self,*args,**kwargs):
        all_posts = Post.objects.all().values()
        return JsonResponse(list((all_posts)),status=200,safe=False)

@method_decorator(csrf_exempt,name="dispatch")    
class UpdatePostView(View):
    
    def patch(self,request,*args,**kwargs):
        post_id = kwargs.get("post_id")

        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")

        if title and content:
            Post.objects.filter(post_id=post_id).update(title=title,content=content)

            updated_post = Post.objects.filter(post_id=post_id).values("title","content").first()

            return JsonResponse(updated_post,status=200)
        return JsonResponse({"Error":"Could not update post"})
    
@method_decorator(csrf_exempt,"dispatch")
class DeletePostView(View):
    
    def delete(self,*args,**kwargs):
        post_id = kwargs.get("post_id")

        post_to_delete = Post.objects.get(post_id=post_id)

        post_to_delete.delete()

        return JsonResponse({"message":"Post was sucessufully deleted."},status=200)