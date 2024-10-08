def test_invalid_type_in_create_statement(parser):
    sql = 'create table users (not-a-type);'
    expected_error = '\r\nError 1:21\r\ncreate table users (not-a-type);\r\n                    ^\r\ninvalid type\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)

    assert result == ''
    assert error == expected_error