# the name of the output
CO=linear_calendar

# names of files other than sources the change of which should recompile the
# source
#CHANGED_FILES_OTHER =literature.bib
CHANGED_FILES_OTHER+=$(wildcard figs/*.tikz) $(wildcard figs/*.tex)

# List of TeX files
TEX_FILES=$(wildcard *.tex)

###############################################################################
#                                 Rules                                       #
###############################################################################

.PHONY: all images clean pack love

all: $(CO).pdf

$(CO).pdf: $(CHANGED_FILES_OTHER) $(TEX_FILES)
	pdflatex $(CO)
	bibtex $(CO)
	pdflatex $(CO)
	pdflatex $(CO)

clean:
	rm -f *.dvi *.log $(CO).blg $(CO).bbl $(CO).toc *.aux $(CO).out $(CO).lof
	rm -f $(CO).pdf
	rm -f *~

love: $(CO).pdf
	xpdf $(CO).pdf
