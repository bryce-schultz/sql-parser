def test_expected_into_after_insert(parser):
    sql = 'insert'
    expected_result = ''
    expected_error = '\r\nError 1:8\r\ninsert\r\n       ^\r\nexpected into\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_table_name_after_insert_into(parser):
    sql = 'insert into'
    expected_result = ''
    expected_error = '\r\nError 1:13\r\ninsert into\r\n            ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_open_parenthesis_after_insert_into_table(parser):
    sql = 'insert into users'
    expected_result = ''
    expected_error = '\r\nError 1:19\r\ninsert into users\r\n                  ^\r\nexpected (\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_column_name_after_insert_into_table_open_parenthesis(parser):
    sql = 'insert into users ('
    expected_result = ''
    expected_error = '\r\nError 1:20\r\ninsert into users (\r\n                   ^\r\nexpected a column name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_comma_after_insert_into_table_open_parenthesis_column_name(parser):
    sql = 'insert into users (id'
    expected_result = ''
    expected_error = '\r\nError 1:22\r\ninsert into users (id\r\n                     ^\r\nexpected ,\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_values_after_insert_into_table_open_parenthesis_column_name_close_parenthesis(parser):
    sql = 'insert into users (id)'
    expected_result = ''
    expected_error = '\r\nError 1:24\r\ninsert into users (id)\r\n                       ^\r\nexpected values\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_open_parenthesis_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values(parser):
    sql = 'insert into users (id) values'
    expected_result = ''
    expected_error = '\r\nError 1:31\r\ninsert into users (id) values\r\n                              ^\r\nexpected (\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_value_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis(parser):
    sql = 'insert into users (id) values ('
    expected_result = ''
    expected_error = '\r\nError 1:32\r\ninsert into users (id) values (\r\n                               ^\r\nexpected a value\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_comma_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis_value(parser):
    sql = 'insert into users (id) values (1'
    expected_result = ''
    expected_error = '\r\nError 1:33\r\ninsert into users (id) values (1\r\n                                ^\r\nexpected ,\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_expected_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis_value_close_parenthesis(parser):
    sql = 'insert into users (id) values (1)'
    expected_result = ''
    expected_error = '\r\nError 1:34\r\ninsert into users (id) values (1)\r\n                                 ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error