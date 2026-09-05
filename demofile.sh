
mkdir templates 
python3 scaffold.py country name
python3 scaffold.py city country_id:references name
python3 scaffold.py fiddle_type name
python3 scaffold.py city_travel city_id:references fiddle_type_id:references title composer artist score:staff time_signature key_signature pic
