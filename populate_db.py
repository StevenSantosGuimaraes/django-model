import django, os, sys

from django.utils import timezone

from datetime import datetime
from decimal import Decimal


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


def populate_db():

    from apps.core.models import Departamento, CentroCusto, Funcionario, FolhaPagamento

    Departamento.objects.all().delete()
    CentroCusto.objects.all().delete()
    Funcionario.objects.all().delete()
    FolhaPagamento.objects.all().delete()

    ti = Departamento.objects.create(nome="TI")
    rh = Departamento.objects.create(nome="RH")
    financeiro = Departamento.objects.create(nome="Financeiro")

    cc1 = CentroCusto.objects.create(codigo="CC001", descricao="Tecnologia")
    cc2 = CentroCusto.objects.create(codigo="CC002", descricao="Recursos Humanos")
    cc3 = CentroCusto.objects.create(codigo="CC003", descricao="Financeiro")

    funcionarios = [
        Funcionario(nome="Ana Silva", departamento=ti, centro_custo=cc1, salario_base=5000.00),
        Funcionario(nome="João Souza", departamento=rh, centro_custo=cc2, salario_base=4000.00),
        Funcionario(nome="Maria Oliveira", departamento=financeiro, centro_custo=cc3, salario_base=6000.00),
        Funcionario(nome="Pedro Santos", departamento=ti, centro_custo=cc1, salario_base=5500.00),
    ]
    Funcionario.objects.bulk_create(funcionarios)

    competencias = [

        datetime(2024, 1, 1),
        datetime(2024, 2, 1),
        datetime(2024, 3, 1),
        datetime(2024, 4, 1),
        datetime(2024, 5, 1),
        datetime(2024, 6, 1),
        datetime(2024, 7, 1),
        datetime(2024, 8, 1),
        datetime(2024, 9, 1),
        datetime(2024, 10, 1),
        datetime(2024, 11, 1),
        datetime(2024, 12, 1),

        datetime(2025, 1, 1),
        datetime(2025, 2, 1),
        datetime(2025, 3, 1),
        datetime(2025, 4, 1),
    ]

    folhas = []
    for func in Funcionario.objects.all():
        for comp in competencias:
            folhas.append(FolhaPagamento(
                funcionario=func,
                competencia=comp,
                valor_pago=func.salario_base * Decimal('1.1')
            ))

    FolhaPagamento.objects.bulk_create(folhas)

    print("Dados populados com sucesso!")


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()
    populate_db()
