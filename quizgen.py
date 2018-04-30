import random, os, argparse, re, subprocess

fileName = ""


# This reads a file and returns LaTeX code for a problem
def generateProblem(f):
    # Read all the lines of python code
    lines = f.readlines()
    f.close()
    marker = lines.index("#####\n")
    # Get python code
    pythonCode = "".join(lines[:marker])
    # Get latex code
    latexCode = "".join(lines[marker + 1:])
    # Run python code
    exec(pythonCode)
    # Do the replacements and then neaten the formula code up. This only works for x and t, could
    # be modified to work with any variable in the list of variables, but would need to rethink
    # strategy to do that.
    for x in varList:
        latexCode = latexCode.replace("@" + x, str(eval(x)))
    neatenItems = [["1x", "x"], ["0x", "0"], ["x^1", "x"], ["--", "+"], ["-+", "-"], ["+-", "-"], ["-0", ""], ["+0", ""], [" (x)", " x"], ["1t", "t"], ["0t", "0"], ["t^1", "t"], [" (t)", " t"]]
    for x in neatenItems:
        latexCode = latexCode.replace(x[0],x[1])
    return latexCode

# I need to modify this so that I only get one version of each problem type. I will create
# new subfolders for each problem type, and then grab a randomization from each type, or
# grab one random problem from the list in the folder. Either way, I can randomly select one file
# from each folder, then run the python script in the file.
# To get a list of all subdirectories, I need to say "from glob import glob" and then
# subdirectories = glob("./*/") should make a list of them. I'll also need to modify this
# procedure so that I dive into a folder rather than grabbing a file.
def getProblems(thisTarget):
    problems = []
    fileNames = sorted(os.listdir("./" + thisTarget))
    for f in fileNames:
        if f.endswith(".def"):
            p = generateProblem(open(thisTarget + "/" + f))
            problems.append(p)
    return problems

def getCriteria(thisTarget):
    cfile = open(thisTarget + "/criteria.tex")
    return cfile.read()

def getTitle(thisTarget):
    titles = open("Static/titles.txt").read()
    for item in titles.split("\n"):
        if item.startswith(thisTarget):
            return item.split(" ", 1)[1]

def createQuizFile(problems, criteria):
    global fileName, name
    fname = name
    if fname != "":
        fname = "_" + name.replace(" ", "_")
    fileName = target + "_" + str(version) + fname + ".tex"
    f = open(fileName, 'w')
    f.write(createHeader())
    for x in problems:
        f.write(x)
        f.write("\n")
    f.write("\t\end{questions}\n\end{document}")
    f.close()

def createHeader():
    hdr = open("Static/header.txt").read()
    replacements = {
        "#0" : str(name),
        "#1" : str(target),
        "#2" : str(date),
        "#3" : str(targetTitle),
        "#4" : str(criteria),
        "#5" : str(version),
    }
    substrs = sorted(replacements, key=len, reverse=True)
    regexp = re.compile('|'.join(map(re.escape, substrs)))
    hdr = regexp.sub(lambda match: replacements[match.group(0)], hdr)
    return hdr

# Parse the args man!
parser = argparse.ArgumentParser()
parser.add_argument("target", help="the target to build quiz on (case sensitive)", type=str)
parser.add_argument("-n", "--name", help="student's name", type=str, default="")
parser.add_argument("-d", "--date", help="day of quiz -- use double quotes", type=str, default="\\today")
parser.add_argument("-v", "--version", help="version number", type=int, default=None)
args = parser.parse_args()

# Set up some easy to reference variable names.
name = args.name
target = args.target
date = args.date
version = args.version

# Create the quiz.
problems = getProblems(target)
criteria = getCriteria(target)
targetTitle = getTitle(target)
createQuizFile(problems, criteria)
subprocess.call(["latexmk -quiet -pdf " + fileName], shell=True)
subprocess.call(["latexmk -c"], shell=True)
subprocess.call(["rm -rf *.dvi"], shell=True)

# Include into template
