# Generated by Django 3.2.8 on 2021-10-16 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TechCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tech Categories',
                'db_table': 'Tech Category',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=70)),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_children', to='resources.techcategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_technology_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_technology_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'verbose_name': 'Technologies',
                'db_table': 'Technology',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('difficulty', models.PositiveSmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Advanced')], default=0)),
                ('cost', models.PositiveSmallIntegerField(choices=[(0, 'Free'), (1, 'Paid')], default=1)),
                ('link', models.URLField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_material_set', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='resources.technology')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_material_set', to=settings.AUTH_USER_MODEL, verbose_name='Updated By')),
            ],
            options={
                'db_table': 'Material',
            },
        ),
    ]