from shop_online.models import Animale, Prodotto


def erase_db():
    print("Cancello il DB")

    Prodotto.objects.all().delete()
    Animale.objects.all().delete()


def init_db():
    categorie_animali = ["cane", "gatto", "roditore", "uccello", "pesce"]

    for e in categorie_animali:
        a = Animale()
        a.animale = e
        a.save()

    qs_an = Animale.objects.all()

    prodotti_dizionario = {
        "nome_prodotto": ["croccantini", "scatolette", "pallina", "antiparassitario", "roba"],
    }

    for i in qs_an.iterator():
        for e in prodotti_dizionario:
            a = Prodotto()
            a.animale = i
            a.nome = prodotti_dizionario[e]
            a.save()

    print("DUMP DB")
    print(Animale.objects.all())
