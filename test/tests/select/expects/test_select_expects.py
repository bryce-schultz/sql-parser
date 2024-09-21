def test_expected_star_after_select(parser):
    sql = 'select'
    expected_error = '\r\nError 1:8\r\nselect\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_from_after_select_star(parser):
    sql = 'select *'
    expected_error = '\r\nError 1:10\r\nselect *\r\n         ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_table_after_select_star_from(parser):
    sql = 'select * from'
    expected_error = '\r\nError 1:15\r\nselect * from\r\n              ^\r\nexpected a table name\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_where_after_select_star_from_table(parser):
    sql = 'select * from users'
    expected_error = '\r\nError 1:21\r\nselect * from users\r\n                    ^\r\nexpected where\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_field_after_select_star_from_table_where(parser):
    sql = 'select * from users where'
    expected_error = '\r\nError 1:27\r\nselect * from users where\r\n                          ^\r\nexpected a field name\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_operator_after_select_star_from_table_where_field(parser):
    sql = 'select * from users where field'
    expected_error = '\r\nError 1:33\r\nselect * from users where field\r\n                                ^\r\nexpected an operator\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_value_after_select_star_from_table_where_field_operator(parser):
    sql = 'select * from users where field ='
    expected_error = '\r\nError 1:35\r\nselect * from users where field =\r\n                                  ^\r\nexpected a value\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_semicolon_after_select_star_from_table_where_field_operator_value(parser):
    sql = 'select * from users where field = 1'
    expected_error = '\r\nError 1:36\r\nselect * from users where field = 1\r\n                                   ^\r\nexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table(parser):
    sql = 'select from users'
    expected_error = '\r\nError 1:8\r\nselect from users\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where(parser):
    sql = 'select from users where'
    expected_error = '\r\nError 1:8\r\nselect from users where\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where_field(parser):
    sql = 'select from users where field'
    expected_error = '\r\nError 1:8\r\nselect from users where field\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where_field_operator(parser):
    sql = 'select from users where field ='
    expected_error = '\r\nError 1:8\r\nselect from users where field =\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where_field_operator_value(parser):
    sql = 'select from users where field = 1'
    expected_error = '\r\nError 1:8\r\nselect from users where field = 1\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where_field_operator_value_semicolon(parser):
    sql = 'select from users where field = 1;'
    expected_error = '\r\nError 1:8\r\nselect from users where field = 1;\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_star_after_select_from_table_where_field_operator_value_semicolon_select_star_from_table(parser):
    sql = 'select from users where field = 1; select * from users'
    expected_error = '\r\nError 1:8\r\nselect from users where field = 1; select * from users\r\n       ^\r\nexpected *\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_from_after_select_star_before_table_name(parser):
    sql = 'select * users'
    expected_error = '\r\nError 1:10\r\nselect * users\r\n         ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_from_after_select_star_before_table_name_semicolon(parser):
    sql = 'select * users;'
    expected_error = '\r\nError 1:10\r\nselect * users;\r\n         ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_expected_from_after_select_star_before_table_name_semicolon_select_star_from_table(parser):
    sql = 'select * users; select * from users'
    expected_error = '\r\nError 1:10\r\nselect * users; select * from users\r\n         ^\r\nexpected from\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error