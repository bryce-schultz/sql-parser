def test_column_name_is_not_a_keyword_in_create_statement(parser):
    sql = 'create table users (int create;'
    expected_result = ''
    expected_error = '\r\nError 1:25\r\ncreate table users (int create;\r\n                        ^\r\ncolumn name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(expected_result)
    print(error)
    print(expected_error)

    assert result == expected_result
    assert error == expected_error

def test_column_name_is_not_a_keyword_in_insert_statement(parser):
    sql = 'insert into users (create);'
    expected_result = ''
    expected_error = '\r\nError 1:20\r\ninsert into users (create);\r\n                   ^\r\ncolumn name cannot be a keyword\r\n\r\n'

    result, error = parser.parse(sql)

    print(result)
    print(expected_result)
    print(error)
    print(expected_error)

    assert result == expected_result
    assert error == expected_error