# script to derive products from LIDAR data
# settings are found in options.py

import glob
import arcpy

from options import *

if __name__ == '__main__':
	print("Running batch_lidar")
	if convertToLAS:
		print("Converting files in " + convertFolder)
		# check if the output folder has LAS files already
		for las in glob.glob(outputFolder + r"\*.las", recursive=False):
			print("WARNING: The output folder " + outputFolder + " contains other LAS files.")
			print("Files in the output folder will not be overwritten, but there may be a file name conflict error.")
			break
		# run the conversion tool
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
		# combine the files into a single dataset
		result = arcpy.management.CreateLasDataset(
			lasFolder,
			lasDataset
		)
		if verboseOutput: print(result)
	if createDEM:
		print("Creating DEM")
		# generate a DEM from the LAS dataset
		result = arcpy.conversion.LasDatasetToRaster(
			lasDataset,
			demRaster,
			sampling_value=resolution
		)
		if verboseOutput: print(result)
	if createContour:
		print("Create Contour Lines")
		# generate contour lines from the LAS dataset
		result = arcpy.ddd.SurfaceContour(
			lasDataset,
			contourFeature,
			resolution
		)
		if verboseOutput: print(result)
	if createTIN:
		print("Creating TIN")
		# generate a TIN from the LAS dataset
		result = arcpy.ddd.LasDatasetToTin(
			lasDataset,
			tinDataset,
			thinning_type="WINDOW_SIZE",
			thinning_method="CLOSEST_TO_MEAN",
			thinning_value=resolution
		)
		if verboseOutput: print(result)
