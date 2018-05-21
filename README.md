# quizgen
A django webapp for dynamic math quiz generation.

# To Do
We need a function class to compare, display, and interact with math functions. 


Find a way to easily enter math notation. The Desmos graphing app uses http://mathquill.com/ for entering math. Another option is https://guppy.js.org/site/#. 

Problems have the following components, at least:

1. Text (probably we can use Markdown for that part: https://daringfireball.net/projects/markdown/)
2. Math typesetting (we can use LaTeX and/or MathML and/or MathJAX to display)
3. Math objects
  * Functions
  * Matrices
  * Graphs
4. Code (Python)
  a) Generate random instances of a problem.
  b) Generate solutions to a problem.
  c) Show hints to solving a problem.
5. Metadata:
  a) Tags
  b) Topic
  c) Author
  d) Date
  e) Version

Each problem will have the following sections:
1. Python code
2. Markdown text
3. LaTeX code
