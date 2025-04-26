from django.db.models import Sum
from django.shortcuts import render

import json

from .forms import FiltroFolhaForm
from .models import FolhaPagamento


def folha_pagamento_view(request):

    form = FiltroFolhaForm(request.GET or None)
    queryset = FolhaPagamento.objects.all()

    if form.is_valid():

        departamentos = form.cleaned_data.get('departamentos')
        centros_custo = form.cleaned_data.get('centros_custo')
        competencia_inicio = form.cleaned_data.get('competencia_inicio')
        competencia_fim = form.cleaned_data.get('competencia_fim')

        if departamentos:
            queryset = queryset.filter(funcionario__departamento__in=departamentos)
        if centros_custo:
            queryset = queryset.filter(funcionario__centro_custo__in=centros_custo)
        if competencia_inicio:
            queryset = queryset.filter(competencia__gte=competencia_inicio)
        if competencia_fim:
            queryset = queryset.filter(competencia__lte=competencia_fim)

    dados = (
        queryset
        .values('competencia')
        .annotate(total_pago=Sum('valor_pago'))
        .order_by('competencia')
    )

    competencias = [d['competencia'].strftime('%Y-%m') for d in dados]
    totais = [float(d['total_pago']) for d in dados]

    context = {
        'form': form,
        'competencias': json.dumps(competencias),
        'totais': json.dumps(totais),
    }

    return render(request, 'folha_pagamento.html', context)
