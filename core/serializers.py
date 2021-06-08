from rest_framework import serializers
from .models import Post


# these fields are of what type, how to dump them to JSON will be 
# taken care by serializer. We don't need to take care of dumping to JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','owner']