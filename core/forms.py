from django import forms
from django.contrib.auth import password_validation
from registration.forms import RegistrationForm

from .models import Ingredient, Recipe, RecipeStep

TEXT_INPUT_CLASSES = "pa2 f4 w-100"


class CustomRegistrationForm(RegistrationForm):
    email = forms.EmailField(
        label="E-mail address",
        widget=forms.EmailInput(attrs={"class": TEXT_INPUT_CLASSES}),
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": TEXT_INPUT_CLASSES}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": TEXT_INPUT_CLASSES}
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta(RegistrationForm.Meta):
        widgets = {
            "username": forms.TextInput(attrs={"class": TEXT_INPUT_CLASSES}),
            "password": forms.PasswordInput(attrs={"class": TEXT_INPUT_CLASSES}),
            "password_confirmation": forms.PasswordInput(
                attrs={"class": TEXT_INPUT_CLASSES}
            ),
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "prep_time_in_minutes",
            "cook_time_in_minutes",
            "public",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": TEXT_INPUT_CLASSES}),
            "prep_time_in_minutes": forms.NumberInput(
                attrs={"class": TEXT_INPUT_CLASSES}
            ),
            "cook_time_in_minutes": forms.NumberInput(
                attrs={"class": TEXT_INPUT_CLASSES}
            ),
            "public": forms.CheckboxInput(attrs={"class": "ml2 mt2"}),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "amount",
            "item",
        ]


class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ["text"]

        widgets = {
            "text": forms.TextInput(attrs={"class": TEXT_INPUT_CLASSES}),
        }
