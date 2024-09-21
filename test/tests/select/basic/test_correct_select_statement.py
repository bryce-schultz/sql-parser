def test_select_correct_statement(parser):
    sql = 'select * from table where column = 1;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_select_two_correct_statements(parser):
    sql = 'select * from table where column = 1; select * from table where column = 2;'
    expected_result = '\r\nsuccess\r\n\r\n\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error