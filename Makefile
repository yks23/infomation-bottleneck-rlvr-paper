PAPER = main

.PHONY: all pdf clean distclean

all: pdf

pdf:
	latexmk -pdf $(PAPER).tex

clean:
	latexmk -c $(PAPER).tex

distclean:
	latexmk -C $(PAPER).tex
	rm -rf build
