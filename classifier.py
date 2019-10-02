# Copyright 2018 by Issam R.S ALmustafa, The James Hutton Institute.
#All rights reserved.
# This module is a  Classifier Tool used to sort out the different .sac files to thier corresponding folder
# As part of the job requirement

############################ Include modules here ############################################################

import os			# Import OS module 
import shutil			# Import shutil module 

###############################################################################################################

########################### Defining GLobal variables here   ##################################################
stations={'BANCO':'path',.....}
source_path = os.getcwd() 			#Get current directly path
#print(source_path)				#Print current directory path to verify
dest_path = source_path + '/BANCO'		#Specify the destination path
#print(destination_path)			#Print the the destination path to verify 
content = os.listdir(source_path)		#Save listed files and folders inside files list 

########################### Code starts here ###################################################################


sac_files = [i for i in content if i.endswith('.sac')]   #Save only .sac files in this list

if len(sac_files)==0:		       		#Check if list is empty
  print("No sac files in directory")   		#Print error message
else:
  for file in sac_files:     	       		#Walk through the list of sac_files
    print(file)		   	       		#Print every element in the list
    name=file.split('_')               		#Split the file name into sections and save them inside name
    station=name[5]		       		#Get the 6th element and save it inside station
    #print(station)	  	       		#Print the station name
    if station=="BANCO":
      print("BANCO station found")     		#Display message if Banco station found
      MovFrom = source_path +'/'+file  		#Specify complete file path
      MovTo = dest_path + '/' + file            #Specify destination file path
      #print(MovFrom)				#Print to verify       			
      #print(MovTo)                             #Print to verify	
      shutil.move(MovFrom,MovTo)		#Move the file to its corresponding folder
      


