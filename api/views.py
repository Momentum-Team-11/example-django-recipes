from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Recipe
from .serializers import RecipeSerializer
from rest_framework.generics import ListAPIView

# class RecipeListView(APIView):
#     def get(self, request, format=None):
#         """
#         List all the recipes
#         """
#         recipes = Recipe.objects.all()
#         serializer = RecipeSerializer(recipes, many=True)
#         # return a response with json data
#         return Response(serializer.data)

# refactor that view to use a Generic View
# https://www.django-rest-framework.org/api-guide/generic-views/#listapiview
# notice that with this I do not need to provide a get() method!
class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
