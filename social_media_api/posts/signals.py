# posts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like, Comment
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if not created:
        return
    post = instance.post
    user = instance.user
    if post.author != user:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=str(post.pk),
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if not created:
        return
    post = instance.post
    user = instance.author
    if post.author != user:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='commented on your post',
            target_content_type=ContentType.objects.get_for_model(instance),
            target_object_id=str(instance.pk),
        )
