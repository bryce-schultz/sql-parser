#pragma once

#include <string>

namespace SQL
{
	class Tokenizer
	{
	public:
		Tokenizer();
		Tokenizer(const std::string &input, const std::string &filename = "");

		std::string peek();
		std::string next();

		std::string getErrorString(const std::string &message = "", int additional_space = 0) const;
	private:
		std::string _filename;
		std::string _original_input;
		std::string _input;
		std::string _token;
		std::string _current_line;

		int _lineno;
		int _column;
	};
}

