from django.db import models

class GuestbookEntry(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    author_name = models.CharField(max_length=255, verbose_name="Имя автора")
    author_email = models.EmailField(verbose_name="Почта автора")
    text = models.TextField(verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время редактирования")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Статус",
    )

    def __str__(self):
        return f"{self.author_name} - {self.status}"
