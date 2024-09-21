def test_semicolon_after_drop(parser):
    sql = 'drop;'
    expected_error = 'Error 1:5\r\ndrop;\r\n    ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_drop_table(parser):
    sql = 'drop table;'
    expected_error = 'Error 1:10\r\ndrop table;\r\n          ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_drop_table_name(parser):
    sql = 'drop table name;'
    expected_error = 'Error 1:15\r\ndrop table name;\r\n              ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_drop_table_name_semicolon(parser):
    sql = 'drop table name;'
    expected_result = 'success\r\n'
    expected_error = 'Error 1:15\r\ndrop table name;\r\n              ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error != expected_error

