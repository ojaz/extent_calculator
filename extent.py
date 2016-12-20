import os
import argparse

from handlers.raster_handler import RasterHandler


# list of cached handlers
handlers = { 'raster': RasterHandler() }

def get_handler(ext):
    '''
    Get a cached handler or create a new one depending on the file type

    params: ext (str) - file extention
    return: (object) - handler object for calculating image metadata
    '''
    if ext not in handlers:
        return handlers['raster']


def start(files):
    '''
    For file names specified, calculate the image extents, and get the SRS codes

    params: files (list) - filenames to determine metadata for
    return: (None)
    '''
    for f in files:
        path, ext = os.path.splitext(f)
        handler = get_handler(ext)
        extent = handler.get_extent(f);

        if extent:
            SRS, UL, LR = extent
            print 'Extent for {}:'.format(f)
            print '({}) UL={}, LR={}\n'.format(SRS, UL, LR)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='PATH',
                        type=str, nargs='+',
                        help='List of file paths to calculate extents')
    args = parser.parse_args()
    files = args.path
    start(files)

