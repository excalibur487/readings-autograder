# readings-autograder - v1.0.0

You'll need python3 and piazza-api for the grader to work. Once you have python installed, run
```make``` from the root and that should install the dependencies *(piazza-api)* for you.

Usage: ```python3 grader.py``` in your terminal or git bash

Program will prompt for your piazza credentials. Once logged in, enter the post number for the readings post. 
*(you'll find this number in the url after "/post")*

### Note: _**Anonymous**_ posters will have to be graded manually for now. 

The output will be a csv file with student names and their corresponding scores.

Current grading criteria:
70% for an initial post. 30% for a reply.
