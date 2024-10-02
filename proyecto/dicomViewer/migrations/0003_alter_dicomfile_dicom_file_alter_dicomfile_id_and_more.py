# Generated by Django 4.2.16 on 2024-10-02 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dicomViewer', '0002_dicomfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dicomfile',
            name='dicom_file',
            field=models.FileField(upload_to='dicom_files/'),
        ),
        migrations.AlterField(
            model_name='dicomfile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dicomfile',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
