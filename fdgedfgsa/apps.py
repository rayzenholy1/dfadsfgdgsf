from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class FdgedfgsaConfig(AppConfig):
    name = 'fdgedfgsa'

    def ready(self):
        # Create reader group and assign permissions
        from .models import Book
        reader_group, created = Group.objects.get_or_create(name='readers')
        if created:
            # Get permissions for viewing books
            content_type = ContentType.objects.get_for_model(Book)
            view_permission = Permission.objects.get(
                codename='view_book',
                content_type=content_type,
            )
            reader_group.permissions.add(view_permission)
            reader_group.save()
