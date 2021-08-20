from datetime import datetime
from decimal import Decimal
from logging import basicConfig, getLogger, INFO

from amazon.ion.simple_types import IonPyBool, IonPyBytes, IonPyDecimal, IonPyDict, IonPyFloat, IonPyInt, IonPyList, \
    IonPyNull, IonPySymbol, IonPyText, IonPyTimestamp
from amazon.ion.simpleion import dumps, loads

logger = getLogger(__name__)
basicConfig(level=INFO)
IonValue = (IonPyBool, IonPyBytes, IonPyDecimal, IonPyDict, IonPyFloat, IonPyInt, IonPyList, IonPyNull, IonPySymbol,
            IonPyText, IonPyTimestamp)


class SampleData:

    CREDIT = [
        {
            'PersonId': '1',
            'CreditNumber': '2720993981312698',
            'CurrentAvailableAmount': '2683.32',
            'ExpiryTimeOfCredit': datetime(2025, 11, 15)
        },
        {
            'PersonId': '2',
            'CreditNumber': '5388911127338035',
            'CurrentAvailableAmount': '234221.39',
            'ExpiryTimeOfCredit': datetime(2023, 11, 15)
        },
        {
            'PersonId': '3',
            'CreditNumber': '5369340347790028',
            'CurrentAvailableAmount': '1223.44',
            'ExpiryTimeOfCredit': datetime(2022, 10, 15)
        }
    ]
    PERSON = [
        {
            'PersonName': 'Raul Gonzaliz',
            'CreditNumber': '2720993981312698',
            'CurrentAvailableAmount': '2683.32',
            'Address': '1719 University Street, Seattle, WA, 98109',
            'DOB': datetime(1963, 8, 19)
        },
        {
            'PersonName': 'Logan Brent',
            'CreditNumber': '5388911127338035',
            'CurrentAvailableAmount': '234221.39',
            'DOB': datetime(1967, 7, 3),
            'Address': '43 Stockert Hollow Road, Everett, WA, 98203'
        },
        {
            'PersonName': 'Alexis Pena',
            'CreditNumber': '5369340347790028',
            'CurrentAvailableAmount': '1223.44',
            'DOB': datetime(1974, 2, 10),
            'Address': '4058 Melrose Street, Spokane Valley, WA, 99206'
        }
    ]
    USER_REGISTRATION = [
        {
            'PersonName': 'Raul Gonzaliz',
            'CreditNumber': '2720993981312698',
            'ExpiryTimeOfCredit': datetime(2025, 11, 15)
        },
        {
            'PersonName': 'Logan Brent',
            'CreditNumber': '5388911127338035',
            'ExpiryTimeOfCredit': datetime(2023, 11, 29)
        },
        {
            'PersonName': 'Alexis Pena',
            'CreditNumber': '5369340347790028',
            'ExpiryTimeOfCredit': datetime(2022, 10, 15)
        }
    ]


def convert_object_to_ion(py_object):
    ion_object = loads(dumps(py_object))
    return ion_object


def to_ion_struct(key, value):
    ion_struct = dict()
    ion_struct[key] = value
    return loads(str(ion_struct))


def get_document_ids(transaction_executor, table_name, field, value):
    query = "SELECT id FROM {} AS t BY id WHERE t.{} = '{}'".format(table_name, field, value)
    cursor = transaction_executor.execute_statement(query)
    return list(map(lambda table: table.get('id'), cursor))


def get_document_ids_from_dml_results(result):
    ret_val = list(map(lambda x: x.get('documentId'), result))
    return ret_val


def print_result(cursor):
    result_counter = 0
    for row in cursor:
        # Each row would be in Ion format.
        logger.info(dumps(row, binary=False, indent='  ', omit_version_marker=True))
        result_counter += 1
    return result_counter
