from django.forms import ModelForm
from .models import Organization, OrgMember, Student, College, Program
from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.save()
        return user


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class OrgMemberForm(ModelForm):
    class Meta:
        model = OrgMember
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"
