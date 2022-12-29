from django.db import models
from django.urls import reverse

# Create your models here.
class IncomingMail(models.Model):
    id_enter = models.CharField(max_length=200, null=True)  # No Surat Asal

    date_enter = models.DateField(null=True)  # Tanggal Surat Asal
    id_enter = models.CharField(max_length=200)  # No Surat Asal
    # no
    id_mail = models.CharField(max_length=200)  # No Surat Asal
    date = models.DateField()  # Tanggal Surat Asal
    sender = models.CharField(max_length=200)  # Pengirim
    regarding = models.TextField()  # Perihal
    file_or_image = models.FileField(
        upload_to="storage/incoming-mail/", null=True, blank=True
    )  # Foto

    def __str__(self):
        return f"{self.id_mail} {self.regarding}"

    def get_absolute_url(self):
        return reverse("incoming-mail-list")

    class Meta:
        ordering = ("-date_enter",)

    def filename(self):
        import os

        return os.path.basename(self.file_or_image.name)


class OutgoingMail(models.Model):
    # No
    id_mail = models.CharField(max_length=100)  # No Surat
    date = models.DateField()  # Tanggal Surat
    to_send = models.CharField(max_length=100)  # Kepada
    regarding = models.CharField(max_length=100)  # Perihal
    code = models.CharField(max_length=100)  # Kode
    file_or_image = models.FileField(
        upload_to="storage/outgoing-mail/", null=True, blank=True
    )  # Foto / File

    def __str__(self):
        return f"{self.id_mail} {self.regarding}"

    def get_absolute_url(self):
        return reverse("outgoing-mail-list")

    class Meta:
        ordering = ("-date",)

    def filename(self):
        import os

        return os.path.basename(self.file_or_image.name)
