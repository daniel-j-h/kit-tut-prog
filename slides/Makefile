PYTHON ?= python2.6
BUILDDIR ?= ../build
INDEXFILE ?= ../index.html
BUILDSLIDE ?= buildSlide.py
BUILDINDEX ?= buildIndex.py

all: slides index

slides: $(patsubst %.html, $(BUILDDIR)/%.html, $(wildcard *.html))

$(BUILDDIR)/%.html: %.html Makefile
	$(PYTHON) $(BUILDSLIDE) $< > $@

index: Makefile
	$(PYTHON) $(BUILDINDEX) $(BUILDDIR) > $(INDEXFILE)

clean:
	rm -f $(BUILDDIR)/*.html $(INDEXFILE)

.PHONY: all slides index clean
