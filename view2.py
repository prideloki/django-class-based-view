from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import View
from django.shortcuts import render


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class SuperAdminRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(SuperAdminRequiredMixin, cls).as_view(**initkwargs)
        superadmin_required = user_passes_test(lambda u: u.is_superuser)

        return superadmin_required(view)


class StaffRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(StaffRequiredMixin, cls).as_view(**initkwargs)
        staff_required = user_passes_test(lambda u: u.is_staff)
        return staff_required(view)


class EmailRequiredMixin(object):

    def email_required(user):
        return user.email

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(EmailRequiredMixin, cls).as_view(**initkwargs)
        email_required = user_passes_test(lambda u: cls.email_required(u))
        return email_required(view)


class UserNameSpecificMixin(object):

    def check_user_name(user):
        return 'usr1' == user.username

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(UserNameSpecificMixin, cls).as_view(**initkwargs)
        username_specific = user_passes_test(lambda u: cls.check_user_name(u))
        return username_specific(view)


class PermissionRequiredMixin(object):
    permission_required = None

    def check_user(self, user):
        return user.has_perm(self.permission_required)

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(PermissionRequiredMixin, cls).as_view(**initkwargs)
        permissions = user_passes_test(lambda u: cls.check_user(cls, u))
        return permissions(view)


class SuperAdminPage(SuperAdminRequiredMixin, View):

    def get(self, request):
        template_name = 'myapp/superadmin_page.html'
        return render(request, template_name)


class StaffPage(StaffRequiredMixin, View):

    def get(self, request):
        template_name = 'myapp/staff_page.html'
        return render(request, template_name)


class EmailPage(EmailRequiredMixin, View):

    def get(self, request):
        template_name = 'myapp/email_required.html'
        return render(request, template_name)


class UserNameSpecificPage(UserNameSpecificMixin, View):

    def get(self, request):
        template_name = 'myapp/only_this_user.html'
        return render(request, template_name)


class OnlyViewQuestions(PermissionRequiredMixin, View):
    permission_required = 'polls.view_question'

    def get(self, request):
        template_name = 'myapp/only_this_user.html'
        return render(request, template_name)
