#include <iostream>
#include <fstream>

#include "Parser.h"

using Parser = SQL::Parser;

int main(int argc, char **argv)
{
	std::string input;

	if (argc > 2)
	{
		std::cerr << "Usage: " << argv[0] << " [SQL statement]" << std::endl;
		return 1;
	}

	if (argc == 2)
	{
		std::string filename(argv[1]);

		std::ifstream file(filename);

		if (!file.is_open())
		{
			std::cerr << "Could not open file: " << filename << std::endl;
			return 1;
		}

		std::string line;

		while (std::getline(file, line))
		{
			if (line.empty())
			{
				break;
			}

			Parser parser;
			auto result = parser.parse(line);

			if (result.success)
			{
				for (const auto &arg : result.args)
				{
					std::cout << arg << std::endl;
				}
			}
			else
			{
				for (const auto &arg : result.args)
				{
					std::cerr << arg << std::endl;
				}

				std::cerr << result.error << std::endl;
			}
		}
	}
	else
	{
		do
		{
			std::getline(std::cin, input);

			if (input.empty() || input == "exit")
			{
				break;
			}

			Parser parser;
			auto result = parser.parse(input);

			if (result.success)
			{
				for (const auto &arg : result.args)
				{
					std::cout << arg << std::endl;
				}
			}
			else
			{
				for (const auto &arg : result.args)
				{
					std::cerr << arg << std::endl;
				}

				std::cerr << result.error << std::endl;
			}

		} while (!input.empty() && input != "exit");
	}

	return 0;
}