from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


@user_passes_test(is_admin, redirect_field_name="home")
def admin_view(request):

    return render(request, 'relationship_app/admin_dashboard.html')
