#-------------------------------------------------------------------------------
# Name:        Mosiac Dataset
# Purpose:  Creating a script for mosaicking images of SLU campus maps together
#
# Author:      Govind Chadalawada
#
# Created:     10/04/2017
# Copyright:   (c) Govind 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Create a geodatabase
##import arcpy
##from arcpy import env
##
#arcpy.CreateFileGDB_management("C:\Users\Govind\Documents\Sustainability\Year2\Spring\GIS5090\Projects\FinalProj\Final_python\Output", "timeline.gdb")


#Building the Mosaic Dataset
##import arcpy
##arcpy.env.workspace = "C:\Users\Govind\Documents\Sustainability\Year2\Spring\GIS5090\Projects\FinalProj\Final_python\Output"
##
###import variables
##gdbName = r"C:\Users\Govind\Documents\Sustainability\Year2\Spring\GIS5090\Projects\FinalProj\Final_python\Output\timeline.gdb"
##mdName = "campusTimeline"
##sr = "3857"
##numBands = 3
##pixelType = "16_Bit_Unsigned"
##productDef = "NATURAL_COLOR_RGB"
##waveLength = ""

#arcpy.CreateMosaicDataset_management(gdbName, mdName, sr, numBands, pixelType, waveLength)


#Adding Raster to Mosaic Dataset
##import arcpy
##arcpy.env.workspace = "C:\Users\Govind\Documents\Sustainability\Year2\Spring"
##
##mdname = r"C:\Users\Govind\Documents\Sustainability\Year2\Spring\GIS5090\Projects\FinalProj\Final_python\Output\timeline.gdb\campusTimeline"
##rastType ="Raster Dataset"
##inputPath = r"C:\Users\Govind\Documents\Sustainability\Year2\Spring\GIS5970\Mizzou_maps\SLU_sanborn.gdb\Campus_Images.gdb\FinalMos"
##updateCs = "UPDATE_CELL_SIZES"
##updatebnd = "UPDATE_BOUNDARY"
##updateovr = "UPDATE_OVERVIEWS"
##maxlevel = "-1"
##maxcs = "#"
##maxdim = "#"
##spatialref = "#"
##inputdatafilter = "#"
##subfolder = "SUBFOLDERS"
##duplicates = "OVERWRITE_DUPLICATES"
##calStatistics = "CALCULATE_STATISTICS"
##pyramids = "BUILD_PYRAMIDS"
##thumbnails = "NO_THUMBNAILS"
##caption = "Raster of SLU Campus 1909"
##forcesr = "NO_FORCE_SPATIAL_REFERENCE"

#arcpy.AddRastersToMosaicDataset_management(mdname, rastType, inputPath, updateCs, updatebnd, updateovr, maxlevel, maxcs, maxdim, spatialref, inputdatafilter, subfolder, duplicates, pyramids, calStatistics, thumbnails, caption, forcesr)

