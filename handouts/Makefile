SHELL := /bin/bash
PDFLATEX = pdflatex

all: FeedbackForm.pdf LessonPlan.pdf

FeedbackForm.pdf: FeedbackForm.tex
	$(PDFLATEX) $<

LessonPlan.pdf: LessonPlan.tex
	$(PDFLATEX) $<

clean:
	rm -f *.{aux,log,pdf}
