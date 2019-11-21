'''
Heat Map of Artists Hometown's of Top Releases per Genre of Music
A map depicting the top releases per a genre of music with geocoded artist hometown sites as heatmap analysis
'''

# cmd lines
# cd Z:GIS220\Final
# MidWestEmoChart.csv

import arcpy


def main():
    workspace = "Z:\GIS220\Final"
    
    if arcpy.Exists("Z:\GIS220\Final\MidWestEmo.gdb"):
        print("gdb already exists")
    else:
        # Execute CreateFileGDB
        arcpy.CreateFileGDB_management(workspace, "MidWestEmo.gdb")
        print("gdb created")

    # Create Address Locator
    arcpy.CreateAddressLocator_geocoding("General — City State Country", "MidWestEmoChart.csv", "'Feature ID' FeatureID VISIBLE NONE;'*From Left' L_F_ADD VISIBLE NONE;'*To Left' L_T_ADD VISIBLE NONE;'*From Right' R_F_ADD VISIBLE NONE;'*To Right' R_T_ADD VISIBLE NONE;'Prefix Direction' PREFIX VISIBLE NONE;'Prefix Type' PRE_TYPE VISIBLE NONE;'*Street Name' NAME VISIBLE NONE;'Suffix Type' TYPE VISIBLE NONE;'Suffix Direction' SUFFIX VISIBLE NONE;'Left City or Place' CITYL VISIBLE NONE;'Right City or Place' CITYR VISIBLE NONE;'Left Zipcode' ZIPL VISIBLE NONE;'Right Zipcode' ZIPR VISIBLE NONE;'Left State' State_Abbr VISIBLE NONE;'Right State' State_Abbr VISIBLE NONE", Atlanta_AddressLocator, "", "DISABLED")

    # Read Excel file into FileGeodatabase
    
    
    
    # Read csv of Hometowns w/ headers into dictionary
        #csv.DictReader
    
    # Read csv of latLon w/ headers into dictionary
    
    # For hometown_line in hometowns: 
        # For latLon_line in latLon
            # if hometowns["city"] in latLon.values():
                # write to new csv 
                
                # FIND FUNCTION THAT DOES CROSS PRODUCT OF LISTS

    # Loop through feature class and update hometowns into addresses

    # Search for null address

    # Write a log file of addresses that were updated

    # Display point data

    # Create heat map layer from point data

    # Display points and heat map layer on map

main()
