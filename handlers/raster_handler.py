from util import error_handler
from osgeo import gdal, osr


class RasterHandler(object):
    def get_extent(self, path):
        '''
        Get extent and SRS code for a given file using gdal and osr

        params: path (str) - path to file to gather metadata
        return: (list) - srs code, and extent for file
        '''
        gdal.UseExceptions()                  # force gdal exceptions
        gdal.PushErrorHandler(error_handler)  # use custom gdal error handling

        # open file with gdal
        try:
            geos = gdal.Open(path)
        except RuntimeError:
            return False

        # calculate imagery extent
        ulx, xres, _, uly, _, yres = geos.GetGeoTransform()
        lrx = ulx + (geos.RasterXSize * xres)
        lry = uly + (geos.RasterYSize * yres)

        # get imagery projection srs for reference
        proj = geos.GetProjection()
        srs = osr.SpatialReference(wkt=proj).GetAttrValue('geogcs')

        return [srs, (ulx, uly), (lrx, lry)]
