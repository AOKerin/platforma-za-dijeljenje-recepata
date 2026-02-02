from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Category, Recipe, Tip
from django.db import transaction
import random


CATEGORIES = [
    "Deserti",
    "Glavna jela",
    "Juhe",
    "Vegetarijanska jela",
    "Brza hrana",
    "Zdrava prehrana",
]

RECIPES = [
    {
        "title": "Palačinke s čokoladom",
        "description": "Klasične domaće palačinke mekane teksture, idealne za doručak ili desert.",
        "ingredients": "Brašno, mlijeko, jaja, šećer, sol, čokoladni namaz",
        "tip": "Tijesto ostavite da odstoji 15 minuta prije pečenja kako bi palačinke bile mekše."
    },
    {
        "title": "Špageti bolognese",
        "description": "Tradicionalno talijansko jelo s bogatim mesnim umakom.",
        "ingredients": "Špageti, mljeveno meso, rajčica, luk, češnjak, maslinovo ulje",
        "tip": "Umak kuhajte na laganoj vatri barem 30 minuta za bolji okus."
    },
    {
        "title": "Povrtna juha",
        "description": "Lagana i zdrava juha od svježeg povrća.",
        "ingredients": "Mrkva, krumpir, celer, luk, sol, papar",
        "tip": "Povrće narežite na jednake komade kako bi se ravnomjerno skuhalo."
    },
    {
        "title": "Salata od slanutka",
        "description": "Brza i hranjiva salata bogata proteinima.",
        "ingredients": "Slanutak, rajčica, krastavac, maslinovo ulje, limun",
        "tip": "Dodajte svježi peršin ili bosiljak za dodatnu aromu."
    },
    {
        "title": "Domaći hamburger",
        "description": "Sočan burger pripremljen kod kuće.",
        "ingredients": "Mljeveno meso, pecivo, sir, salata, rajčica",
        "tip": "Meso nemojte previše gnječiti kako bi burger ostao sočan."
    },
]


class Command(BaseCommand):
    help = "Generira testne podatke (kategorije, recepte i savjete)."

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Brisanje starih podataka...")
        Tip.objects.all().delete()
        Recipe.objects.all().delete()
        Category.objects.all().delete()

        user, created = User.objects.get_or_create(username="demo")
        if created:
            user.set_password("demo12345")
            user.save()

        self.stdout.write("Stvaranje kategorija...")
        categories = [Category.objects.create(name=name) for name in CATEGORIES]

        self.stdout.write("Stvaranje recepata i savjeta...")
        for r in RECIPES:
            recipe = Recipe.objects.create(
                title=r["title"],
                description=r["description"],
                ingredients=r["ingredients"],
                category=random.choice(categories),
                author=user
            )
            Tip.objects.create(recipe=recipe, content=r["tip"])

        self.stdout.write(self.style.SUCCESS("Testni podaci su generirani. Korisnik: demo / demo12345"))
