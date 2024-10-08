#include <iostream>
#include <string>

#include "Parser.h"
#include "SqlSemanticChecker.h"

using namespace SQL;

#define SUCCESS return { true, "", { COLOR_GREEN + "\nsuccess\n" + COLOR_RESET } }

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

	return { false, result.error };
}

ParseResult Parser::parseStatements()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { true };
	}

	Args args;

	auto result = parseStatement();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	result = parseStatements();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	return { true, "", args };
}

ParseResult Parser::parseStatement()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
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

	return { false, _tokenizer.getErrorString("unrecognized statement " + token, 1) };
}

// select
ParseResult Parser::parseSelect()
{
	auto token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}
		
	if (token != "select")
	{
		return { false, expected("select") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}
	
	if (token != "*")
	{
		return { false, expected("*") };
	}

	// select *
	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "from")
	{
		return { false, expected("from") };
	}

	// select * from table
	auto result = parseFrom();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token == ";")
	{
		_tokenizer.next();
		SUCCESS;
	}

	if (token != "where")
	{
		return { false, expected("where") };
	}

	// select * from table where
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

	// select * from table where field operator value ;
	_tokenizer.next();

	SUCCESS;
}

ParseResult Parser::parseInsert()
{
	auto token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "insert")
	{
		return { false, expected("insert") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "into")
	{
		return { false, expected("into") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	auto semantic_check = SQL::globals::table_name_is_not_keyword_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "(")
	{
		return { false, expected("(") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a column name") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto result = parseIdentifierList();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != ")")
	{
		return { false, expected(")") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "values")
	{
		return { false, expected("values") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "(")
	{
		return { false, expected("(") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token.empty())
	{
		return { false, expected("a value") };
	}

	result = parseValueList();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != ")")
	{
		return { false, expected(")") };
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token != ";")
	{
		return { false, expected(";") };
	}

	_tokenizer.next();

	SUCCESS;
}

ParseResult Parser::parseUpdate()
{
	return { false, _tokenizer.getWarningString("Unimplemented", 1) };
}

ParseResult Parser::parseDelete()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("delete") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "delete")
	{
		return { false, expected("delete") };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
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
		SUCCESS;
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
		_tokenizer.next();
		return { false, expected(";") };
	}

	_tokenizer.next();

	SUCCESS;
}

ParseResult Parser::parseCreate()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("create") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "create")
	{
		return { false, expected("create") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("table") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "table")
	{
		return { false, expected("table") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto semantic_check = SQL::globals::table_name_is_not_keyword_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	token = _tokenizer.next();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "(")
	{
		return { false, expected("(") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a type") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto result = parseSchema();

	if (!result.success)
	{
		return { false, result.error };
	}

	token = _tokenizer.peek();

	if (token != ")")
	{
		return { false, expected(")") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	token = _tokenizer.peek();

	if (token != ";")
	{
		return { false, expected(";") };
	}

	_tokenizer.next();

	SUCCESS;
}

ParseResult Parser::parseDrop()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("drop") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "drop")
	{
		return { false, expected("drop") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("table") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != "table")
	{
		return { false, expected("table") };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	token = _tokenizer.next();

	if (token != ";")
	{
		_tokenizer.next();
		return { false, expected(";") };
	}

	_tokenizer.next();

	SUCCESS;
}

ParseResult Parser::parseFrom()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("from") };
	}

	if (token != "from")
	{
		return { false, expected("from")};
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a table name") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto semantic_check = SQL::globals::table_name_is_not_keyword_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	std::string table_name = token;

	_tokenizer.next();

	return { true, "", { table_name } };
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

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a field name") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("an operator") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected("a value") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	_tokenizer.next();

	return { true, "", { token } };
}

ParseResult SQL::Parser::parseSchema()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a type") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	Args args;

	auto result = parseScheme();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token == ")")
	{
		return { true, "", result.args };
	}

	if (token != ",")
	{
		return { false, expected(",") };
	}

	_tokenizer.next();

	result = parseSchema();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	return { true, "", args };
}

ParseResult SQL::Parser::parseScheme()
{
	auto result = parseType();

	if (!result.success)
	{
		return { false, result.error };
	}

	if (result.args.empty())
	{
		return { false, devError("parseType must return a value if it succeeds!") };
	}

	std::string type = result.args[0];

	auto token = _tokenizer.peek();

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token.empty())
	{
		return { false, expected("a column name") };
	}

	if (token == ")")
	{
		return { false, expected("a column name") };
	}

	auto semantic_check = SQL::globals::invalid_identifier_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	std::string column_name = token;

	token = _tokenizer.next();

	return { true, "", { type, column_name } };
}

ParseResult SQL::Parser::parseIdentifierList()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("an identifier") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto semantic_check = SQL::globals::invalid_identifier_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	Args args;

	args.push_back(token);

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected(",") };
	}

	if (token == ")")
	{
		return { true, "", args };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != ",")
	{
		return { false, expected(",") };
	}

	token = _tokenizer.next();

	auto result = parseIdentifierList();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	return { true, "", args };
}

ParseResult SQL::Parser::parseValueList()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a value") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	Args args;

	args.push_back(token);

	token = _tokenizer.next();

	if (token.empty())
	{
		return { false, expected(",") };
	}

	if (token == ")")
	{
		return { true, "", args };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	if (token != ",")
	{
		return { false, expected(",") };
	}

	token = _tokenizer.next();

	auto result = parseValueList();

	if (!result.success)
	{
		return { false, result.error };
	}

	for (const auto &arg : result.args)
	{
		args.push_back(arg);
	}

	return { true, "", args };
}

ParseResult SQL::Parser::parseType()
{
	auto token = _tokenizer.peek();

	if (token.empty())
	{
		return { false, expected("a type") };
	}

	if (token == ";")
	{
		return { false, unexpectedSemicolon() };
	}

	auto semantic_check = SQL::globals::type_is_valid_semantic_check.check(token);

	if (!semantic_check.success)
	{
		return { false, semanticError(semantic_check.error) };
	}

	std::string type = token;

	_tokenizer.next();

	return { true, "", { type } };
}

std::string Parser::unexpectedSemicolon()
{
	const int desired_space = 2;

	int whitespace = _tokenizer.getTrailingspace();
	if (!_tokenizer.peek().empty())
	{
		const int non_empty_space = 1;
		whitespace = non_empty_space;
	}

	return _tokenizer.getErrorString("unexpected ;", desired_space - whitespace);
}

std::string Parser::expected(const std::string &expected)
{
	int desired_space = 2;

	// Add custom spacing for certain tokens here
	if (
		expected == ";" || 
		expected == ")" ||
		expected == ",")
	{
		desired_space = 1;
	}

	std::string previous_token = _tokenizer.getPreviousToken();

	if (previous_token == "(")
	{
		desired_space = 1;
	}

	int whitespace = _tokenizer.getTrailingspace();
	if (!_tokenizer.peek().empty())
	{
		const int non_empty_space = 1;
		whitespace = non_empty_space;
	}

	return _tokenizer.getErrorString("expected " + expected, desired_space - whitespace);
}

std::string SQL::Parser::semanticError(const std::string &message)
{
	return _tokenizer.getErrorString(message, 1);
}

std::string SQL::Parser::devError(const std::string &message)
{
	return _tokenizer.getErrorString("[DEV] " + message);
}
