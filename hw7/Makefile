SOURCE = hw1 hw2 hw3 hw4 hw5 hw6 hw7

PDF_COMPILE = .build/latexrun
REMOVE_ANSWER = awk -f .build/remove-answers.awk

all: $(addsuffix .pdf, $(SOURCE)) $(addsuffix -sol.pdf, $(SOURCE)) $(addsuffix -student.tex, $(SOURCE))

%-sol.tex: %.tex homework.sty
	sed -e 's/% \\solstrue/\\solstrue/g' $< > $@

%-student.tex: %.tex
	${REMOVE_ANSWER} $< > $@
	sed -e 's/% \\solstrue/\\solstrue/g' -i "" $@
	sed -e '/^ *%/ d' -i "" $@

%.pdf: %.tex homework.sty
	${PDF_COMPILE} $<

clean:
	rm -Rf $(addsuffix .pdf, $(SOURCE))
	rm -Rf *.log *.aux *.make *.d *.fls *.rel *.synctex.gz *-sol.tex *-sol.pdf *-student.* *.out
