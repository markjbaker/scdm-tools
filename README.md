# scdm-tools
Tools for Stanley Center Data Management. Used for REDCap, UGER cluster, etc.

Stack/Style/etc.:
	-Assume at least Python 3.7 (meaning we have fstrings, type hints, etc.) 
	-Version control system is Git. Repository is public on github.com/markjbaker
	-Dependency control is through requirements.txt. Use a virtual environment during development so `pip` can handle this for you
	-Use `pandas` to manipulate data unless it's simple enough to be kept in a primitive datatype (dict, list, etc.)
	-Use `requests` for all REST API calls  
	-Focus on readability. No actual style guide yet but try to be consistent with what's already there
	-Try to make code as self-documenting as possible through docstrings and type hints
	
Planned:
	-REDCap module that is independent of other tools
	-"Project-to-cloud" framework makes any cloud API easy to integrate