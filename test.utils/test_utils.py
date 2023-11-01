from develop import utils

def test_get_data():
    assert len(utils.get_data('operations.json')) > 0


def test_get_operations_executed(test_data):
    assert len(utils.get_operations_executed(test_data)) == 2


def test_get_last_operations(test_data):
    assert len(utils.get_last_operations(test_data, 4)) == 4
    assert utils.get_last_operations(test_data, 4)[0]['date'] == "2023-07-03T18:35:29.512364"


def test_get_operations_formatted():
    last_operations = ['\n'
                       '            03-07-2023 Перевод организации\n'
                       '            MasterCard 7158 30** ****6758->Счет **5560\n'
                       '            8221.37 USD\n'
                       '            '] != ['\n'
                                           '        03-07-2023 Перевод организации\n'
                                           '        MasterCard 7158** ****6758->Счет 3538** ****5560\n'
                                           '        8221.37 USD\n'
                                           '        ']





