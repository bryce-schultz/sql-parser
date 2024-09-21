def test_semicolon_after_drop(parser):
    sql = 'drop;'
    expected_error = '\r\nError 1:5\r\ndrop;\r\n    ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_drop_table(parser):
    sql = 'drop table;'
    expected_error = '\r\nError 1:11\r\ndrop table;\r\n          ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_drop_table_name(parser):
    sql = 'drop table name;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error
