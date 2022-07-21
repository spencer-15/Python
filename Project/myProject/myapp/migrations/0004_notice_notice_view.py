# Generated by Django 4.0.6 on 2022-07-13 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pic', models.FileField(null=True, upload_to='media/images/')),
                ('video', models.FileField(null=True, upload_to='media/video/')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='notice_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_at', models.DateTimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.notice')),
            ],
        ),
    ]
