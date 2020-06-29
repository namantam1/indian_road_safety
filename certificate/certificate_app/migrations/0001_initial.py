# Generated by Django 3.0.7 on 2020-06-28 19:37

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
                ('profile', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('upload_report', models.FileField(upload_to='media/files')),
                ('status', models.CharField(choices=[('A', 'Approved'), ('P', 'Pending'), ('R', 'Rejected')], default='P', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(editable=False, max_length=8, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_worked_on', models.CharField(choices=[('irsc', 'IRSC'), ('intellify', 'Intellify'), ('isafe', 'iSAFE Assisst'), ('solve', 'Solve(Multiple Projects)')], max_length=15)),
                ('status', models.CharField(choices=[('V', 'Volunteer'), ('I', 'Intern')], max_length=1)),
                ('tenure', models.CharField(choices=[('1 Month', '1 month'), ('2 Month', '2 month'), ('3 Month', '3 month'), ('4 Month', '4 month'), ('5 Month', '5 month'), ('6 Month', '6 month'), ('7 Month', '7 month'), ('8 Month', '8 month'), ('9 Month', '9 month'), ('10 Month', '10 month'), ('11 Month', '11 month'), ('12 Month', '12 month')], max_length=10)),
                ('joining_data', models.DateField()),
                ('end_date', models.DateField()),
                ('upload_traker_link', models.URLField()),
                ('mentor_or_leader', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProfileChoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph_contact_no', models.CharField(max_length=12)),
                ('whatsapp_no', models.CharField(max_length=12)),
                ('project', models.CharField(choices=[('irsc', 'IRSC'), ('intellify', 'Intellify'), ('isafe', 'iSAFE Assisst'), ('solve', 'Solve(Multiple Projects)')], max_length=15)),
                ('type_of_internship', models.CharField(choices=[('wfh', 'work from home'), ('wfo', 'wrok from office')], max_length=15)),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('pan_number', models.CharField(max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
                ('emergency_contact_no', models.CharField(max_length=12)),
                ('bank_account_no', models.CharField(max_length=15)),
                ('ifsc_code', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('permanent_address', models.TextField()),
                ('current_address', models.TextField()),
                ('biometric_id_number', models.CharField(max_length=15)),
                ('intership_tenure', models.CharField(choices=[('1 Month', '1 month'), ('2 Month', '2 month'), ('3 Month', '3 month'), ('4 Month', '4 month'), ('5 Month', '5 month'), ('6 Month', '6 month'), ('7 Month', '7 month'), ('8 Month', '8 month'), ('9 Month', '9 month'), ('10 Month', '10 month'), ('11 Month', '11 month'), ('12 Month', '12 month')], max_length=10)),
                ('resume', models.FileField(upload_to='media/resume')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.ProfileChoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('registration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='certificate_app.RegistrationNumber')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
