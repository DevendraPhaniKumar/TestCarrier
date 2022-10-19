# pic6-rest-api

## Dependencies
- pycurl: http://pycurl.io/
  - Although not currently used, this will be required to implement binary/file upload/download in the near future
  
## Current Features:
- init: setup server location
- login: login with given credentials
- logout: logout of currently logged in account
- read: read single database point
- read_list: read list of database points
- write: write database point
- write_list: write list of database points
- get_upgrade_status: will return download/upgrade status
- get_version_info: return version of hardware & FW
- keep_alive: infinite loop to keep alive connection...write stop_keep_alive True to stop
- initiate_upgrade: Will prompt for file selection or use provided file based on path to upgrade PIC6
