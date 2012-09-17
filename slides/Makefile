PYTHON ?= python2.6
BUILDDIR ?= ../build
BUILDSLIDES ?= buildSlides.py
BUILDINDEX ?= buildIndex.py

all: slides index

slides: $(patsubst %.html, $(BUILDDIR)/%.html, $(wildcard *.html))

$(BUILDDIR)/%.html: %.html Makefile
	$(PYTHON) $(BUILDSLIDES) $< > $@

index: Makefile
	$(PYTHON) $(BUILDINDEX) $(BUILDDIR) > ../index.html

clean:
	rm -f $(BUILDDIR)/*.html ../index.html

.PHONY: all slides index clean
