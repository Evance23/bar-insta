# Generated by Django 3.2.9 on 2022-02-23 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0002_auto_20220223_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['-pk']},
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='image',
            new_name='post',
        ),
        migrations.AddField(
            model_name='comments',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
