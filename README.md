# quizgen
A django webapp for dynamic math quiz generation.

# To Do
Write a python "function" class that compares functions. (we'll need to write some good tests for this)
Find a way to easily enter math notation. The Desmos graphing app uses http://mathquill.com/ for entering math. Another option is https://guppy.js.org/site/#. Maybe there are more? We should try to integrate this into a test page at some point.
I think that each problem will have at least the following components (please add more if you think of any):
Text (probably we can use Markdown for that part: https://daringfireball.net/projects/markdown/)
Math typesetting (we can use LaTeX and/or MathML and/or MathJAX to display)
Math objects
Functions
Matrices
Graphs
.....
Code (I think we've settled on Python). Some things the code may do:
Generate random instances of a problem.
Generate solutions to a problem.
Show hints to solving a problem.
.....
Metadata:
Tags
Topic
Author
Date
Version
......
.....
Idea: perhaps all content should be split into one of three compartments (could be in a single file, or sort of split up into multiple files and organized by our database): 
Python code
Markdown text
LaTeX code
Ideally, the "Function" class would have a lot of useful features. One could be that it would have a way to display itself in multiple output styles (markdown, mathml, latex). We can probably do better using the function to display itself after we've randomized it and so forth. That way we do all of the logical stuff before we create a latex file and thus avoid having to process a latex file to do the randomizing, which is how I do it now (pretty clunky, and causes typesetting errors because it's not catching all the weird cases).
