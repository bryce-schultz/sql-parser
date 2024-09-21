#pragma once

#include <string>

extern const std::string COLOR_RED;
extern const std::string COLOR_RESET;
extern const std::string COLOR_GREEN;
extern const std::string DECORATION_STRIKETHROUGH;

extern std::string COLOR_RGB(int r, int g, int b);

namespace SQL
{
	class Tokenizer
	{
	public:
		Tokenizer();
		Tokenizer(const std::string &input, const std::string &filename = "");

		std::string peek();
		std::string next();

		int getTrailingspace() const;

		std::string getErrorString(const std::string &message = "", int additional_space = 0);
	private:
		std::string _filename;
		std::string _original_input;
		std::string _input;
		std::string _token;
		std::string _current_line;

		int _trailingspace;

		int _lineno;
		int _column;
	};
}

