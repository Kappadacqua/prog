# Generated by Django 4.1.7 on 2023-03-01 16:40

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('nome', models.CharField(blank=True, max_length=50)),
                ('cognome', models.CharField(blank=True, max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=10)),
                ('citta', models.CharField(blank=True, max_length=50)),
                ('indirizzo', models.CharField(blank=True, max_length=100)),
                ('codice_postale', models.CharField(blank=True, max_length=5)),
                ('punti', models.PositiveIntegerField(default=0, editable=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Utenti',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]