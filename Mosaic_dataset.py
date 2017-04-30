#-------------------------------------------------------------------------------
# Name:       Creating Temporal Mosiac Dataset
# Purpose:  Creating a script for mosaicking images of early St. Louis maps together
#
# Author:      Govind Chadalawada
#
#Create a geodatabase
import arcpy
from arcpy import env

#arcpy.CreateFileGDB_management("E:\Final_python\Output", "timeline.gdb")


#Building the Mosaic Datasets for 1860, 1880, 1895, 1902 & 1903
import arcpy
arcpy.env.workspace = "E:\Final_python\Output"

#import variables
gdbName = r"E:\Final_python\Output\timeline.gdb"
mdName = "1903stl"
sr = "102696 "
numBands = 3
pixelType = "8_Bit_Unsigned"
productDef = "NATURAL_COLOR_RGB"
waveLength = ""

#arcpy.CreateMosaicDataset_management(gdbName, mdName, sr, numBands, pixelType, waveLength)


#Adding Raster to Mosaic Dataset for the years 1860, 1880, 1895, 1902 & 1903
import arcpy
arcpy.env.workspace = "E:\Final_python"

#import variables
mdname = r"E:\Final_python\Output\timeline.gdb\T1903stl"
rastType ="Raster Dataset"
inputPath = r"E:\Final_python\Images\stl_1903\G4164_S4_1904_G4.tif"
updateCs = "UPDATE_CELL_SIZES"
updatebnd = "UPDATE_BOUNDARY"
updateovr = "NO_OVERVIEWS"
maxlevel = "-1"
maxcs = "#"
maxdim = "#"
spatialref = "#"
inputdatafilter = "*.TIF"
subfolder = "SUBFOLDERS"
duplicates = "ALLOW_DUPLICATES"
calStatistics = "CALCULATE_STATISTICS"
pyramids = "BUILD_PYRAMIDS"
thumbnails = "Build_THUMBNAILS"
caption = "Raster of St. Louis 1902"
forcesr = "NO_FORCE_SPATIAL_REFERENCE"

#arcpy.AddRastersToMosaicDataset_management(mdname, rastType, inputPath, updateCs, updatebnd, updateovr, maxlevel, maxcs, maxdim, spatialref, inputdatafilter, subfolder, duplicates, pyramids, calStatistics, thumbnails, caption, forcesr)


#Create Master Mosaic Dataset
gdbName = r"E:\Final_python\Output\timeline.gdb"
mdName = "stltime"
sr = "102696 "
numBands = 3
pixelType = "8_Bit_Unsigned"
productDef = "NATURAL_COLOR_RGB"
waveLength = ""

#arcpy.CreateMosaicDataset_management(gdbName, mdName, sr, numBands, pixelType, waveLength)
#Mosaic Raster Datasets are added to the Master through ArcCatalog
#Through ArcCatalog I made the master dataset into a temporal version to showcase the rasters of all five periods for St. Louis City

