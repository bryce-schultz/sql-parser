def test_expected_from_after_delete(parser):
    sql = 'delete'
    expected_error = 'Error 1:7\r\ndelete\r\n      ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_from(parser):
    sql = 'delete from'
    expected_error = 'Error 1:12\r\ndelete from\r\n           ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_where_after_delete_from_table(parser):
    sql = 'delete from table'
    expected_error = 'Error 1:18\r\ndelete from table\r\n                 ^\r\nexpected where\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_field_after_delete_from_table_where(parser):
    sql = 'delete from table where'
    expected_error = 'Error 1:24\r\ndelete from table where\r\n                       ^\r\nexpected a field name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_operator_after_delete_from_table_where_field(parser):
    sql = 'delete from table where field'
    expected_error = 'Error 1:30\r\ndelete from table where field\r\n                             ^\r\nexpected an operator\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_value_after_delete_from_table_where_field_operator(parser):
    sql = 'delete from table where field ='
    expected_error = 'Error 1:32\r\ndelete from table where field =\r\n                               ^\r\nexpected a value\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_delete_from_table_where_field_operator_value(parser):
    sql = 'delete from table where field = 1'
    expected_error = 'Error 1:34\r\ndelete from table where field = 1\r\n                                 ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error