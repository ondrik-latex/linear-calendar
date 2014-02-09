from datetime import date
import re

LATEX_SOURCE = "./template.tex"

FIRST_DATE = date(2014, 1, 1)
LAST_DATE = date(2014, 12, 14)

if __name__ == "__main__":
    begin_date = FIRST_DATE
    end_date = LAST_DATE
    with open(LATEX_SOURCE) as latex_file:
        for line in latex_file:
            if (re.search(r"^\\newcommand{\\firstdate}{[^}]*}$", line)):
                line = re.sub(r"{[^{]*}$", "{" + begin_date.isoformat() + "}", line)
            if (re.search(r"^\\newcommand{\\lastdate}{[^}]*}$", line)):
                line = re.sub(r"{[^{]*}$", "{" + end_date.isoformat() + "}", line)
            print(line, end = '')

