# Generated by Django 4.1.7 on 2023-04-26 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_price_alter_project_partner'),
        ('tasks', '0002_usertask_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_task', to='projects.project'),
        ),
    ]
