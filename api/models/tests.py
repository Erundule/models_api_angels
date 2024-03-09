import data_validation as dv
import data_treatment as dt
import prediction_model as pm

def test(data):

    if(dv.data_validation(data) is not True):
        return dv.data_validation(data)
    
    treated_data = dt.data_treatment(data)
    pm.predict_test([treated_data])

def main(): 

    test_data_valid = {
        'schooling': '6',
        'previous_weight': '65.5',
        'gestational_risk': '1',
        'has_hypertension': '1',
        'has_diabetes': '0',
        'has_pelvic_surgery': '0',
        'has_urinary_infection': '1',
        'has_congenital_malformation': '0',
        'has_family_twinship': '1',
        'amount_gestation': '2',
        'amount_abortion': '1',
        'amount_deliveries': '2',
        'amount_cesarean': '1',
        'mothers_birth_date': '1990-05-15',
        'date_start_pregnancy': '2023-01-01',
        'date_first_prenatal': '2023-01-10',
        'date_last_delivery': '2023-12-20'
    }

    test_data_invalid = {
        'schooling': '-1',  # Invalid schooling level
        'previous_weight': '-65.5',  # Negative weight
        'gestational_risk': '3',  # Invalid gestational risk
        'has_hypertension': '2',  # Invalid binary value
        'has_diabetes': '3',  # Invalid binary value
        'has_pelvic_surgery': '1',
        'has_urinary_infection': '0',
        'has_congenital_malformation': '2',  # Invalid binary value
        'has_family_twinship': '0',
        'amount_gestation': '-1',  # Negative value
        'amount_abortion': 'abc',  # Non-integer value
        'amount_deliveries': '2',
        'amount_cesarean': '1',
        'mothers_birth_date': '1990-05-15',
        'date_start_pregnancy': '2023-01-01',
        'date_first_prenatal': '2023-01-10',
        'date_last_delivery': '2023-12-20'
    }

    test_data_missing = {
        'schooling': '6',
        'previous_weight': '65.5',
        'gestational_risk': '1',
        'has_hypertension': '1',
        'has_diabetes': '0',
        'has_pelvic_surgery': '0',
        'has_urinary_infection': '1',
        'has_congenital_malformation': '0',
        'has_family_twinship': '1',
        'amount_gestation': '2',
        'amount_abortion': '1',
        'amount_deliveries': '2',
        'amount_cesarean': '1',
        'mothers_birth_date': '1990-05-15',
        # Missing date_start_pregnancy
        # Missing date_first_prenatal
        # Missing date_last_delivery
    }

    print(test(test_data_valid))
    print(test(test_data_invalid))
    print(test(test_data_missing))

main()
