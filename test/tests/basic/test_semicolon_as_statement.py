def test_semicolon_as_statement(parser):
    sql = ';'
    expected_error = 'Error 1:1\r\n;\r\n^\r\nunexpected ;\r\n\r\n'

    result, error = parser.parse(sql)

    print('result')
    print(result)
    print('error')
    print(error)
    print('expected_error')
    print(expected_error)

    assert result == ''
    assert error == expected_error