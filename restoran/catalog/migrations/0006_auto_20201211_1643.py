# Generated by Django 3.1.2 on 2020-12-11 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_tableinstance_imprint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Type',
        ),
        migrations.AddField(
            model_name='food',
            name='Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.type'),
        ),
    ]
