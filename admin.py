from django.contrib import admin
from myapp.models import Role, Book, Organization
import logging
# Register your models here.

logger = logging.getLogger(__name__)

class RoleAdmin(admin.ModelAdmin):
    exclude = ('permissions',)


class BookAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(BookAdmin, self).get_queryset(request)

        user = request.user

        if user.is_superuser:
            return queryset

        organization = Organization.objects.get(user=user)
        logger.debug('Something went wrong!')
        return queryset.filter(organization=organization)
        


class OrganizationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Role, RoleAdmin)
