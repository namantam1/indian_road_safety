# Generated by Django 3.0.7 on 2020-07-02 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectWorkedChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_worked', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='StatusChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='TenureChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenure', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfInternChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_intern', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=500)),
                ('upload_report', models.FileField(upload_to='media/files')),
                ('status', models.CharField(choices=[('A', 'Approved'), ('P', 'Pending'), ('R', 'Rejected')], default='P', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(editable=False, max_length=225, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_date', models.DateField()),
                ('end_date', models.DateField()),
                ('upload_traker_link', models.URLField()),
                ('mentor_or_leader', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProfileChoice')),
                ('project_worked_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProjectWorkedChoice')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.StatusChoice')),
                ('tenure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.TenureChoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_contact_no', models.CharField(max_length=15)),
                ('whatsapp_no', models.CharField(max_length=15)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('pan_number', models.CharField(max_length=20)),
                ('aadhaar', models.CharField(max_length=20)),
                ('emergency_contact_no', models.CharField(max_length=15)),
                ('bank_account_no', models.CharField(max_length=20)),
                ('ifsc_code', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('permanent_address', models.TextField()),
                ('current_address', models.TextField()),
                ('biometric_id_number', models.CharField(max_length=225)),
                ('resume', models.FileField(upload_to='media/resume')),
                ('internship_tenure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.TenureChoice')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProfileChoice')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProjectWorkedChoice')),
                ('type_of_internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.TypeOfInternChoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('certificate_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
