'''
Tool that utilizes python gdal bindings to calculate imagery extents.
Will output the extent as upper left and lower right coordinates, and the
SRS code for the image projection.

Author: ojaz
Updated: 12/16/16

### Requirements
    * gdal >= 1.10
    * python >= 2.7.10

### Usage
    $ python extent.py [-h] PATH [PATH ...]
'''

from argparse import ArgumentParser
from osgeo import gdal, osr


def get_extent(path):
    gdal.UseExceptions()                  # force gdal exceptions
    gdal.PushErrorHandler(error_handler)  # use custom gdal error handling

    # open file with gdal
    try:
        geos = gdal.Open(path)
    except RuntimeError:
        print "File not found {}!".format(path)
        return

    # calculate imagery extent
    ulx, xres, _, uly, _, yres = geos.GetGeoTransform()
    lrx = ulx + (geos.RasterXSize * xres)
    lry = uly + (geos.RasterYSize * yres)

    # get imagery projection srs for reference
    proj = geos.GetProjection()
    srs = osr.SpatialReference(wkt=proj).GetAttrValue('geogcs')

    return [srs, (ulx, uly), (lrx, lry)]


def error_handler(err_class, err_num, err_msg):
    # clean default error messages
    err_msg = err_msg.replace('\n', ' ')

    # ignore warnings, else print formatted error info
    if err_class == gdal.CE_Warning or err_class == gdal.CE_None:
        pass
    else:
        print '[{} ({})]: {}\n'.format(err_class, err_num, err_msg)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('path', metavar='PATH',
                        type=str, nargs='+',
                        help='List of file paths to calculate extents')
    args = parser.parse_args()
    files = args.path

    for f in files:
        extent = get_extent(f);
        SRS, UL, LR = extent

        print 'Extent for {}:'.format(f)
        print '({}) UL={}, LR={}\n'.format(SRS, UL, LR)
