Introduction To Programming tutorial
====================================

Get the slides
--------------

 * Online: [http://kit.trvx.org](http://kit.trvx.org)
 * Local: Open index.html in your browser


Building the slides
-------------------

Note: The build directory already contains the latest slides.  
You only have to re-build a slide if you modified a corresponding file in the slide directory, or added a new one.

Jinja2 is used to simplify the build process.  
Reveal.js is included as a git submodule, so you have to clone the repository recursively.

    git clone --recursive --branch gh-pages git://github.com/daniel-j-h/kit-tut-prog.git
    cd kit-tut-prog/slides/
    make --jobs 2 --keep-going

Or build them yourself

    ./buildSlide.py tutorial-01.html > ../build/tutorial-01.html
    ./buildIndex.py ../build/ > ../index.html


Adding new slides
-----------------

All slides should extend from slide.tmpl and override the slides block.  
Add your new .html file to the slides directory, metadata to the .json file, and re-run the commands above.


Example slide syntax
--------------------

Your presentation file (my-presentation.html) should probably look like this.

    {% extends 'slide.tmpl' %}
    {% block slides %}
    <section data-markdown>
      ## First Slide

      Using markdown.
    </section>
    <section>
      <h2>Second Slide</h2>
      <p>Using html.</p>
    </section>
    {% endblock %}

You want to add some metadata, too.

    "my-presentation" : {
      "date" : "Oct. 29 2012",
      "description" : "Basic examples"
    }

The description and date, if provided, is used for the index and for the cover slide.
