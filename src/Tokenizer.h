#pragma once

#include <string>
#include <vector>
#include <map>

extern const std::string COLOR_RED;
extern const std::string COLOR_RESET;
extern const std::string COLOR_GREEN;
extern const std::string COLOR_LIGHT_GREY;
extern const std::string COLOR_YELLOW;
extern const std::string COLOR_BLUE;
extern const std::string DECORATION_BOLD;
extern const std::string DECORATION_STRIKETHROUGH;

extern std::string COLOR_RGB(int r, int g, int b);

namespace SQL
{
	enum class ErrorLevel
	{
		INFO,
		WARNING,
		ERROR
	};

	class Tokenizer
	{
	public:
		Tokenizer();
		Tokenizer(const std::string &input, const std::string &filename = "");

		std::string peek();
		std::string next();

		int getTrailingspace() const;
		std::string getPreviousToken() const;

		std::string getErrorString(const std::string &message = "", int additional_space = 0);
		std::string getWarningString(const std::string &message = "", int additional_space = 0);
		std::string getInfoString(const std::string &message = "", int additional_space = 0);
	private:
		std::string getLevelString(ErrorLevel level, const std::string &message, int additional_space);
		void consumeRestOfLine();
	private:
		std::string _filename;
		std::string _original_input;
		std::string _input;
		std::string _token;
		std::string _previous_token;
		std::string _current_line;

		int _trailingspace;

		int _lineno;
		int _column;
	};
}

