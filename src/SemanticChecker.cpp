#include "SemanticChecker.h"

int SemanticCheck::_next_check_id = 0;

SemanticCheck::SemanticCheck(SemanticLevel level, bool enabled):
	_level(level),
	_enabled(enabled),
	_check_id(_next_check_id++)
{
}

int SemanticCheck::getCheckId() const
{
	return _check_id;
}
