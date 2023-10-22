# import math
# thing = {}
# if(thing):
#     print(math.floor(2.9))

def Select_Reports(command_line_args:dict[str,str], possibleReports:dict[str,list[str]]):
    if command_line_args["report_selector"]: 
        reports = filter(lambda x: command_line_args["report_selector"] in x, possibleReports[command_line_args["integration_type"]])
        if not reports:
            raise Exception(f'Report type name {command_line_args["report_selector"]} did not match any report types')
    else: reports = possibleReports[command_line_args["integration_type"]]
    return reports


# command_line_args["integration_type"]:str = "Single" if sys.argv[1] == "Single" else "Cons"
# command_line_args["generateBaseline"]:bool = False if sys.argv[-1] != '-b' else True
# command_line_args["report_selector"] = sys.argv[2] if len(sys.argv) > 2 else None
args = ["", "Single", "Custom"]

command_line_args= {"integration_type": "Single" if args[1] == "Single" else "Cons", 
                    "generateBaseline": False if args[-1] != '-b' else True,
                    "report_selector": args[2] if len(args) > 2 else None
                     }
possibleReports: dict[str,list[str]] = {
           "Single": ["CSV", "QBD_Accr", "QBO_Accr", "Xero_Accr", "Custom"],  #["CSV", "QBD_Accr","QBD_Cash", "QBO_Accr","QBO_Cash", "Xero_Accr", "Xero_Cash"]
           "Cons": ["QBCD_NE_BA_NCC_Accr"]
           }
basePath = r'c:\Users\aamrl\OneDrive\Desktop\REACH'
BaselinesAndNewDownloadsPath = fr'{basePath}\PDF_SNAPSHOTS\{command_line_args["integration_type"]}_Companies\BaseLinesAndNewDownloads'

reports = Select_Reports(command_line_args, possibleReports)

print((reports))