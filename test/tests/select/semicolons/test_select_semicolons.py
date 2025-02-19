def test_semicolon_after_select(parser):
    sql = 'select;'
    expected_error = '\r\nError 1:7\r\nselect;\r\n      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star(parser):
    sql = 'select *;'
    expected_error = '\r\nError 1:9\r\nselect *;\r\n        ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from(parser):
    sql = 'select * from;'
    expected_error = '\r\nError 1:14\r\nselect * from;\r\n             ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table(parser):
    sql = 'select * from users;'
    expectred_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expectred_result
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where(parser):
    sql = 'select * from users where;'
    expected_error = '\r\nError 1:26\r\nselect * from users where;\r\n                         ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id(parser):
    sql = 'select * from users where id;'
    expected_error = '\r\nError 1:29\r\nselect * from users where id;\r\n                            ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id_eq(parser):
    sql = 'select * from users where id =;'
    expected_error = '\r\nError 1:31\r\nselect * from users where id =;\r\n                              ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id_eq_1(parser):
    sql = 'select * from users where id = 1;'
    expected_error = ''
    expected_result = '\r\nsuccess\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error