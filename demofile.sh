
mkdir templates 
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py country name
python3 scaffold.py dependency name  description
python3 scaffold.py dependency_data dependency_id:references attribute value
python3 scaffold.py package name description
python3 scaffold.py package_data dependency_id:references attribute value
python3 scaffold.py commandline_load_dependency user_id:references dependency_id:references datetime  terminal_console_id:references  datetime datetime_end complete:radio
python3 scaffold.py commandline_load_package user_id:references package_id:references datetime complete:radio  terminal_console_id:references datetime_end
python3 scaffold.py terminal_console lat lon  name
python3 scaffold.py terminal_console_status status terminal_console_id:references user_id:references
