#pragma once
#include <memory>
#include "SemanticChecker.h"

namespace SQL
{
	class TableNameIsNotKeywordSemanticCheck : public SemanticCheck
	{
	public:
		TableNameIsNotKeywordSemanticCheck(SemanticLevel level = SemanticLevel::ERROR, bool enabled = true):
			SemanticCheck(level, enabled)
		{
		}

		SemanticResult check(const std::string &value) override
		{
			bool result = true;

			if (value == "select")
			{
				result = false;
			}
			else if (value == "insert")
			{
				result = false;
			}
			else if (value == "delete")
			{
				result = false;
			}
			else if (value == "update")
			{
				result = false;
			}
			else if (value == "create")
			{
				result = false;
			}
			else if (value == "drop")
			{
				result = false;
			}
			else if (value == "from")
			{
				result = false;
			}
			else if (value == "where")
			{
				result = false;
			}
			else if (value == "table")
			{
				result = false;
			}
			else if (value == "like")
			{
				result = false;
			}

			if (!result)
			{
				return { false, "Table name cannot be a keyword" };
			}

			return { true };
		}
	};

	namespace globals
	{
		extern TableNameIsNotKeywordSemanticCheck table_name_is_not_keyword_semantic_check;
	}
}

