def test_correct_delete_statement(parser):
    sql = 'delete from users where id = 1;'
    expected_result = 'success\r\n'
    expected_error = ''

    result, error = parser.parse(sql)

    print(result)
    print(error)

    assert result == expected_result
    assert error == expected_error