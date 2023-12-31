# Generated by Django 4.2.2 on 2023-06-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0004_rename_users_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagid', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='tags',
            new_name='compid',
        ),
    ]
