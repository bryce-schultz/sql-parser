def test_expected_table_after_drop(parser):
    sql = 'drop'
    expected_error = 'Error 1:5\r\ndrop\r\n    ^\r\nexpected table\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_name_after_drop_table(parser):
    sql = 'drop table'
    expected_error = 'Error 1:11\r\ndrop table\r\n          ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_drop_table_name(parser):
    sql = 'drop table name'
    expected_error = 'Error 1:16\r\ndrop table name\r\n               ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error