# Colors of Public Art
This project was created by [Mads Hartmann][mads] and
[Mikkel Hartmann][mikkel] while attending [Hack our Art][hack-our-art]
in Copenhagen from the 8th to 10th of April 2016.

The dataset we worked with was about the collection of public art that
the [Danish Arts Foundation][danish-arts-foundation] has purchased
since its creation in 1964. The dataset contained various information
about each artwork as well as an image taken of it taken at the time
of the purchase.

We decided to focus on paintings and wanted to explore the color usage
throughout the years. To do this we wrote a simple program that
downloaded all of the images of the paintings and analyzed the colors in
the images and picked the top five most used colors for each
image. Based on this information we created a small website where you
can browse the collection based on the colors used in the paintings.

You can browse the result on [colors-of-public-art.com][colors-of-public-art]

## Image analysis
We didn't have any prior knowledge of how to analyze colors in images
so we did the simplest thing we could think of.

We found a list of 140 colors and their RGB values and wrote a program
that for each pixel in an image finds which of the 140 colors it
resembles the most and marks that pixel down as being of that
color. Once all the pixels have been considered it finds the top five
most used colors in that image.

## Code
This project contains all the code you need in order to

* Download the images of the paintings
* Analyze the colors of each image (no attention was given to
  the performance of the code so the analysis might take a while if
  you run it on all of the images, expect roughly 10 hours)
* Run a small web-server that allows you to browse the collection by color

The structure of the project is

    .
    ├── README.md
    ├── requirements.txt :: List of python packages that needs to be installed.
    ├── data
    │   ├── dump.json :: Full dump of the dataset. You never know if the API will respond tomorrow.
    │   └── example.json :: A tiny slice of the dataset. Useful for looking up attributes.
    ├── src
    │   ├── cli :: A collection of small command line tools
    │   ├── common :: Pyhton modules used by both the cli and web modules.
    │   └── web :: Modules related to the webserver
    └── static
        ├── assets :: Contains the color usage chart.
        ├── images :: The images will be downloaded to this location
        └── styles :: CSS

The code was written quite hastily during the hackathon which is very
likely reflected in the quality.

## Running the code
Assuming that the images are still stored in the same place as when
the data-dump was committed to git it should be pretty simple to get the
code up and running on your machine. I assume you have python 2.7,
[virtualenv][virtualenv], and GNU Make installed.

The following three commands will download 10 images, analyze those images
and finally start the webserver.

    make run-download COUNT=10
    make run-analyze COUNT=10
    make run-web


[mads]: http://mads-hartmann.com/
[mikkel]: http://mikkelhartmann.dk/
[hack-our-art]: https://www.facebook.com/events/186114941758670/
[danish-arts-foundation]: http://www.kunst.dk/english/danish-arts-foundation/
[colors-of-public-art]: http://colors-of-public-art.com
[virtualenv]: https://virtualenv.pypa.io/en/latest/
