#!/bin/bash

for ifile in `ls tex/*.tex`
do
	echo "$ifile"
	bfile=`basename $ifile ".tex"`
	echo "Starting $bfile..."
	cp $ifile "diagram.tex"
	pdflatex "main.tex" > "log/$bfile.log"
	pdf2svg "main.pdf" "svg/$bfile.svg"
	echo "done!"
done
