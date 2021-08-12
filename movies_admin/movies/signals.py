import datetime
from django.db.models.signals import post_save


def congratulatory(sender, instance, created, **kwargs):
    print(instance)
    print(created)
    if created and instance.birth_date == datetime.date.today():
        print(f"У {instance.full_name} сегодня день рождения! 🥳")


post_save.connect(
    receiver=congratulatory,
    sender='movies.Person',
    weak=True, dispatch_uid='congratulatory_signal'
)
