from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_orgs"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()
        context["total_colleges"] = College.objects.count()
        today = timezone.now().date()
        context["students_joined_this_year"] = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("student")
            .distinct()
            .count()
        )
        return context

class OrganizationList(LoginRequiredMixin, ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        sort = self.request.GET.get("sort")
        if sort:
            qs = qs.order_by(sort)
        return qs


class OrganizationCreateView(PermissionRequiredMixin, CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    permission_required = 'studentorg.add_organization'


class OrganizationUpdateView(PermissionRequiredMixin, UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')
    permission_required = 'studentorg.change_organization'


class OrganizationDeleteView(PermissionRequiredMixin, DeleteView):
    model = Organization
    template_name = 'org_confirm_delete.html'
    success_url = reverse_lazy('organization-list')
    permission_required = 'studentorg.delete_organization'


class OrgMemberList(LoginRequiredMixin, ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'orgmembers'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related("student", "organization")
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(student__lastname__icontains=query) |
                Q(student__firstname__icontains=query) |
                Q(organization__name__icontains=query)
            )
        sort = self.request.GET.get("sort")
        if sort:
            qs = qs.order_by(sort)
        return qs


class OrgMemberCreateView(PermissionRequiredMixin, CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')
    permission_required = 'studentorg.add_orgmember'


class OrgMemberUpdateView(PermissionRequiredMixin, UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')
    permission_required = 'studentorg.change_orgmember'


class OrgMemberDeleteView(PermissionRequiredMixin, DeleteView):
    model = OrgMember
    template_name = 'orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember-list')
    permission_required = 'studentorg.delete_orgmember'

class StudentList(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related("program")
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(student_id__icontains=query) |
                Q(lastname__icontains=query) |
                Q(firstname__icontains=query) |
                Q(program__prog_name__icontains=query)
            )
        sort = self.request.GET.get("sort")
        if sort:
            qs = qs.order_by(sort)
        return qs


class StudentCreateView(PermissionRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')
    permission_required = 'studentorg.add_student'


class StudentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')
    permission_required = 'studentorg.change_student'


class StudentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
    permission_required = 'studentorg.delete_student'

class CollegeList(LoginRequiredMixin, ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'colleges'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(college_name__icontains=query)
        sort = self.request.GET.get("sort")
        if sort:
            qs = qs.order_by(sort)
        return qs


class CollegeCreateView(PermissionRequiredMixin, CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')
    permission_required = 'studentorg.add_college'


class CollegeUpdateView(PermissionRequiredMixin, UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')
    permission_required = 'studentorg.change_college'


class CollegeDeleteView(PermissionRequiredMixin, DeleteView):
    model = College
    template_name = 'college_confirm_delete.html'
    success_url = reverse_lazy('college-list')
    permission_required = 'studentorg.delete_college'

class ProgramList(LoginRequiredMixin, ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'programs'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().select_related("college")
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        sort = self.request.GET.get("sort")
        if sort:
            qs = qs.order_by(sort)
        return qs


class ProgramCreateView(PermissionRequiredMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')
    permission_required = 'studentorg.add_program'


class ProgramUpdateView(PermissionRequiredMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')
    permission_required = 'studentorg.change_program'


class ProgramDeleteView(PermissionRequiredMixin, DeleteView):
    model = Program
    template_name = 'program_confirm_delete.html'
    success_url = reverse_lazy('program-list')
    permission_required = 'studentorg.delete_program'
