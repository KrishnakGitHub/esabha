# Generated by Django 3.0.5 on 2020-06-13 05:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_name', models.CharField(max_length=200)),
                ('suggetion', models.CharField(max_length=200)),
                ('feedback', models.CharField(max_length=200)),
                ('feed_phone_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('feed_email', models.CharField(max_length=300)),
                ('feed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(null=True, upload_to='images\\')),
                ('subject', models.CharField(max_length=200)),
                ('msg', models.TextField(blank=True, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(18)])),
                ('gender', models.CharField(choices=[('female', 'FEMALE'), ('male', 'MALE'), ('other', 'OTHER')], default='None', max_length=20)),
                ('YOE', models.IntegerField(default=0, null=True)),
                ('YOP', models.IntegerField(default=0, null=True)),
                ('YOJ', models.IntegerField(default=0, null=True)),
                ('grduper', models.IntegerField(default=0, null=True)),
                ('interper', models.IntegerField(default=0, null=True)),
                ('highper', models.IntegerField(default=0, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('entrepreneur', 'ENTREPRENEUR'), ('gov employee', 'GOV EMPLOYEE'), ('private sector', 'PRIVATE SECTER'), ('higher studies', 'HIGHER STUDIES'), ('searching job', 'SEARCHING JOB')], default='None', max_length=20)),
                ('ptype', models.CharField(choices=[('alumni', 'Alumni'), ('student', 'STUDENT'), ('staff', 'STAFF')], default='None', max_length=20)),
                ('course', models.CharField(choices=[('b.Tech', 'B.TECH'), ('m.Tech', 'M.TECH'), ('phd', 'PHD'), ('bca', 'BCA'), ('mca', 'MCA')], default='None', max_length=20)),
                ('branch', models.CharField(choices=[('cse', 'CSE'), ('ece', 'ECE'), ('me', 'ME'), ('ee', 'EE'), ('civil', 'CIVIL'), ('che', 'CHE')], default='None', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('description', models.TextField(blank=True, default='none', null=True)),
                ('pic', models.ImageField(null=True, upload_to='images\\')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyPost')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(blank=True, choices=[('racist', 'racist'), ('abbusing', 'abbusing')], max_length=20, null=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyPost')),
            ],
        ),
        migrations.AddField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile'),
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='social.MyProfile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='social.MyProfile')),
            ],
        ),
    ]
