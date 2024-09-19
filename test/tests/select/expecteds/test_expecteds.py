def test_expected_star_after_select(parser):
    sql = 'select'
    expected_error = 'Error 1:7\r\nselect\r\n      ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_from_after_select_star(parser):
    sql = 'select *'
    expected_error = 'Error 1:9\r\nselect *\r\n        ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_select_star_from(parser):
    sql = 'select * from'
    expected_error = 'Error 1:14\r\nselect * from\r\n             ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_where_after_select_star_from_table(parser):
    sql = 'select * from table'
    expected_error = 'Error 1:20\r\nselect * from table\r\n                   ^\r\nexpected where\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_field_after_select_star_from_table_where(parser):
    sql = 'select * from table where'
    expected_error = 'Error 1:26\r\nselect * from table where\r\n                         ^\r\nexpected a field name\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_operator_after_select_star_from_table_where_field(parser):
    sql = 'select * from table where field'
    expected_error = 'Error 1:32\r\nselect * from table where field\r\n                               ^\r\nexpected an operator\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_value_after_select_star_from_table_where_field_operator(parser):
    sql = 'select * from table where field ='
    expected_error = 'Error 1:34\r\nselect * from table where field =\r\n                                 ^\r\nexpected a value\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_select_star_from_table_where_field_operator_value(parser):
    sql = 'select * from table where field = 1'
    expected_error = 'Error 1:36\r\nselect * from table where field = 1\r\n                                   ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error