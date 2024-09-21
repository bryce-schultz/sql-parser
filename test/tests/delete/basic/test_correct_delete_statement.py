def test_correct_delete_statement(parser):
    sql = 'delete from users where id = 1;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_two_correct_delete_statements(parser):
    sql = 'delete from users where id = 1; delete from users where id = 2;'
    expected_result = '\r\nsuccess\r\n\r\n\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error