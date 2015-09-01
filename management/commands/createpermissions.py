from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from myapp.global_permissions import GlobalPermission


class Command(BaseCommand):

    def handle(self, *args, **options):

        if not GlobalPermission.objects.filter(codename='can_do_it').exists(): 
          GlobalPermission.objects.create(codename='can_do_it', name='Can do it')
        if not GlobalPermission.objects.filter(codename='can_did_it').exists(): 
          GlobalPermission.objects.create(codename='can_did_it', name='Can did it')
          # if not Permission.objects.filter(codename="create_manager").exists():
          #     Permission.objects.create(codename='create_manager',
          #                               name='Create Campaign Manager',
          #                               content_type=campaign_user_content_type)
        # if not Permission.objects.filter(codename="create_viewer").exists():
        #     Permission.objects.create(codename='create_viewer',
        #                               name='Create Campaign Viewer',
        #                               content_type=campaign_user_content_type)
        # if not Permission.objects.filter(codename="assign_campaign").exists():
        #     Permission.objects.create(codename='assign_campaign',
        #                               name='Assign Campaign to User',
        #                               content_type=campaign_content_type)
