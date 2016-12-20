from osgeo import gdal


def error_handler(err_class, err_num, err_msg):
    '''
    Custom error handler for gdal errors, uses more readable messages and
      disregards warnings (as they are generally not helpful and intrusive when
      simply calculating extents)

    params: err_class (int) - type of error (warning, failure, etc.)
            err_num   (int) - error code specific to problem
            err_msg   (str) - description of error
    return: (None)
    '''
    # clean default error messages
    err_msg = err_msg.replace('\n', ' ')

    # ignore warnings, else print formatted error info
    if err_class == gdal.CE_Warning or err_class == gdal.CE_None:
        pass
    else:
        print '[ERROR {} CODE {}]: {}\n'.format(err_class, err_num, err_msg)
