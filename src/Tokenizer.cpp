#include "Tokenizer.h"

const std::string COLOR_RED = "\033[1;31m";
const std::string COLOR_RESET = "\033[0m";
const std::string COLOR_GREEN = "\033[1;32m";

SQL::Tokenizer::Tokenizer():
	_filename(""),
	_original_input(""),
	_input(""),
	_token(""),
	_current_line(""),
	_lineno(1),
	_column(1),
	_trailingspace(0)
{
}

SQL::Tokenizer::Tokenizer(const std::string &input, const std::string &filename):
	_filename(filename),
	_original_input(input),
	_input(input),
	_token(""),
	_current_line(""),
	_lineno(1),
	_column(1),
	_trailingspace(0)
{
}

std::string SQL::Tokenizer::peek()
{
	if (_token.empty())
	{
		return next();
	}

	return _token;
}

std::string SQL::Tokenizer::next()
{
	std::string token;

	while (!_input.empty())
	{
		if (_input[0] == ' ')
		{
			if (token.empty())
			{
				_column++;
				_current_line += " ";
				_trailingspace++;
				_input.erase(0, 1);
				continue;
			}
			else
			{
				break;
			}
		}
		else if (_input[0] == '\t')
		{
			_column += 4;
			_current_line += "    ";
			_trailingspace += 4;
			_input.erase(0, 1);
			continue;
		}
		else if (_input[0] == '\r')
		{
			_input.erase(0, 1);
			continue;
		}
		else if (_input[0] == '\n')
		{
			_lineno++;
			_column = 1;
			_current_line.clear();
			_trailingspace = 0;
			_input.erase(0, 1);
			break;
		}
		else if (_input[0] == '(' || _input[0] == ')' || _input[0] == ',' || _input[0] == ';' || _input[0] == '*')
		{
			if (token.empty())
			{
				_column += 1;
				token = _input[0];
				_trailingspace = 0;
				_current_line += _input[0];
				_input.erase(0, 1);
				break;
			}
			else
			{
				break;
			}
		}
		else  // normal character
		{
			token += _input[0];
			_column++;
			_trailingspace = 0;
			_current_line += _input[0];
			_input.erase(0, 1);
		}
	}

	_token = token;
	return _token;
}

int SQL::Tokenizer::getTrailingspace() const
{
	return _trailingspace;
}

std::string SQL::Tokenizer::getErrorString(const std::string &message, int additional_space)
{
	// get the rest of the line
	while(!_input.empty() && _input[0] != '\n' && _input[0] != EOF)
	{
		_current_line += _input[0];
		_input.erase(0, 1);
	}

	// find the start of the error
	int error_start = (_column - _token.size() - 1) + additional_space;

	// build the error string
	std::string error;
	if (_filename.empty())
	{
		error += "Error " + std::to_string(_lineno) + ":" + std::to_string(error_start) + "\n";
	}
	else
	{
		error += "Error " + _filename + ":" + std::to_string(_lineno) + ":" + std::to_string(error_start) + "\n";
	}

	for (int i = 0; i < _current_line.size(); ++i)
	{
		if (i >= error_start - 1 && i <= error_start + _token.size() - 2)
		{
			error += COLOR_RED;
		}

		if (_current_line[i] == '\t')
		{
			error += "    ";
		}
		else
		{
			error += _current_line[i];
		}

		if (i >= error_start - 1 && i <= error_start + _token.size() - 2)
		{
			error += COLOR_RESET;
		}
	}

	error += "\n";

	//error += _current_line + "\n";

	for (int i = 0; i < error_start - 1; ++i)
	{
		error += " ";
	}

	error += "^\n";

	if (!message.empty())
	{
		error += COLOR_RED + message + COLOR_RESET + "\n";
	}

	return error;
}
