def test_unexpected_semicolon_after_create(parser):
    sql = 'create;'
    expected_error = '\r\nError 1:7\r\ncreate;\r\n      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error

def test_unexpected_semicolon_after_create_table(parser):
    sql = 'create table;'
    expected_error = '\r\nError 1:13\r\ncreate table;\r\n            ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error

def test_unexpected_semicolon_after_create_table_name(parser):
    sql = 'create table name;'
    expected_error = '\r\nError 1:18\r\ncreate table name;\r\n                 ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error

def test_unexpected_semicolon_after_create_table_name_open_parenthesis(parser):
    sql = 'create table name (;'
    expected_error = '\r\nError 1:20\r\ncreate table name (;\r\n                   ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error

def test_unexpected_semicolon_after_create_table_name_open_parenthesis_int(parser):
    sql = 'create table name (int;'
    expected_error = '\r\nError 1:23\r\ncreate table name (int;\r\n                      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error

def test_unexpected_semicolon_after_create_table_name_open_parenthesis_int_column(parser):
    sql = 'create table name (int column;'
    expected_error = '\r\nError 1:30\r\ncreate table name (int column;\r\n                             ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error