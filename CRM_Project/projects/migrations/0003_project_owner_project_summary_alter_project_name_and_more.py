# Generated by Django 4.1.7 on 2023-04-20 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_remove_project_owner_alter_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.TextField(default='', verbose_name='summary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Done', 'Done')], default='In progress', max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
