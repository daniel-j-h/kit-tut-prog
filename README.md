Introduction To Programming tutorial
====================================

Building the slides
-------------------

Note: The build directory already contains the latest slides.
You only have to re-build a slide if you modified a corresponding file in the slide directory, or added a new one.

Jinja2 is used to simplify the build process.

* git clone --recursive --branch gh-pages git://github.com/daniel-j-h/kit-tut-prog.git
* cd kit-tut-prog/slides/
* ./buildSlides.py tutorial-01.html > ../build/tutorial-01.html
* ./buildIndex.py ../build/ > ../index.html


Adding new slides
-----------------

All slides should extend from slide.tmpl and override the slides block.
Add your new .html file to the slides directory, metadata to the .json file, and re-run the commands above on your new slide.

See the .html and .json files in the slides directory for further information.
