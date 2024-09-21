def test_expected_table_after_create(parser):
    sql = 'create'
    expected_error = '\r\nError 1:7\r\ncreate\r\n      ^\r\nexpected table\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_name_after_create_table(parser):
    sql = 'create table'
    expected_error = '\r\nError 1:13\r\ncreate table\r\n            ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_open_parenthesis_after_create_table_name(parser):
    sql = 'create table name'
    expected_error = '\r\nError 1:17\r\ncreate table name\r\n                ^\r\nexpected (\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_type_after_create_table_name_open_parenthesis(parser):
    sql = 'create table name ('
    expected_error = '\r\nError 1:18\r\ncreate table name (\r\n                 ^\r\nexpected a type\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_column_name_after_create_table_name_open_parenthesis_type(parser):
    sql = 'create table name (type'
    expected_error = '\r\nError 1:23\r\ncreate table name (type\r\n                      ^\r\nexpected a column name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_close_parenthesis_after_create_table_name_open_parenthesis_type_column_name(parser):
    sql = 'create table name (type column'
    expected_error = '\r\nError 1:29\r\ncreate table name (type column\r\n                            ^\r\nexpected )\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_create_table_name_open_parenthesis_type_column_name_close_parenthesis(parser):
    sql = 'create table name (type column)'
    expected_error = '\r\nError 1:30\r\ncreate table name (type column)\r\n                             ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_create_before_table_name(parser):
    sql = 'create before table name'
    expected_error = '\r\nError 1:7\r\ncreate before table name\r\n      ^\r\nexpected table\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_create_before_table_name_semicolon(parser):
    sql = 'create before table name;'
    expected_error = '\r\nError 1:7\r\ncreate before table name;\r\n      ^\r\nexpected table\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error