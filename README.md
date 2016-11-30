# Extent Calculator
Tool that utilizes python gdal bindings to calculate imagery extents.
Will output the extent as upper left and lower right coordinates, and the
SRS code for the image projection.

### Requirements
* gdal >= 1.10
* python >= 2.7.10

### Usage
`$ python extent.py [-h] PATH [PATH ...]`
