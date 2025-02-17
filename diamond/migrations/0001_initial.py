# Generated by Django 4.1.6 on 2024-03-13 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accountprofile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(default='true.jpg', upload_to='user/')),
                ('bankname', models.CharField(default='', max_length=200)),
                ('bankacc', models.CharField(default='', max_length=100)),
                ('accountname', models.CharField(default='', max_length=100)),
                ('points', models.CharField(default=1, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('referral_code', models.CharField(default='RDXVY', max_length=6)),
                ('is_published', models.BooleanField(default=True)),
                ('package', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accountprofile.package')),
                ('referree', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accountprofile.referral')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
