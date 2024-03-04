# Só vou deixar um código prévio pra checagem básica das coisas que o professor botou
from datetime import datetime


def campo_nao_preenchido(campo):
    if campo is None:
        return True
    else:
        return False


def campo_nao_e_inteiro(valor):
    try:
        valor = int(valor)
        return False
    except ValueError:
        return True


def data_nao_e_valida(data1, data2):
    try:
        data1 = datetime.fromisoformat(data1)
        data2 = datetime.fromisoformat(data2)
        return False
    except ValueError:
        return True


def checar_peso_anterior_valido(peso_anterior):
    if (campo_nao_preenchido(peso_anterior)):
        return False

    try:
        resultado = float(peso_anterior)
        return True
    except ValueError:
        return False


def checar_se_risco_gestacional_valido(risco_gestacional):
    if (campo_nao_preenchido(risco_gestacional) or campo_nao_e_inteiro(risco_gestacional)):
        return False

    risco_gestacional_numerico = int(risco_gestacional)

    if (risco_gestacional_numerico >= 0) and risco_gestacional_numerico <= 2:
        return True

    return False


def checar_se_escolaridade_valido(escolaridade):
    if (campo_nao_preenchido(escolaridade) or campo_nao_e_inteiro(escolaridade)):
        return False

    escolaridade_numeric = int(escolaridade)

    if (escolaridade_numeric >= 0 and escolaridade_numeric <= 8):
        is_escolaridade_valido = True

    return False


def checar_se_categoria_e_binaria(categoria):
    if (campo_nao_preenchido(categoria) or campo_nao_e_inteiro(categoria)):
        return False

    categoria_numeric = int(categoria)

    if (categoria_numeric == 0 or categoria_numeric == 1):
        return True

    return False


def checar_se_categoria_e_inteira_positiva(categoria):
    if (campo_nao_preenchido(categoria) or campo_nao_e_inteiro(categoria)):
        return False

    categoria_numeric = int(categoria)

    categoria_e_inteiro_positivo = categoria_numeric >= 0

    if (categoria_e_inteiro_positivo):
        return True

    return False


def idade_e_valida(data_nascimento, data_primeiro_pre_natal):  # checa se a idade é valida e se for, retorna a idade
    if (campo_nao_preenchido(data_nascimento) or campo_nao_preenchido(data_primeiro_pre_natal) or data_nao_e_valida(
            data_nascimento, data_primeiro_pre_natal)):
        return False

    data_nascimento = datetime.fromisoformat(data_nascimento)
    data_primeiro_pre_natal = datetime.fromisoformat(data_primeiro_pre_natal)

    idade = abs((int)((data_nascimento - data_primeiro_pre_natal).days / 365))

    return idade


def primeiro_pre_natal_valido(data_inicio_gestacao,
                              data_primeiro_pre_natal):  # checa se é valido e se for retorna qntd de semanas
    if (campo_nao_preenchido(data_inicio_gestacao) or campo_nao_preenchido(
            data_primeiro_pre_natal) or data_nao_e_valida(data_inicio_gestacao, data_primeiro_pre_natal)):
        return False

    data_inicio_gestacao = datetime.fromisoformat(data_inicio_gestacao)
    data_primeiro_pre_natal = datetime.fromisoformat(data_primeiro_pre_natal)

    quantidadeSemanas = abs((int)((data_inicio_gestacao - data_primeiro_pre_natal).days / 7))

    return quantidadeSemanas


def semanas_entre_gravidezes_valido(data_inicio_gestacao,
                                    data_ultimo_parto):  # checa se é valido e se for retorna qntd de semanas
    if (data_ultimo_parto is None):
        return -1

    if (campo_nao_preenchido(data_inicio_gestacao) or data_nao_e_valida(data_inicio_gestacao, data_ultimo_parto)):
        return False

    data_inicio_gestacao = datetime.fromisoformat(data_inicio_gestacao)
    data_ultimo_parto = datetime.fromisoformat(data_ultimo_parto)

    quantidadeMeses = abs((int)((data_inicio_gestacao - data_ultimo_parto).days / 30))

    if (quantidadeMeses > 12):
        quantidadeMeses = 12

    return quantidadeMeses
