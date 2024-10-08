def test_table_name_is_not_keyword_select(parser):
    sql = 'select * from select;'
    expected_error = '\r\nError 1:15\r\nselect * from select;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_insert(parser):
    sql = 'select * from insert;'
    expected_error = '\r\nError 1:15\r\nselect * from insert;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_delete(parser):
    sql = 'select * from delete;'
    expected_error = '\r\nError 1:15\r\nselect * from delete;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_update(parser):
    sql = 'select * from update;'
    expected_error = '\r\nError 1:15\r\nselect * from update;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_create(parser):
    sql = 'select * from create;'
    expected_error = '\r\nError 1:15\r\nselect * from create;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_drop(parser):
    sql = 'select * from drop;'
    expected_error = '\r\nError 1:15\r\nselect * from drop;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_from(parser):
    sql = 'select * from from;'
    expected_error = '\r\nError 1:15\r\nselect * from from;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_where(parser):
    sql = 'select * from where;'
    expected_error = '\r\nError 1:15\r\nselect * from where;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_table(parser):
    sql = 'select * from table;'
    expected_error = '\r\nError 1:15\r\nselect * from table;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error

def test_table_name_is_not_keyword_like(parser):
    sql = 'select * from like;'
    expected_error = '\r\nError 1:15\r\nselect * from like;\r\n              ^\r\ntable name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error