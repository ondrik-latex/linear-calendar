import re

from datetime import date, timedelta
from subprocess import call

LATEX_SOURCE = "./template.tex"
OUTPUT_BASE = "./output"

FIRST_DATE = date(2014, 1, 1)
LAST_DATE = date(2014, 12, 31)

MAX_DAYS = 34

if __name__ == "__main__":
    begin_date = FIRST_DATE

    i = 0
    while begin_date <= LAST_DATE:
        end_date = min(begin_date + timedelta(days=MAX_DAYS), LAST_DATE)
        file_name = OUTPUT_BASE + i.__str__() + ".tex"
        with open(file_name, mode="w") as out_file:
            with open(LATEX_SOURCE, mode="r") as latex_file:
                for line in latex_file:
                    if (re.search(r"^\\newcommand{\\firstdate}{[^}]*}$", line)):
                        line = re.sub(r"{[^{]*}$", "{" + begin_date.isoformat() + "}", line)
                    if (re.search(r"^\\newcommand{\\lastdate}{[^}]*}$", line)):
                        line = re.sub(r"{[^{]*}$", "{" + end_date.isoformat() + "}", line)
                    out_file.write(line)
        call(["pdflatex", file_name])
        begin_date = end_date + timedelta(days=1)
        i = i+1
