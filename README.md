# quizgen
A Python script dynamic math quiz generation. Eventually will be wrapped into the Mango project.

# To Do
We need a function class to compare, display, and interact with math functions. 


Find a way to easily enter math notation. The Desmos graphing app uses http://mathquill.com/ for entering math. Another option is https://guppy.js.org/site/#. 

Problems have the following components, at least:

1. Text (probably we can use Markdown for that part: https://daringfireball.net/projects/markdown/)
2. Math typesetting (we can use LaTeX and/or MathML and/or MathJAX to display)
3. Math objects
    1. Functions
    2. Matrices
    3. Graphs
4. Code (Python)
    1. Generate random instances of a problem.
    2. Generate solutions to a problem.
    3. Show hints to solving a problem.
5. Metadata:
    1. Tags
    2. Topic
    3. Author
    4. Date
    5. Version

Each problem will have the following sections:
1. Python code
2. Markdown text
3. LaTeX code
