# Generated by Django 5.1.1 on 2024-10-11 06:34

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField()),
                ('event_status', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feed_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_name', models.CharField(max_length=200)),
                ('rtsp_link', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='FeedPolygon',
            fields=[
                ('polygon_id', models.AutoField(primary_key=True, serialize=False)),
                ('polygon_name', models.CharField(max_length=255)),
                ('feed_polygons', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=2), size=5)),
                ('polygon_color', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=3)),
                ('feeds', models.ManyToManyField(related_name='feed_polygons', to='config_app.feed')),
            ],
        ),
    ]
