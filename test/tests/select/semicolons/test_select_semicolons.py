def test_semicolon_after_select(parser):
    sql = 'select;'
    expected_error = 'Error 1:7\r\nselect;\r\n      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star(parser):
    sql = 'select *;'
    expected_error = 'Error 1:9\r\nselect *;\r\n        ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from(parser):
    sql = 'select * from;'
    expected_error = 'Error 1:14\r\nselect * from;\r\n             ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table(parser):
    sql = 'select * from table;'
    expected_error = 'Error 1:20\r\nselect * from table;\r\n                   ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where(parser):
    sql = 'select * from table where;'
    expected_error = 'Error 1:26\r\nselect * from table where;\r\n                         ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id(parser):
    sql = 'select * from table where id;'
    expected_error = 'Error 1:29\r\nselect * from table where id;\r\n                            ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id_eq(parser):
    sql = 'select * from table where id =;'
    expected_error = 'Error 1:31\r\nselect * from table where id =;\r\n                              ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_select_star_from_table_where_id_eq_1(parser):
    sql = 'select * from table where id = 1;'
    expected_error = 'Error 1:33\r\nselect * from table where id = 1;\r\n                                ^\r\nunexpected ;\r\n\r\n'
    expected_result = 'success\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error != expected_error