import arcpy

# SET OPTIONS

# environment settings
# set the geodatabase where the script will create items
arcpy.env.workspace = r"D:\Projects_Tower2019\GIS\Lidar\AutomateLidar.gdb"
# overwrite items in the workspace with items created by this script
# if this is false, an error will occur when an item already exists
arcpy.env.overwriteOutput = True

# LAS/LAZ/ZLAS directory
# all matching files in the directory will be converted