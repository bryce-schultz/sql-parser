def test_semicolon_after_delete(parser):
    sql = 'delete;'
    expected_error = '\r\nError 1:7\r\ndelete;\r\n      ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_delete_from(parser):
    sql = 'delete from;'
    expected_error = '\r\nError 1:12\r\ndelete from;\r\n           ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_delete_from_table(parser):
    sql = 'delete from users;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error

def test_semicolon_after_delete_from_table_where(parser):
    sql = 'delete from users where;'
    expected_error = '\r\nError 1:24\r\ndelete from users where;\r\n                       ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_delete_from_table_where_field(parser):
    sql = 'delete from users where id;'
    expected_error = '\r\nError 1:27\r\ndelete from users where id;\r\n                          ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_delete_from_table_where_field_operator(parser):
    sql = 'delete from users where id =;'
    expected_error = '\r\nError 1:29\r\ndelete from users where id =;\r\n                            ^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == ''
    assert error == expected_error

def test_semicolon_after_delete_from_table_where_field_operator_value(parser):
    sql = 'delete from users where id = 1;'
    expected_result = '\r\nsuccess\r\n\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error