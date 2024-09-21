#pragma once
#include <string>
#include <map>
#include <memory>

enum class SemanticLevel
{
	INFO,
	WARNING,
	ERROR
};

struct SemanticResult
{
	bool success { true };
	std::string error { "" };
	std::string message { "" };
};

	    

class SemanticCheck
{
public:
	SemanticCheck(SemanticLevel level = SemanticLevel::ERROR, bool enabled = true);
	virtual SemanticResult check(const std::string &value) = 0;

	int getCheckId() const;

protected:
	SemanticLevel _level;
	bool _enabled;
	int _check_id;

	static int _next_check_id;
};