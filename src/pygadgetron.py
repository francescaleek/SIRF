# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pygadgetron', [dirname(__file__)])
        except ImportError:
            import _pygadgetron
            return _pygadgetron
        if fp is not None:
            try:
                _mod = imp.load_module('_pygadgetron', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pygadgetron = swig_import_helper()
    del swig_import_helper
else:
    import _pygadgetron
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def cGT_ISMRMRDatasetFromFile(file, group):
    return _pygadgetron.cGT_ISMRMRDatasetFromFile(file, group)
cGT_ISMRMRDatasetFromFile = _pygadgetron.cGT_ISMRMRDatasetFromFile

def cGT_readISMRMRDatasetHeader(ptr_data, ptr_head):
    return _pygadgetron.cGT_readISMRMRDatasetHeader(ptr_data, ptr_head)
cGT_readISMRMRDatasetHeader = _pygadgetron.cGT_readISMRMRDatasetHeader

def cGT_setConnectionTimeout(ptr_con, timeout_ms):
    return _pygadgetron.cGT_setConnectionTimeout(ptr_con, timeout_ms)
cGT_setConnectionTimeout = _pygadgetron.cGT_setConnectionTimeout

def cGT_connect(ptr_con, host, port):
    return _pygadgetron.cGT_connect(ptr_con, host, port)
cGT_connect = _pygadgetron.cGT_connect

def cGT_sendConfigScript(ptr_con, config):
    return _pygadgetron.cGT_sendConfigScript(ptr_con, config)
cGT_sendConfigScript = _pygadgetron.cGT_sendConfigScript

def cGT_sendConfigFile(ptr_con, file):
    return _pygadgetron.cGT_sendConfigFile(ptr_con, file)
cGT_sendConfigFile = _pygadgetron.cGT_sendConfigFile

def cGT_sendParameters(ptr_con, par):
    return _pygadgetron.cGT_sendParameters(ptr_con, par)
cGT_sendParameters = _pygadgetron.cGT_sendParameters

def cGT_sendParametersString(ptr_con, par):
    return _pygadgetron.cGT_sendParametersString(ptr_con, par)
cGT_sendParametersString = _pygadgetron.cGT_sendParametersString

def cGT_addReader(ptr_gc, id, ptr_r):
    return _pygadgetron.cGT_addReader(ptr_gc, id, ptr_r)
cGT_addReader = _pygadgetron.cGT_addReader

def cGT_addWriter(ptr_gc, id, ptr_r):
    return _pygadgetron.cGT_addWriter(ptr_gc, id, ptr_r)
cGT_addWriter = _pygadgetron.cGT_addWriter

def cGT_addGadget(ptr_gc, id, ptr_r):
    return _pygadgetron.cGT_addGadget(ptr_gc, id, ptr_r)
cGT_addGadget = _pygadgetron.cGT_addGadget

def cGT_configGadgetChain(ptr_con, ptr_gc):
    return _pygadgetron.cGT_configGadgetChain(ptr_con, ptr_gc)
cGT_configGadgetChain = _pygadgetron.cGT_configGadgetChain

def cGT_registerHDFReceiver(ptr_con, file, group):
    return _pygadgetron.cGT_registerHDFReceiver(ptr_con, file, group)
cGT_registerHDFReceiver = _pygadgetron.cGT_registerHDFReceiver

def cGT_registerImagesReceiver(ptr_con, ptr_img):
    return _pygadgetron.cGT_registerImagesReceiver(ptr_con, ptr_img)
cGT_registerImagesReceiver = _pygadgetron.cGT_registerImagesReceiver

def cGT_writeImages(ptr_imgs, ptr_conn, out_file, out_group):
    return _pygadgetron.cGT_writeImages(ptr_imgs, ptr_conn, out_file, out_group)
cGT_writeImages = _pygadgetron.cGT_writeImages

def cGT_numImages(ptr_imgs):
    return _pygadgetron.cGT_numImages(ptr_imgs)
cGT_numImages = _pygadgetron.cGT_numImages

def cGT_getImageDimensions(ptr_imgs, im_num, ptr_dim):
    return _pygadgetron.cGT_getImageDimensions(ptr_imgs, im_num, ptr_dim)
cGT_getImageDimensions = _pygadgetron.cGT_getImageDimensions

def cGT_getImageDataAsDoubleArray(ptr_imgs, im_num, ptr_data):
    return _pygadgetron.cGT_getImageDataAsDoubleArray(ptr_imgs, im_num, ptr_data)
cGT_getImageDataAsDoubleArray = _pygadgetron.cGT_getImageDataAsDoubleArray

def cGT_sendAcquisitions(ptr_con, ptr_dat):
    return _pygadgetron.cGT_sendAcquisitions(ptr_con, ptr_dat)
cGT_sendAcquisitions = _pygadgetron.cGT_sendAcquisitions

def cGT_disconnect(ptr_con):
    return _pygadgetron.cGT_disconnect(ptr_con)
cGT_disconnect = _pygadgetron.cGT_disconnect

def newObject(name):
    return _pygadgetron.newObject(name)
newObject = _pygadgetron.newObject

def deleteObject(ptr):
    return _pygadgetron.deleteObject(ptr)
deleteObject = _pygadgetron.deleteObject

def newDataHandle():
    return _pygadgetron.newDataHandle()
newDataHandle = _pygadgetron.newDataHandle

def deleteDataHandle(ptr):
    return _pygadgetron.deleteDataHandle(ptr)
deleteDataHandle = _pygadgetron.deleteDataHandle

def executionStatus(ptr):
    return _pygadgetron.executionStatus(ptr)
executionStatus = _pygadgetron.executionStatus

def executionError(ptr):
    return _pygadgetron.executionError(ptr)
executionError = _pygadgetron.executionError

def executionErrorFile(ptr):
    return _pygadgetron.executionErrorFile(ptr)
executionErrorFile = _pygadgetron.executionErrorFile

def executionErrorLine(ptr):
    return _pygadgetron.executionErrorLine(ptr)
executionErrorLine = _pygadgetron.executionErrorLine
# This file is compatible with both classic and new-style classes.


