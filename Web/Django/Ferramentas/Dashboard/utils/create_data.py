import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice
import random
import django
from django.conf import settings


DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from dashboard.models import Produto, Vendedor, Vendas

    Produto.objects.all().delete()
    Vendedor.objects.all().delete()
    Vendas.objects.all().delete()

    fake = faker.Faker('pt_BR')

    django_produto = []
    django_Vendedor= []
    django_Vendas = []

    produtos = ['Smartphone', 'Smart TV', 'Echo Dot','Fire TV Stick','Computador', 'Chromecast', 'Placa de amplificador', 'vaporizador', 'SDD' ]

    django_produto = [Produto(nome=nome) for nome in produtos]

    for category in django_produto:
        category.save()

    for _ in range(20):
        profile = fake.profile()
        nome = profile['name']
        django_Vendedor.append(
            Vendedor(nome=nome)
        )

    if len(django_Vendedor) > 0:
        Vendedor.objects.bulk_create(django_Vendedor)

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        nome_produto = choice(django_produto)
        vendedor = choice(django_Vendedor)
        total: float = round(random.uniform(1, 5000), 2)
        created_date: datetime = fake.date_this_year()

        django_Vendas.append(
            Vendas(nome_produto=nome_produto,
                   vendedor=vendedor,
                   total=total,
                   data=created_date
                   )
        )

    if len(django_Vendedor) > 0:
        Vendas.objects.bulk_create(django_Vendas)