def test_invalid_statement(parser):
    sql = 'nonsense'
    expected_redult = ''
    expected_error = 'Error 1:1\r\nnonsense\r\n^\r\nunrecognized statement nonsense\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)
    print(result)

    assert result == expected_redult
    assert error == expected_error

def test_invalid_statement_with_semicolon(parser):
    sql = 'nonsense;'
    expected_redult = ''
    expected_error = 'Error 1:1\r\nnonsense;\r\n^\r\nunrecognized statement nonsense\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)
    print(result)

    assert result == expected_redult
    assert error == expected_error

def test_invalid_statement_with_semicolon_and_whitespace(parser):
    sql = 'nonsense; '
    expected_redult = ''
    expected_error = 'Error 1:1\r\nnonsense; \r\n^\r\nunrecognized statement nonsense\r\n\r\n'

    result, error = parser.parse(sql)

    print(expected_error)
    print(error)
    print(result)

    assert result == expected_redult
    assert error == expected_error