# Generated by Django 4.2.4 on 2023-08-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_image',
            field=models.FileField(null=True, upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
    ]
