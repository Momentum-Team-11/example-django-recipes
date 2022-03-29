from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Recipe
from .serializers import RecipeSerializer


class RecipeListView(APIView):
    def get(self, request, format=None):
        """
        List all the recipes
        """
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        # return a response with json data
        return Response(serializer.data)
