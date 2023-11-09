from develop import utils
from develop.utils import get_operations_formatted

def test_get_data():
    data = utils.get_data('operations.json')
    assert len(data) > 0
    assert isinstance(data, list)
    assert all(isinstance(operation, dict) for operation in data)

def test_get_operations_executed(test_data):
    executed_operations = utils.get_operations_executed(test_data)
    assert len(executed_operations) == 2
    assert all(operation['state'] == 'EXECUTED' for operation in executed_operations)

def test_get_last_operations(test_data):
    last_operations = utils.get_last_operations(test_data, 4)
    assert len(last_operations) == 4
    assert all(isinstance(operation, dict) for operation in last_operations)
    dates = [operation['date'] for operation in last_operations]
    assert dates == sorted(dates, reverse=True)


def test_get_operations_formatted(test_data):
    last_operations = [
        {
            "date": "2023-07-03T18:35:29.512364",
            "description": "Перевод организации",
            "from": "MasterCard 7158 30** ****6758",
            "to": "Счет **5560",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD"}}
        }
    ]
    expected_result = [
        '03-07-23 Перевод организации\nMasterCard 7158** ****6758->Счет 3538** ****5560\n8221.37 USD\n'
    ]
    print(get_operations_formatted(last_operations))

def test_example(test_data):
    assert len(test_data) == 4
    assert test_data[0]["state"] == "CANCELED"
