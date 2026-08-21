
mkdir templates 
python3 scaffold.py country name
python3 scaffold.py user username email phone password country_id:references
python3 scaffold.py city name country_id:references
python3 scaffold.py destination budget city_id:references emotional_state
python3 scaffold.py job name
python3 scaffold.py set_yourself user_id:references what_you_re_great_at_doing
python3 scaffold.py help_other advice_type user_id:references otheruser_id:references content
python3 scaffold.py dreamjob user_id:references job_id:references
python3 scaffold.py career_relationship user_id:references content
python3 scaffold.py connectpeople user_id:references otheruser_id:references values emotional_goals
