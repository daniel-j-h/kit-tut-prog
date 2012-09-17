PYTHON ?= python2.6
BUILDDIR ?= ../build
BUILDSLIDE ?= buildSlide.py
BUILDINDEX ?= buildIndex.py

all: slides index

slides: $(patsubst %.html, $(BUILDDIR)/%.html, $(wildcard *.html))

$(BUILDDIR)/%.html: %.html Makefile
	$(PYTHON) $(BUILDSLIDE) $< > $@

index: Makefile
	$(PYTHON) $(BUILDINDEX) $(BUILDDIR) > ../index.html

clean:
	rm -f $(BUILDDIR)/*.html ../index.html

.PHONY: all slides index clean
