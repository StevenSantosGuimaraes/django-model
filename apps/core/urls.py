from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('folha-pagamento/', views.folha_pagamento_view, name='folha_pagamento'),
]