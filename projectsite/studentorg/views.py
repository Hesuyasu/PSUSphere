from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class OrganizationList(ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_confirm_delete.html'
    success_url = reverse_lazy('organization-list')

# ---- OrgMember ----


class OrgMemberList(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'orgmembers'
    paginate_by = 5


class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember-list')

# ---- Student ----


class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

# ---- College ----


class CollegeList(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'colleges'
    paginate_by = 5


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')


class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_confirm_delete.html'
    success_url = reverse_lazy('college-list')

# ---- Program ----


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'programs'
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_confirm_delete.html'
    success_url = reverse_lazy('program-list')
