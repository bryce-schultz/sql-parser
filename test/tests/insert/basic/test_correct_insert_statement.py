def test_correct_insert_statement_one_column(parser):
    sql = 'insert into users (id) values (0);'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_correct_insert_statement(parser):
    sql = 'insert into users (id, name) values (0, "john");'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_two_correct_insert_statements(parser):
    sql = 'insert into users (id, name) values (0, "john"); insert into users (id, name) values (1, "doe");'
    expected_result = '\r\nsuccess\r\n\r\n\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error