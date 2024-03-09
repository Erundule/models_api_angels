from datetime import datetime

def is_field_empty(field):
    if field is None:
        return True
    else:
        return False

def is_not_integer_field(value):
    try:
        value = int(value)
        return False
    except ValueError:
        return True

def is_not_valid_date(date1, date2):
    try:
        date1 = datetime.fromisoformat(date1)
        date2 = datetime.fromisoformat(date2)
        return False
    except ValueError:
        return True

def is_previous_weight_valid(previous_weight):
    if is_field_empty(previous_weight):
        return False
    
    try:
        previous_weight_numeric = float(previous_weight)

        if previous_weight_numeric < 0:
            return False

        return True
    except ValueError:
        return False

def is_gestational_risk_valid(gestational_risk):
    if is_field_empty(gestational_risk) or is_not_integer_field(gestational_risk):
        return False
    
    gestational_risk_numeric = int(gestational_risk)

    if 0 <= gestational_risk_numeric <= 2:
        return True
    
    return False

def is_schooling_valid(education):
    if is_field_empty(education) or is_not_integer_field(education):
        return False
        
    education_numeric = int(education)

    if 0 <= education_numeric <= 8:
        return True
    
    return False

def is_field_binary(category):
    if is_field_empty(category) or is_not_integer_field(category):
        return False

    category_numeric = int(category)

    if category_numeric == 0 or category_numeric == 1:
        return True

    return False

def is_field_non_negative_integer(category):
    if is_field_empty(category) or is_not_integer_field(category):
        return False

    category_numeric = int(category)

    is_non_negative_integer = category_numeric >= 0

    if is_non_negative_integer:
        return True

    return False

def is_age_valid(birth_date, first_prenatal_date):
    if is_field_empty(birth_date) or is_field_empty(first_prenatal_date) or is_not_valid_date(birth_date, first_prenatal_date):
        return False
    
    birth_date = datetime.fromisoformat(birth_date)
    first_prenatal_date = datetime.fromisoformat(first_prenatal_date)

    age = abs((int)((birth_date - first_prenatal_date).days / 365))

    return age

def is_first_prenatal_valid(pregnancy_start_date, first_prenatal_date):
    if is_field_empty(pregnancy_start_date) or is_field_empty(first_prenatal_date) or is_not_valid_date(pregnancy_start_date, first_prenatal_date):
        return False
    
    pregnancy_start_date = datetime.fromisoformat(pregnancy_start_date)
    first_prenatal_date = datetime.fromisoformat(first_prenatal_date)

    weeks_count = abs((int)((pregnancy_start_date - first_prenatal_date).days / 7))

    return weeks_count

def is_time_between_pregnancies_valid(pregnancy_start_date, last_delivery_date):
    if last_delivery_date is None:
        return -1
    
    if is_field_empty(pregnancy_start_date) or is_not_valid_date(pregnancy_start_date, last_delivery_date):
        return False
    
    pregnancy_start_date = datetime.fromisoformat(pregnancy_start_date)
    last_delivery_date = datetime.fromisoformat(last_delivery_date)

    months_count = abs((int)((pregnancy_start_date - last_delivery_date).days / 30))

    if months_count > 12:
        months_count = 12
    
    return months_count

def data_validation(json_data):

    """
    Esta função retorna um número representando um erro específico que pode ser causado por problemas nas entradas
    recebidas do gateway. Caso não haja erros, ela retorna um dicionário com 3 dados computados.

    Parâmetros:
    - json_data: Um dicionário contendo dados a serem validados.

    Retorno:
    - Um número representando o tipo de erro, ou um dicionário com dados calculados se não houver erros.
    """

    dict_dados_calculados_por_datas = {}

    try:
        schooling = json_data['schooling']
        previous_weight = json_data['previous_weight']
        gestacional_risc = json_data['gestational_risk']
        has_hypertension = json_data['has_hypertension'] #checar pra ver isso aqui pq talvez n tenha has_
        has_diabetes = json_data['has_diabetes']
        has_pelvic_surgery = json_data['has_pelvic_surgery']
        has_urinary_infection = json_data['has_urinary_infection']
        has_congenital_malformation = json_data['has_congenital_malformation']
        has_family_twinship = json_data['has_family_twinship']
        amount_gestation = json_data['amount_gestation']
        amount_abortion = json_data['amount_abortion']
        amount_deliveries = json_data['amount_deliveries']
        amount_cesarean  = json_data['amount_cesarean']
        data_nascimento = json_data['data_nascimento']
        data_inicio_gestacao = json_data['data_inicio_gestacao'] #checar pra ver se de fato é assim q a data vem
        first_prenatal = json_data['first_prenatal'] #checar se vem assim também
        data_ultimo_parto = json_data['data_ultimo_parto'] #checar pra ver se vem assim
    except KeyError:
        return 17
    

    if is_previous_weight_valid(previous_weight) is False:
        return 1
    
    if is_gestational_risk_valid(gestacional_risc) is False:
        return 2
    
    if is_schooling_valid(schooling) is False:
        return 3
    
    if is_field_binary(has_hypertension) is False:
        return 4
    
    if is_field_binary(has_diabetes) is False:
        return 5
    
    if is_field_binary(has_pelvic_surgery) is False:
        return 6
    
    if is_field_binary(has_urinary_infection) is False:
        return 7
    
    if is_field_binary(has_congenital_malformation) is False:
        return 8
    
    if is_field_binary(has_family_twinship) is False:
        return 9
    
    if is_field_non_negative_integer(amount_gestation) is False:
        return 10
    
    if is_field_non_negative_integer(amount_abortion) is False:
        return 11
    
    if is_field_non_negative_integer(amount_deliveries) is False:
        return 12
    
    if is_field_non_negative_integer(amount_cesarean) is False:
        return 13
    
    if is_age_valid(data_nascimento, data_inicio_gestacao) is False:
        return 14
    else:
        idade = is_age_valid(data_nascimento, data_inicio_gestacao)
        dict_dados_calculados_por_datas['idade'] = idade

    if is_first_prenatal_valid(data_inicio_gestacao, data_primeiro_prenatal) is False:
        return 15
    else:
        quantidade_semanas_pre_natal = is_first_prenatal_valid(data_inicio_gestacao, data_primeiro_prenatal)
        dict_dados_calculados_por_datas['quantidade_semanas_pre_natal'] = quantidade_semanas_pre_natal
    
    if is_time_between_pregnancies_valid(data_inicio_gestacao, data_ultimo_parto) is False:
        return 16
    else:
        quantidade_meses_entre_gravidezes = is_time_between_pregnancies_valid(data_inicio_gestacao, data_ultimo_parto)
        dict_dados_calculados_por_datas['quantidade_meses_entre_gravidezes'] = quantidade_meses_entre_gravidezes

    return dict_dados_calculados_por_datas #retornar mais coisas
