import input_data_validation as input

def main(): 
    test_data_functional = {
    'previous_weight': '65.5',
    'gestacional_risk': '0',
    'schooling': '3',
    'has_arterial_hypertension': 1,
    'has_diabetes': 0,
    'has_cirurgia_pelvica': 0,
    'has_infeccao_urinaria': 1,
    'has_malformacao_familiar': 1,
    'has_gemelaridade_familiar': 0,
    'quant_gest': 2,
    'quant_aborto': 0,
    'quant_partos': 1,
    'quant_partos_cesarios': 0,
    'data_nascimento': '2001-04-12T14:17:37Z',
    'data_inicio_gestacao': '2021-04-12T14:17:37Z',
    'data_primeiro_prenatal': '2021-06-12T14:17:37Z',
    'data_ultimo_parto': '2019-04-12T14:17:37Z',
}
    test_data_error_dates = {
    'previous_weight': '65.5',
    'gestacional_risk': '0',
    'schooling': '3',
    'has_arterial_hypertension': 1,
    'has_diabetes': 0,
    'has_cirurgia_pelvica': 0,
    'has_infeccao_urinaria': 1,
    'has_malformacao_familiar': 1,
    'has_gemelaridade_familiar': 0,
    'quant_gest': 2,
    'quant_aborto': 0,
    'quant_partos': 1,
    'quant_partos_cesarios': 0,
    'data_nascimento': '2001-:17:37Z',
    'data_inicio_gestacao': '2021-04-12T14:17:37Z',
    'data_primeiro_prenatal': '2021-06-12T14:17:37Z',
    'data_ultimo_parto': '2019-04-12T14:17:37Z',
}
    test_data_error_false_instead_of_0 = {
    'previous_weight': '65.5',
    'gestacional_risk': '0',
    'schooling': '3',
    'has_arterial_hypertension': 1,
    'has_diabetes': 0,
    'has_cirurgia_pelvica': False,
    'has_infeccao_urinaria': False,
    'has_malformacao_familiar': True,
    'has_gemelaridade_familiar': 0,
    'quant_gest': 2,
    'quant_aborto': 0,
    'quant_partos': 1,
    'quant_partos_cesarios': 0,
    'data_nascimento': '2001-04-12T14:17:37Z',
    'data_inicio_gestacao': '2021-04-12T14:17:37Z',
    'data_primeiro_prenatal': '2021-06-12T14:17:37Z',
    'data_ultimo_parto': '2019-04-12T14:17:37Z',
}

    print(input.data_validation(test_data_functional))
    print(input.data_validation(test_data_error_dates))
    print(input.data_validation(test_data_error_false_instead_of_0))


    
main()