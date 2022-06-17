# script to derive products from LIDAR data
# script settings are found in options.py

import arcpy

from options import *

if __name__ == '__main__':
	print("Running batch_lidar")
	if convertToLAS:
		print("Converting files in " + convertFolder)
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

