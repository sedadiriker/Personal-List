
from .models import Personal
from .serializer import PersonalSerializer
from rest_framework import viewsets
from .tasks import send_email_task

# Create your views here.


class PersonalViewset(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

    def perform_create(self, serializer):
        personal = serializer.save()

        send_email_task.delay(
            subject="Yeni Personel Eklendi",
            message=f"""
        Yeni personel eklendi:

        Ad: {personal.firstname}
        Soyad: {personal.lastname}
        Email: {personal.email}
        Pozisyon: {personal.position}
        """,
            from_email="Personel Listesi",
            recipient_list=[personal.email]
        )
