from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Blog
from .serializers import BlogSerializer

# List Blog Posts API View (For Authenticated Users)
class BlogListView(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

# Create Blog Post API View
class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def post(self, request):
        # Ensure the user has permission to add a blog
        if not request.user.has_perm('blog.add_blog'):
            raise PermissionDenied("You do not have permission to add a blog.")

        # Create the blog
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Set the current user as the author
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Blog Post API View
class BlogDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def delete(self, request, pk):
        # Ensure the user has permission to delete a blog
        if not request.user.has_perm('blog.delete_blog'):
            raise PermissionDenied("You do not have permission to delete a blog.")

        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the blog is authored by the user or if the user is an admin
        if blog.author == request.user or request.user.is_superuser:
            blog.delete()
            return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        else:
            raise PermissionDenied("You are not allowed to delete this blog.")


