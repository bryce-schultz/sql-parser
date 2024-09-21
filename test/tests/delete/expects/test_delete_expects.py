def test_expected_from_after_delete(parser):
    sql = 'delete'
    expected_error = '\r\nError 1:8\r\ndelete\r\n       ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_from(parser):
    sql = 'delete from'
    expected_error = '\r\nError 1:13\r\ndelete from\r\n            ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_where_after_delete_from_table(parser):
    sql = 'delete from users'
    expected_error = '\r\nError 1:19\r\ndelete from users\r\n                  ^\r\nexpected where\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_field_after_delete_from_table_where(parser):
    sql = 'delete from users where'
    expected_error = '\r\nError 1:25\r\ndelete from users where\r\n                        ^\r\nexpected a field name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_operator_after_delete_from_table_where_field(parser):
    sql = 'delete from users where field'
    expected_error = '\r\nError 1:31\r\ndelete from users where field\r\n                              ^\r\nexpected an operator\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_value_after_delete_from_table_where_field_operator(parser):
    sql = 'delete from users where field ='
    expected_error = '\r\nError 1:33\r\ndelete from users where field =\r\n                                ^\r\nexpected a value\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_delete_from_table_where_field_operator_value(parser):
    sql = 'delete from users where field = 1'
    expected_error = '\r\nError 1:34\r\ndelete from users where field = 1\r\n                                 ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_before(parser):
    sql = 'delete before'
    expected_error = '\r\nError 1:8\r\ndelete before\r\n       ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_before_from(parser):
    sql = 'delete before from'
    expected_error = '\r\nError 1:8\r\ndelete before from\r\n       ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_before_from_table(parser):
    sql = 'delete before from table'
    expected_error = '\r\nError 1:8\r\ndelete before from table\r\n       ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_delete_before_from_table_semicolon(parser):
    sql = 'delete before from table;'
    expected_error = '\r\nError 1:8\r\ndelete before from table;\r\n       ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error