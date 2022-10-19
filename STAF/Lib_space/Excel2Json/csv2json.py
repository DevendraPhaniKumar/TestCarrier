#  UTC Building & Industrial Systems PROPRIETARY INFORMATION
#  This document contains technical data subject to Export
#  Administration Regulation. U.S. ECCN: EAR99
#  Copyright (c) 2017 - Carrier
##
# Package and Module Imports

import csv
import json
import os.path

def convert(filename):
    if os.path.isfile(filename):
        dict = {}
        input_file = csv.DictReader(open(filename))
        counter = 0
        print(input_file)
        
        for row in input_file:
            counter += 1
            dict["TestCases" + str(counter)] = {"Data": row}

        output = \
        open((filename.replace("csv", "json")).replace("csv", "json"), "w", encoding="utf8")
        output.write(json.dumps(dict, sort_keys=True, indent=2,  separators=(',', ": ")))
        #output.close()
        print ("%s was created" %output.name)
    else:
        print ("Sorry, that was not a valid filename")
# convert("D:\other\Excel2Json\Control_Point_TC.csv")
