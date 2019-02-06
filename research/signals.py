from django.db.models.signals import post_save
from django.dispatch import receiver
from research.models.subject import Subject


@receiver(post_save, sender="django_dicom.Patient")
def save_subject(sender, instance, **kwargs):
    existing_ids = Subject.objects.values_list("id_number", flat=True).all()
    if instance.patient_id not in existing_ids:
        subject_attributes = instance.get_subject_attributes()
        new_subject = Subject(**subject_attributes)
        new_subject.save()
        instance.subject = new_subject
        instance.save()
