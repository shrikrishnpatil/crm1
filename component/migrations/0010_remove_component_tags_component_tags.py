# Generated by Django 4.2.2 on 2023-06-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0009_remove_component_tags_component_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='Tags',
        ),
        migrations.AddField(
            model_name='component',
            name='Tags',
            field=models.ManyToManyField(to='component.tag'),
        ),
    ]
