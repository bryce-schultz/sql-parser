def test_correct_create_statement_one_column(parser):
    sql = 'create table users (int id);'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_correct_create_statement(parser):
    sql = 'create table users (int id, string name);'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_two_correct_create_statements(parser):
    sql = 'create table users (int id, string name); create table users2 (int id, string name);'
    expected_result = '\r\nsuccess\r\n\r\n\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error