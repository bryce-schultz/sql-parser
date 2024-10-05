def test_semicolon_after_insert(parser):
    sql = 'insert;'
    expected_result = ''
    expected_error = '\r\nError 1:7\r\ninsert;\r\n      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into(parser):
    sql = 'insert into;'
    expected_result = ''
    expected_error = '\r\nError 1:12\r\ninsert into;\r\n           ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table(parser):
    sql = 'insert into users;'
    expected_result = ''
    expected_error = '\r\nError 1:18\r\ninsert into users;\r\n                 ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis(parser):
    sql = 'insert into users (;'
    expected_result = ''
    expected_error = '\r\nError 1:19\r\ninsert into users (;\r\n                  ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name(parser):
    sql = 'insert into users (id;'
    expected_result = ''
    expected_error = '\r\nError 1:21\r\ninsert into users (id;\r\n                    ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis(parser):
    sql = 'insert into users (id);'
    expected_result = ''
    expected_error = '\r\nError 1:22\r\ninsert into users (id);\r\n                     ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values(parser):
    sql = 'insert into users (id) values;'
    expected_result = ''
    expected_error = '\r\nError 1:29\r\ninsert into users (id) values;\r\n                            ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis(parser):
    sql = 'insert into users (id) values (;'
    expected_result = ''
    expected_error = '\r\nError 1:30\r\ninsert into users (id) values (;\r\n                             ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis_value(parser):
    sql = 'insert into users (id) values (1;'
    expected_result = ''
    expected_error = '\r\nError 1:32\r\ninsert into users (id) values (1;\r\n                               ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_insert_into_table_open_parenthesis_column_name_close_parenthesis_values_open_parenthesis_value_close_parenthesis(parser):
    sql = 'insert into users (id) values (1);'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error