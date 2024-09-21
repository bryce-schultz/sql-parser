#pragma once
#include <string>
#include <vector>

#include "Tokenizer.h"

namespace SQL
{
	typedef std::vector<std::string> Args;

	struct ParseResult
	{
		bool success      { false };
		std::string error { "" };
		Args args		  {};
	};

	class Parser
	{
	public:
		Parser();
		ParseResult parse(const std::string &input);

	private:
		Tokenizer _tokenizer;
		ParseResult parseStatements();
		ParseResult parseStatement();

		ParseResult parseSelect();
		ParseResult parseInsert();
		ParseResult parseUpdate();
		ParseResult parseDelete();
		ParseResult parseCreate();
		ParseResult parseDrop();

		ParseResult parseFrom();
		ParseResult parseWhere();
		ParseResult parseSchema();
		ParseResult parseScheme();

		ParseResult parseType();

		std::string unexpectedSemicolon();
		std::string expected(const std::string &expected);
		std::string semanticError(const std::string &message);
		std::string devError(const std::string &message);
	};
}
