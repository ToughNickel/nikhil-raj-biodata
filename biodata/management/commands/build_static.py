"""
Management command to build a static version of the biodata site.

Usage:
    python manage.py build_static

Generates a self-contained static site in the `_site/` directory
that can be deployed to GitHub Pages or any static host.
"""
import os
import shutil

from django.conf import settings
from django.core.management.base import BaseCommand
from django.test import RequestFactory

from biodata.views import HomeView


class Command(BaseCommand):
    help = 'Build a static HTML version of the site for GitHub Pages deployment'

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        output_dir = os.path.join(base_dir, '_site')

        # Clean previous build
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.makedirs(output_dir)

        # ── 1. Render the homepage ──
        self.stdout.write('Rendering homepage...')
        factory = RequestFactory()
        request = factory.get('/')
        response = HomeView.as_view()(request)
        response.render()
        html = response.content.decode('utf-8')

        # Fix static file URLs to be relative (for GitHub Pages sub-path)
        html = html.replace('/static/', './static/')

        # Write index.html
        index_path = os.path.join(output_dir, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)
        self.stdout.write(self.style.SUCCESS(f'  → {index_path}'))

        # ── 2. Copy static files ──
        self.stdout.write('Copying static files...')
        static_src = os.path.join(base_dir, 'static')
        static_dst = os.path.join(output_dir, 'static')
        shutil.copytree(static_src, static_dst)

        # Remove non-web files from the build
        for root, dirs, files in os.walk(static_dst):
            for f in files:
                if f.lower().endswith(('.heic', '.ds_store')):
                    os.remove(os.path.join(root, f))
                    self.stdout.write(f'  Removed non-web file: {f}')

        self.stdout.write(self.style.SUCCESS(f'  → {static_dst}'))

        # ── 3. Copy .nojekyll for GitHub Pages ──
        nojekyll_path = os.path.join(output_dir, '.nojekyll')
        with open(nojekyll_path, 'w') as f:
            pass
        self.stdout.write(self.style.SUCCESS(f'  → {nojekyll_path}'))

        # ── Done ──
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✓ Static site built successfully in _site/'))
        self.stdout.write(f'  Files: index.html + static assets')
        self.stdout.write(f'  Ready for GitHub Pages deployment!')
