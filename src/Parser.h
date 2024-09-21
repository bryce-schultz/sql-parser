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
		// void parseFile(const std::string &filename);

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

		std::string unexpectedSemicolon();
		std::string expected(const std::string &expected);
		std::string semanticError(const std::string &message);
	};
}
