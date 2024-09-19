#include <iostream>

#include "Parser.h"

using namespace SQL;

Parser::Parser():
	_tokenizer()
{
}

ParseResult Parser::parse(const std::string &input)
{
	_tokenizer = Tokenizer(input);

	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { true, "" };
	}

	auto result = parseStatements();

	if (result.success)
	{
		return { true, "", result.args };
	}

	std::cerr << result.error << std::endl;

	return { false, result.error };
}

ParseResult Parser::parseStatements()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { true };
	}

	auto result = parseStatement();

	if (result.success)
	{
		return parseStatements();
	}

	return { false, result.error };
}

ParseResult Parser::parseStatement()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false };
	}

	if (token == "select")
	{
		return parseSelect();
	}
	else if (token == "insert")
	{
		return parseInsert();
	}
	else if (token == "update")
	{
		return parseUpdate();
	}
	else if (token == "delete")
	{
		return parseDelete();
	}
	else if (token == "create")
	{
		return parseCreate();
	}
	else if (token == "drop")
	{
		return parseDrop();
	}

	_tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	return { false, _tokenizer.getErrorString("unrecognized statement " + token) };
}

ParseResult Parser::parseSelect()
{
	auto token = _tokenizer.peek();

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}
		
	if (token != "select")
	{
		return { false, expected("select") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	if (token != "*")
	{
		return { false, expected("*") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	if (token != "from")
	{
		return { false, expected("from") };
	}

	auto result = parseFrom();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	if (token != "where")
	{
		return { false, expected("where") };
	}

	result = parseWhere();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token != ";")
	{
		return { false, expected(";") };
	}

	return { true, "" };
}

ParseResult Parser::parseInsert()
{
	return ParseResult();
}

ParseResult Parser::parseUpdate()
{
	return ParseResult();
}

ParseResult Parser::parseDelete()
{
	return ParseResult();
}

ParseResult Parser::parseCreate()
{
	return ParseResult();
}

ParseResult Parser::parseDrop()
{
	return ParseResult();
}

ParseResult Parser::parseFrom()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	if (token != "from")
	{
		return { false, expected("from")};
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	return { true, "", { token } };
}

ParseResult Parser::parseWhere()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a condition") };
	}

	if (token != "where")
	{
		return { false, expected("where") };
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a field name") };
	}

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("an operator") };
	}

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a value") };
	}

	if (token == ";")
	{
		_tokenizer.next();
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	return { true, "", { token } };
}

std::string Parser::unexpectedSemicolon()
{
	return _tokenizer.getErrorString("unexpected ;");
}

std::string Parser::expected(const std::string &expected)
{
	return _tokenizer.getErrorString("expected " + expected, 1);
}
