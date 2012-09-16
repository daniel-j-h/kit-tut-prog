Introduction To Programming tutorial
====================================

Building the slides
-------------------

Jinja2 is used to simplify the build process.

* cd slides
* ./buildSlides.py tutorial-1.html > ../build/tutorial-1.html
* ./buildIndex.py ../build/ > ../index.html

Note: The build directory contains the latest slides.
You only have to re-build a slide if you modified a corresponding file in the slide directory, or added a new one.


Adding new slides
-----------------

All slides should extend from slide.tmpl, override the slides block and opt. the title variable.
Add your new .html file to the slides directory and re-run the commands above on your new slide.

See the existing .html files in the slides directory for further information.
