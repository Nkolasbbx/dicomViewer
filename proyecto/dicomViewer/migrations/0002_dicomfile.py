# Generated by Django 4.2.16 on 2024-10-02 03:50

import dicomViewer.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dicomViewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DicomFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dicom_file', models.FileField(upload_to=dicomViewer.models.dicom_directory_path, verbose_name='Archivo DICOM')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dicom_files', to='dicomViewer.usuario')),
            ],
        ),
    ]
