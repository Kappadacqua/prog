from django.shortcuts import render, get_object_or_404

from django.views.decorators.http import require_POST

from negozio_animali.account.models import CustomUser
from ordini.models import Order


@require_POST
def crea_ordine(request):

    user = get_object_or_404(CustomUser, username=request.user)
    print(request.POST.get("data-secret"))




    return render(request, "ordini/")


def history(request):

    ctx = {"ordini": Order.objects.get(user_id=request.user.id)}
    print(ctx)

    #return render(request, template_name="ordini/history.html", context=ctx)
