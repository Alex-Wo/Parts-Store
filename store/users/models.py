from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True, verbose_name='код верификации')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    expiration = models.DateTimeField(verbose_name='истекает')

    class Meta:
        verbose_name = 'код верификации'
        verbose_name_plural = 'коды верификации'

    def __str__(self):
        return f'Код верификации для {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учётной записи для {self.user.username}'
        message = 'Для подтверждения учётной записи {} перейдите по ссылке: {}'.format(
            self.user.email, verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False
