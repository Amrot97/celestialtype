"""
Management command to check template settings.
"""
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from django.template import engines


class Command(BaseCommand):
    help = 'Check template settings and directories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Checking template settings...'))
        
        # Check TEMPLATES setting
        self.stdout.write(f"TEMPLATES setting: {settings.TEMPLATES}")
        
        # Check template directories
        for template_setting in settings.TEMPLATES:
            self.stdout.write(f"\nTemplate backend: {template_setting['BACKEND']}")
            self.stdout.write(f"DIRS: {template_setting['DIRS']}")
            
            # Check if directories exist
            for directory in template_setting['DIRS']:
                exists = os.path.exists(directory)
                self.stdout.write(f"  - {directory}: {'EXISTS' if exists else 'DOES NOT EXIST'}")
                
                # If exists, list template files
                if exists:
                    files = os.listdir(directory)
                    self.stdout.write(f"    Files: {', '.join(files)}")
        
        # Check template engines
        self.stdout.write("\nTemplate engines:")
        for engine in engines.all():
            self.stdout.write(f"  - {engine.__class__.__name__}")
            if hasattr(engine, 'dirs'):
                self.stdout.write(f"    Dirs: {engine.dirs}")
        
        # Try to find specific templates
        self.stdout.write("\nSearching for specific templates:")
        template_names = ['endpoints.html', 'home.html', '404.html', '500.html']
        for template_name in template_names:
            for engine in engines.all():
                try:
                    template = engine.get_template(template_name)
                    self.stdout.write(f"  - {template_name}: FOUND in {engine.__class__.__name__}")
                    if hasattr(template, 'origin') and hasattr(template.origin, 'name'):
                        self.stdout.write(f"    Path: {template.origin.name}")
                except Exception as e:
                    self.stdout.write(f"  - {template_name}: NOT FOUND in {engine.__class__.__name__} ({str(e)})") 