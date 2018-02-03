DEST = hw8

all: ${DEST}.pdf

%.pdf: %.tex
	pdflatex $<

clean:
	rm -Rf ${DEST}.pdf *.log *.aux *.synctex.gz

dist: 
	tar cvzf ${DEST}-student.tar.gz Makefile *tex *sty ${DEST}-*.pdf
