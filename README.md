# Intel_tasks
Test tasks for an Intel interview

All tasks are done on Python 3

# TASK 1
The following conditions are taken due to lack of them in requirements:
+ Dot symbol ___'.'___ after a last digit is allowed. It is ignored during function processing.  
Example: ___1.m___ is equals to 1 minute. Function result is ___60___.
+ Dot symbol ___'.'___ before a first digit is allowed. It represents fractional value less than 1.  
Example: ___.017m___ is equals to 1 second. Function result is ___1___.
+ Dot symbol ___'.'___ without any digits is not allowed. Exception is raised.

Run command from a command line example:    
___python time_converter.py 1.2h___

# TASK 2
For convenient unit testing it has been decided to pass the output type in the argument.  
Thus, common use of the program from the command line with the standard output has the following look:  
___python representer.py ex_1.txt ex_2.txt ex_3.txt___  
The program stops after pressing any key.  
  
Unit tests pass an empty list as an output. This is done for saving result.
  
The program is written on Windows. The quit-mechanism is tested on Windows. However, it is easy to add Linux related program quit.  
Every test file processed by the program should have an empty line at the end. Otherwise last file line will be skipped in the program output.  

# TASK 3
The solution works for ascending sorting.
I have tried to make a solution as much easy as I can. Therefore it has obvious disadvantage for the case with big iterables at the input - a lot of memory is used for storing generated values.
