from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Books

@receiver(post_save, sender=Books)
def post_save_book(sender, instance, created, **kwargs):
    if created:
        print(f"Post created {instance.title}")
    else:
        print(f"Post updated {instance.title}")



'''
- **@receiver(post_save, sender=Books):** Ye decorator function `post_save_book` ko `post_save` signal ke receiver ke roop me register karta hai jab `Books` model ka instance save hota hai.
   - **post_save_book(sender, instance, created, **kwargs):** Ye function signal receiver function hai jo signal trigger hone par execute hota hai.
     - **sender:** Ye signal ko send karne wala model class hai. Is case me ye `Books` model hai.
     - **instance:** Ye model ka actual instance hai jo save ho raha hai.
     - **created:** Ye boolean flag hai jo indicate karta hai ki instance naya create hua hai (True) ya update hua hai (False).
     - **kwargs:** Ye additional arguments hain jo signal ke sath pass ho sakte hain.
'''