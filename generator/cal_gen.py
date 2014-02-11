import re

from datetime import date, timedelta
from subprocess import call

LATEX_SOURCE = "./template.tex"
OUTPUT_FILENAME = "./output.tex"

FIRST_DATE = date(2014, 1, 1)
LAST_DATE = date(2014, 12, 31)

MAX_DAYS = 32

if __name__ == "__main__":
    state = 1    # 1... foreplay, 2... template, 3... climax

    # to store the parts of the file
    foreplay = []
    template = []
    climax = []
    with open(LATEX_SOURCE, mode="r") as latex_file:
        for line in latex_file:
            if (re.search(r"BEGIN TEMPLATE", line)):
                state = 2
                break
            else:
                foreplay.append(line)

        for line in latex_file:
            if (re.search(r"END TEMPLATE", line)):
                state = 3
                break
            else:
                template.append(line)

        for line in latex_file:
            climax.append(line)

    with open(OUTPUT_FILENAME, mode="w") as out_file:
        for line in foreplay:
            out_file.write(line)

        begin_date = FIRST_DATE
        i = 1
        while begin_date <= LAST_DATE:
            end_date = min(begin_date + timedelta(days=MAX_DAYS), LAST_DATE)
            out_file.write("% TEMPLATE INSTANTIATION {0}:\n".format(i))
            for line in template:
                line = re.sub(r'\\firstdate', begin_date.isoformat(), line)
                line = re.sub(r'\\lastdate', end_date.isoformat(), line)
                out_file.write(line)
            out_file.write("% END OF TEMPLATE INSTANTIATION {0}\n".format(i))
            begin_date = end_date + timedelta(days=1)
            i = i + 1

        for line in climax:
            out_file.write(line)

    # create the PDF
    call(["pdflatex", OUTPUT_FILENAME])
