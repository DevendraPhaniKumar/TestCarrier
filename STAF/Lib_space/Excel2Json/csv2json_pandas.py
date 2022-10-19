import pandas as pd
import json

filename = ("D:\other\Excel2Json\System_Start_Stop_TC1_2.csv")
output  = open('temp.json', 'w')

records = pd.DataFrame(pd.read_csv(filename)).to_dict('records')
dict = {}

for i in range(len(records)):
    dict["TestCase"+str(i+1)] = {"Data" : records[i]}

output.write(json.dumps(dict, sort_keys=True, indent=2,  separators=(',', ": ")))
output.close()