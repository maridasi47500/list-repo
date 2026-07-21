mkdir -p templates
python3 scaffold.py langue_orientale name
python3 scaffold.py personne name dateofbirth langue_orientale_id secteur_id salaire experience
python3 scaffold.py secteur name
python3 scaffold.py city_name
python3 scaffold.py future_stuff stuff_type name pic user_id
python3 scaffold.py job name
python3 scaffold.py peoplehasjob person_id job_id
