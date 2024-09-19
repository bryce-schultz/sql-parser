#include <iostream>

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
		std::string input(argv[1]);	
	}
	else
	{
		do
		{
			std::getline(std::cin, input);
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