#Só vou deixar um código prévio pra checagem básica das coisas que o professor botou
from datetime import datetime

def campo_nao_preenchido(campo):
    if campo is None:
        return True
    else:
        return False

def checar_peso_anterior_valido(peso_anterior):
    if(campo_nao_preenchido(peso_anterior)):
        return False
    
    try:
        resultado = float(peso_anterior)
        return True
    except ValueError:
        return False

def checar_risco_gestacional_valido(risco_gestacional):
    if(campo_nao_preenchido(risco_gestacional)):
        return False
    try:
        is_risco_gestacional_valido = False
        risco_gestacional_numerico = int(risco_gestacional)

        if(risco_gestacional_numerico <= 2 and risco_gestacional_numerico >= 0):
            is_risco_gestacional_valido = True

        return is_risco_gestacional_valido

    except ValueError:
        return False

def checar_escolaridade_valido(escolaridade):
    if(campo_nao_preenchido(escolaridade)):
        return False
    try:
        is_escolaridade_valido = False
        escolaridade_numeric = int(escolaridade)

        if(escolaridade_numeric <= 8 and escolaridade_numeric >= 0):
            is_escolaridade_valido = True
        
        return is_escolaridade_valido

    except ValueError:
        return False

def checar_se_categoria_e_binaria(categoria):
    if(campo_nao_preenchido(categoria)):
        return False
    try:
        is_categoria_binario = False

        categoria_numeric = int(categoria)

        if(categoria_numeric == 0 or categoria_numeric == 1):
            is_categoria_binario = True

        return is_categoria_binario

    except ValueError:
        return False

def checar_se_categoria_e_inteira_positiva(categoria):
    if(campo_nao_preenchido(categoria)):
        return False
    try:
        is_inteira_positiva = False

        categoria_numeric = int(categoria)

        if(categoria_numeric >= 0):
            is_inteira_positiva = True

        return is_inteira_positiva
    
    except ValueError:
        return False

def idade_e_valida(data_nascimento, data_primeiro_pre_natal): #checa se a idade é valida e se for, retorna a idade
    if(campo_nao_preenchido(data_nascimento) and campo_nao_preenchido(data_primeiro_pre_natal)):
        return False
    
    try:
        data_nascimento = datetime.fromisoformat(data_nascimento)
        data_primeiro_pre_natal = datetime.fromisoformat(data_primeiro_pre_natal)
    except ValueError:
        return False

    idade = abs((int)((data_nascimento - data_primeiro_pre_natal).days/365))

    return idade 

def primeiro_pre_natal_valido(data_inicio_gestacao, data_primeiro_pre_natal):#checa se é valido e se for retorna qntd de semanas
    if(campo_nao_preenchido(data_inicio_gestacao) and campo_nao_preenchido(data_primeiro_pre_natal)):
        return False
    
    try:
        data_inicio_gestacao = datetime.fromisoformat(data_inicio_gestacao)
        data_primeiro_pre_natal = datetime.fromisoformat(data_primeiro_pre_natal)
    except ValueError:
        return False

    quantidadeSemanas = abs((int)((data_inicio_gestacao - data_primeiro_pre_natal).days/7))

    return quantidadeSemanas

def semanas_entre_gravidezes_valido(data_inicio_gestacao, data_ultimo_parto):#checa se é valido e se for retorna qntd de semanas
    if(campo_nao_preenchido(data_inicio_gestacao)):
        return False
    
    if(data_ultimo_parto is None):
        return -1
    
    try:
        data_inicio_gestacao = datetime.fromisoformat(data_inicio_gestacao)
        data_ultimo_parto = datetime.fromisoformat(data_ultimo_parto)
    except ValueError:
        return False

    quantidadeMeses = abs((int)((data_inicio_gestacao - data_ultimo_parto).days/30))

    if(quantidadeMeses > 12):
        quantidadeMeses = 12
    
    return quantidadeMeses

