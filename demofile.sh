
touch templates/base.html
touch templates/hey.html
mkdir templates 
python3 scaffold.py user username email password phone country_id
python3 scaffold.py country name
python3 scaffold.py cat name
python3 scaffold.py photo country_id cat_id pic
python3 scaffold.py songs country_id title artist music
python3 scaffold.py likes user_id photo_id
python3 scaffold.py likesongs user_id song_id
