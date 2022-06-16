import arcpy

# SET OPTIONS

# environment settings
# set the geodatabase where the script will create items
arcpy.env.workspace = r"D:\Projects_Tower2019\GIS\Lidar\AutomateLidar.gdb"

# overwrite items in the workspace with items created by this script
# if this is false, an error will occur when an item already exists
arcpy.env.overwriteOutput = True

# show output of each geoprocessing tool
# https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/using-tools-in-python.htm
verboseOutput = True

# select which operations to perform
# set these values to false if you wish to skip certain steps
convertToLAS = True

# LAS/LAZ/ZLAS directory
# all matching files in the directory will be converted
convertFolder = r"D:\Projects_Tower2019\GIS\Lidar\data\LAZ"

# text to append to converted LAS files
convertedText = "_converted"

