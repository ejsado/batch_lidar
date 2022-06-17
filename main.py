# script to derive products from LIDAR data
# script settings are found in options.py

import sys
import glob
import arcpy

from options import *

if __name__ == '__main__':
	print("Running batch_lidar")
	if convertToLAS:
		print("Converting files in " + convertFolder)
		for las in glob.glob(outputFolder + r"\*.las", recursive=False):
			print("WARNING: The output folder " + outputFolder + " contains other LAS files.")
			print("Files in the output folder will not be overwritten, but there may be a file name conflict error.")
			break
		result = arcpy.conversion.ConvertLas(
			convertFolder,
			outputFolder,
			las_options=[],
			define_coordinate_system="ALL_FILES",
			in_coordinate_system=definedCRS
		)
		if verboseOutput: print(result)
	if createLasDataset:
		print("Creating LAS Dataset")
		result = arcpy.management.CreateLasDataset(
			lasFolder,
			lasDataset
		)
		if verboseOutput: print(result)
	if createDEM:
		print("Creating DEM")
		result = arcpy.conversion.LasDatasetToRaster(
			lasDataset,
			demRaster
		)
		if verboseOutput: print(result)

