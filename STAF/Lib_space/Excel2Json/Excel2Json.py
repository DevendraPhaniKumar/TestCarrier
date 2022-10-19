#  UTC Building & Industrial Systems PROPRIETARY INFORMATION
#  This document contains technical data subject to Export
#  Administration Regulation. U.S. ECCN: EAR99
#  Copyright (c) 2017 - Carrier
##
# Package and Module Imports
import xlrd
import json
import os.path
import datetime

def getColNames(sheet):
    rowSize = sheet.row_len(0)
    colValues = sheet.row_values(0, 0, rowSize )
    columnNames = []

    for value in (colValues):
        columnNames.append(value)

    return columnNames

def getRowData(row, columnNames):
    rowData = []
    rowData_dict = {}
    dict1 = {}; dict2 = {}
    counter = 0

    for cell in row:
        # check if it is of date type print in iso format
        if cell.ctype==xlrd.XL_CELL_DATE:
            rowData[columnNames[counter].lower().replace(' ', '_')] = datetime.datetime(*xlrd.xldate_as_tuple(cell.value,0)).isoformat()
        elif columnNames[counter] != 'TestcaseNo' and columnNames[counter] != 'Test Discription':
			if cell.value == int(cell.value):
				value =  int(cell.value)
			else:
				value =  cell.value
			# rowData[columnNames[counter].lower().replace(' ', '_')] = cell.value
			rowData.append(value)
			data = columnNames[counter]
			dict1[data] = (value)
        # rowData_dict["Data"] = rowData[1:]
        counter += 1
    dict2["Data"] = dict1
    return dict2

def getSheetData(sheet, columnNames):
    nRows = sheet.nrows
    sheetData = []
    workbookdata = {}
    counter = 1

    for idx in range(1, nRows):
        row = sheet.row(idx)
        rowData_dict = getRowData(row, columnNames)
        workbookdata["TestCases"+str(idx)] = rowData_dict

    return workbookdata

def getWorkBookData(workbook):
    nsheets = workbook.nsheets

    for idx in range(0, nsheets):
        worksheet = workbook.sheet_by_index(idx)
        columnNames = getColNames(worksheet)
        workbookdata = getSheetData(worksheet, columnNames)
    return workbookdata

def convert(filename):
    # filename = raw_input("Enter the path to the filename -> ")
    if os.path.isfile(filename):
        workbook = xlrd.open_workbook(filename)
        workbookdata = getWorkBookData(workbook)
        output = \
        open((filename.replace("xlsx", "json")).replace("xls", "json"), "wb")
        output.write(json.dumps(workbookdata, sort_keys=True, indent=2,  separators=(',', ": ")))
        output.close()
        print ("%s was created" %output.name)
    else:
        print("Sorry, that was not a valid filename")