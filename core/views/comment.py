from rest_framework import viewsets, mixins
from rest_framework.response import Response
from core.models import Comment, CommentLike, Flower
from flauth.models import User
from core.serializers import CommentSerializer
from core.paginators import CommentPaginator

class _CommentViewSet():
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CommentPaginator


class CommentFlowerViewSet(_CommentViewSet, viewsets.ModelViewSet):
    def get_queryset(self):
        flower = Flower.objects.get(pk=self.kwargs['flower_pk'])
        return Comment.objects.filter(flower=flower)

    def perform_create(self, serializer):
        flower = Flower.objects.get(pk=self.kwargs['flower_pk'])
        serializer.save(user=self.request.user, flower=flower)


class CommentUserViewSet(_CommentViewSet, viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        return Comment.objects.filter(user=user)


class CommentLikeViewSet(_CommentViewSet, viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs['user_pk'])
        return Comment.objects.filter(comment_likes__user=user, comment_likes__like=True)












# from rest_framework import status
# from rest_framework.views import APIView
# import floweryroad.settings.base as settings

# from flauth.models import User
# from core.models import Comment, Flower
# from core.serializers.comment import CommentListSerializer
# from core.paginators.comment import CommentPaginator

# # from jockbo.apps.common.models import Post, Comment
# # from jockbo.apps.common.permissions import IsOwnerOrReadOnly
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# # from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class FlowerCommentList(APIView):
#     # permission_classes = (IsAuthenticatedOrReadOnly,)
#     def get(self, request, id):        
#         paginator = CommentPaginator()
#         comments = Comment.objects.all().filter(flower=Flower.objects.get(id=id))
#         comments = paginator.paginate_queryset(comments, request)
#         serializer = CommentListSerializer(comments, context={'request':request}, many=True)
#         return paginator.get_paginated_response(serializer.data)

# class UserCommentList(APIView):
#         # permission_classes = (IsAuthenticatedOrReadOnly,)
    
#     def get(self, request, id):        
#         paginator = CommentPaginator()
#         comments = Comment.objects.all().filter(user=User.objects.get(id=id))
#         comments = paginator.paginate_queryset(comments, request)
#         serializer = CommentListSerializer(comments, context={'request':request}, many=True)
#         return paginator.get_paginated_response(serializer.data)




    # def post(self, request, postPk=None):
    #     serializer = CommentSerializer(data=request.data)
    #     try:
    #         serializer.is_valid()
    #         serializer.save(user=request.user, post=Post.objects.get(id=postPk))
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     except:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class FlowerDetail(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Comment, id=commentPk)

#     def get(self, request, pk=None):
#         comment = self.get_object(pk)
#         comments = paginator.paginate_queryset(comments, request)
#         serializer = CommentListSerializer(comments, context={'request':request}, many=True)
#         return paginator.get_paginated_response(serializer.data)

#     def put(self, request, commentPk, format=None):
#         try:
#             comment = self.get_object(commentPk)
#             serializer = CommentSerializer(comment, data=request.data)
#             serializer.is_valid()
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         except Comment.DoesNotExist:  
#             return Response({'error':'comment is not existed'}, status=status.HTTP_400_BAD_REQUEST)
#         except:  
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, commentPk, format=None):
#         try:
#             snippet = self.get_object(commentPk)
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response({'error':'comment is not existed'}, status=status.HTTP_400_BAD_REQUEST)