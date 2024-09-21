def test_correct_drop_statement(parser):
    sql = 'drop table name;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_two_correct_drop_statements(parser):
    sql = 'drop table name; drop table name2;'
    expected_result = '\r\nsuccess\r\n\r\n\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error