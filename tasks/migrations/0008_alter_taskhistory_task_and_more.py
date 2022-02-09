# Generated by Django 4.0.1 on 2022-02-08 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_taskhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskhistory',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.task'),
        ),
        migrations.AlterUniqueTogether(
            name='taskhistory',
            unique_together={('task', 'old_status', 'new_status', 'updated_date')},
        ),
        migrations.RemoveField(
            model_name='taskhistory',
            name='user',
        ),
    ]
