import arcpy


# GENERAL OPTIONS

# environment settings
# set the geodatabase where the script will create items
arcpy.env.workspace = r"D:\Projects_Tower2019\GIS\Lidar\AutomateLidar.gdb"

# overwrite items in the workspace with items created by this script
# if this is false, an error will occur when an item already exists
arcpy.env.overwriteOutput = True

# show output of each geoprocessing tool
# https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/using-tools-in-python.htm
verboseOutput = True


# GEOPROCESSING OPTIONS

# select which operations to perform
# set these values to False if you wish to skip certain steps
# convert a directory of lidar data files to .las
convertToLAS = False
# create a dataset containing a collection of .las files
createLasDataset = False
# create a digital elevation model raster
createDEM = True
# create contour lines
createContour = True
# create a triangulated irregular network
createTIN = True

# LAS/LAZ/ZLAS directory
# all matching files in the directory will be converted
convertFolder = r"D:\Projects_Tower2019\GIS\Lidar\data\LAZ"

# coordinate system for the input LAS/LAZ/ZLAS files
# https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/spatialreference.htm
# all files in the above directory must be in the same CRS defined here
# (horizontal CRS, vertical CRS)
definedCRS = arcpy.SpatialReference(6342, 5703)

# output folder for files converted to LAS
outputFolder = r"D:\Projects_Tower2019\GIS\Lidar\data\LAS_output"

# folder containing LAS files for the LAS dataset
lasFolder = outputFolder

# LAS dataset name and location
# this file will be overwritten if it already exists
# must end in .lasd
lasDataset = r"D:\Projects_Tower2019\GIS\Lidar\data\wind_cave_lasd.lasd"

# product resolution/interval (units are based on definedCRS)
# used as the raster cell size for the DEM
# used as the contour interval
# used as the window size for thinning points in the TIN
resolution = 5

# DEM file name to be stored in the geodatabase
demRaster = arcpy.env.workspace + r"\wind_cave_LASD_DEM"

# contour feature class file name to be stored in the geodatabase
contourFeature = arcpy.env.workspace + r"\wind_cave_LASD_contour"

# TIN dataset name
# this will be a directory
tinDataset = r"D:\Projects_Tower2019\GIS\Lidar\data\wind_cave_LASD_TIN"
