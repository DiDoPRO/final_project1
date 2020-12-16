# Generated by Django 3.1.2 on 2020-12-10 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a food type (e.g. Asian)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TableInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imprint', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Food availability', max_length=1)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.table')),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the food', max_length=1000)),
                ('Cost', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='Cost')),
                ('Type', models.ManyToManyField(help_text='Select a type for this food', to='catalog.Type')),
            ],
        ),
    ]
