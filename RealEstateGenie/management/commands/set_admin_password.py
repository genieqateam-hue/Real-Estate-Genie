from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Set admin password to Sales@2025'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'Sales@2025'
        
        # Create or update admin user
        user, created = User.objects.get_or_create(
            username=username,
            defaults={'is_staff': True, 'is_superuser': True}
        )
        
        # Set password and ensure user has admin privileges
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created admin user with password: {password}')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully updated admin user password to: {password}')
            )
