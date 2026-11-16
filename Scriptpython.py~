import requests
import os
import subprocess
import string
import random
from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import json
import re


def parse_sql_to_dict(sql_script: str) -> dict:
  schema = {}

  # 1. Capture chaque bloc CREATE TABLE (nom de la table + contenu entre parenthèses)
  table_pattern = re.compile(
      r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([a-zA-Z_][a-zA-Z0-9_]*)\s*\((.*?)\)\s*;",
      re.IGNORECASE | re.DOTALL,
  )

  # 2. Capture le nom de la colonne et son type au début de chaque définition
  column_pattern = re.compile(
      r"^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z]+(?:\(\d+(?:,\s*\d+)?\))?)",
      re.IGNORECASE,
  )

  # Mots-clés SQL désignant des contraintes de table et non des colonnes
  table_constraints = {
      "PRIMARY",
      "FOREIGN",
      "UNIQUE",
      "CHECK",
      "CONSTRAINT",
  }

  for table_match in table_pattern.finditer(sql_script):
    table_name = table_match.group(1)
    body = table_match.group(2)
    schema[table_name] = {}

    # Découpe les définitions par virgule (en ignorant les virgules à l'intérieur des parenthèses, ex: PRIMARY KEY (a, b))
    definitions = re.split(r",(?![^()]*\))", body)

    for definition in definitions:
      col_match = column_pattern.match(definition)
      if col_match:
        col_name, col_type = col_match.groups()
        if col_name.upper() not in table_constraints:
          schema[table_name][col_name] = col_type

  return schema







def list_github_repos(username, token=None,pagenumber=1):
    """
    List all public repositories of a GitHub user.
    
    :param username: GitHub username (string)
    :param token: Optional GitHub Personal Access Token for higher rate limits
    :return: List of repository names
    """
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Username must be a non-empty string.")

    url = f"https://api.github.com/users/{username}/repos?page={pagenumber}"
    print(url)
    headers = {}
    
    # If token is provided, use it for authentication
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []

    repos_data = response.json()
    # Extract repository names
    repo_names = [{"name":repo["name"], "size":repo["size"],"language":repo["language"], "description":repo["description"]} for repo in repos_data]
    return repo_names






app = Flask(__name__)




@app.route("/")
def index():
    try:
        user = request.args.get("username")
        print("option 1", user)
    except:
        user = ""
        print("option 2")
    try:
        pageno = request.args.get("pageno")
        print("option 1", pageno)
    except:
        pageno = "1"
        print("option 2")
    if pageno is None:
        pageno = "1"
  
    # Optional: token = "your_personal_access_token_here"
    token = None  # Set to your token string if you have one



    if user is not None and user != "":
        repos = list_github_repos(user, token,pageno)
        if repos:

            print(f"\nPublic repositories of '{user}':")
            for repo in repos:
                print(f"- {repo}")
        else:
            print("No repositories found or an error occurred.")
            repos=[]
    else:
        print("No repositories found or an error occurred.")
        repos=[]
    return render_template("index.html", repos=repos, username=user,pageno=pageno)


@app.route("/crawler", methods=['GET', 'POST'])
def crawler():
    # Example usage
    try:
        user = request.args.get("username")
    except:
        user = ""
    try:
        pageno = request.args.get("pageno")
    except:
        pageno=""
    try:
        repo = request.args.get("repo")
    except:
        repo=""
    url="https://raw.githubusercontent.com/"+user+"/"+repo+"/refs/heads/main/README.md"
    print(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

    myreadme = response.text
    if request.method == 'POST':
        debutmot=request.form["debutmot"].strip()
        finmot=request.form["finmot"].strip()
        bdd=request.form["bdd"].split("\n")


        with open("pleasecopynow"+repo+".sh", "w") as f:
            f.write("#!/bin/bash")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\necho 'banana'")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\necho \"`cat << EOF\n")

        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nmkdir templates ")
        for x in bdd:
            if len(x.strip()) > 0:
                with open("pleasecopynow"+repo+".sh", "a") as f:
                    f.write("\npython3 scaffold.py "+x.strip())
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nEOF`\" > \"./demofile.sh\"")





        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\ncp scaffold.py ~/")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\ncp hellopython.sh ~/")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nalias proj=\"(cd ~ && . ./hellopython.sh '"+repo+"' \'debut de mes mots: "+debutmot.strip().replace("\"","").replace("'","")+"\' \'fin de mes mots : "+finmot.strip().replace("'","").replace("\"","")+"\')\"")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nproj")


    else:
        bdd=[]



    return render_template("crawler.html", readme=myreadme, repo=repo, username=user, pageno=pageno)

@app.route("/crawlerpic", methods=['GET', 'POST'])
def crawlerpic():
    # Example usage
    try:
        user = request.args.get("username")
    except:
        user = ""
    try:
        pageno = request.args.get("pageno")
    except:
        pageno=""
    try:
        repo = request.args.get("repo")
    except:
        repo=""
    url="https://raw.githubusercontent.com/"+user+"/"+repo+"/refs/heads/main/README.md"
    print(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

    myreadme = response.text
    if request.method == 'POST':
        try:
            pic=request.files["pic"]
            #char_set = string.ascii_uppercase + string.digits
            char_set="azertyuiopqsdfghjklmwxcvbn1234567890"
            myfilename=''.join(random.sample(char_set*6, 8))+"."+pic.filename.split('.')[-1]
            if pic.filename != '':
                pic.save(os.path.join('C:\\', 'Users', os.getlogin(), repo, "static", secure_filename(myfilename)))
            #pic.save(os.path.join('C:\\', 'Utilisateurs', os.getlogin(), repo, "static", secure_filename("hellothere")))
            #print("haha")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "templates", "hey.html"), "a") as f:
                f.write("\n<img src=\""+myfilename+"\" width=\"100px\" height=\"100px\">")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "README.md"), "a") as f:
                f.write("\n![alt text](./static/"+myfilename+")")
        except Exception as e:
            print("exception ", str(e))




    else:
        bdd=[]



    return render_template("crawlerpic.html", readme=myreadme, repo=repo, username=user, pageno=pageno)

@app.route("/crawlerdescription", methods=['GET', 'POST'])
def crawlerdescription():
    mylist=["gps", "job ready", "boule de crystal","wifi","4g","bluetooth", "base de données", "art of coding", "traducteur","langue étrangère", "voyage", "partition de musique lilypond", "ruby", "python", "musician story", "musique classique", "réseau social","météo","actualités", "titres de musique","jouer de la musique","fake", "cookbook"]# Example usage
    try:
        user = request.args.get("username")
    except:
        user = ""
    try:
        pageno = request.args.get("pageno")
    except:
        pageno=""
    try:
        repo = request.args.get("repo")
    except:
        repo=""
    url="https://raw.githubusercontent.com/"+user+"/"+repo+"/refs/heads/main/README.md"
    print(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

    myreadme = response.text
    if request.method == 'POST':
        try:
            lieu=request.form["lieu"]
            programme=request.form["programming"]
            commonactions=request.form["commonactions"]
            unusualactions=request.form["unusualactions"]
             
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "w") as f:
                f.write("- lieu : "+lieu+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- common actions : "+commonactions+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- unusual actions : "+unusualactions+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- ce que je veux programmer : "+programme+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n| property name/clé | oui/non/valeur/détails |")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n| :---------------- | :------: |")
            for w in mylist:
                with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                    f.write("\n| "+w+"       | "+request.form[w.replace(" ", "_")]+" "+request.form[w.replace(" ", "_")+"description"]+" |")
                
        except Exception as e:
            print("exception ", str(e))




    else:
        bdd=[]



    return render_template("crawlerdescription.html",mylist=mylist, readme=myreadme, repo=repo, username=user, pageno=pageno)

@app.route("/crawlerdb", methods=['GET', 'POST'])
def crawlerdb():
    mylist=["gps", "job ready", "boule de crystal","wifi","4g","bluetooth", "base de données", "art of coding", "traducteur","langue étrangère", "voyage", "partition de musique lilypond", "ruby", "python", "musician story", "musique classique", "réseau social","météo","actualités", "titres de musique","jouer de la musique","fake", "cookbook"]# Example usage
    try:
        user = request.args.get("username")
    except:
        user = ""
    try:
        pageno = request.args.get("pageno")
    except:
        pageno=""
    try:
        repo = request.args.get("repo")
    except:
        repo=""
    url="https://raw.githubusercontent.com/"+user+"/"+repo+"/refs/heads/main/README.md"
    url2="https://raw.githubusercontent.com/"+user+"/"+repo+"/refs/heads/main/schema.sql"
    print(url)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

    myreadme = response.text
    print(url2)
    try:
        response2 = requests.get(url2, timeout=10)
        response2.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

    myschema = response2.text
    if request.method == 'POST':
        try:
            lieu=request.form["lieu"]
            programme=request.form["programming"]
            commonactions=request.form["commonactions"]
            unusualactions=request.form["unusualactions"]
             
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "w") as f:
                f.write("- lieu : "+lieu+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- common actions : "+commonactions+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- unusual actions : "+unusualactions+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n- ce que je veux programmer : "+programme+"")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n| property name/clé | oui/non/valeur/détails |")
            with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                f.write("\n| :---------------- | :------: |")
            for w in mylist:
                with open(os.path.join('C:\\','Users',os.getlogin(), repo, "DESCRIPTION.md"), "a") as f:
                    f.write("\n| "+w+"       | "+request.form[w.replace(" ", "_")]+" "+request.form[w.replace(" ", "_")+"description"]+" |")
        except Exception as e:
            print("exception ", str(e))
    result = parse_sql_to_dict(myschema)
    print(json.dumps(result, indent=2))
    awesomelist=[
    "https://getbootstrap.com/docs/6.0/forms/checkbox/",
    "https://getbootstrap.com/docs/6.0/forms/checkbox/",
    "https://getbootstrap.com/docs/6.0/components/card/#card-groups",
    "https://getbootstrap.com/docs/6.0/components/card/",
    "https://getbootstrap.com/docs/6.0/forms/switch/",
    "https://getbootstrap.com/docs/6.0/forms/radio/",
    "https://getbootstrap.com/docs/6.0/getting-started/install",
    "https://getbootstrap.com/docs/6.0/getting-started/ai",
    "https://getbootstrap.com/docs/6.0/getting-started/approach",
    "https://getbootstrap.com/docs/6.0/getting-started/css-variables",
    "https://getbootstrap.com/docs/6.0/getting-started/javascript",
    "https://getbootstrap.com/docs/6.0/getting-started/browsers-devices",
    "https://getbootstrap.com/docs/6.0/getting-started/accessibility",
    "https://getbootstrap.com/docs/6.0/guides/quickstart",
    "https://getbootstrap.com/docs/6.0/guides/npm",
    "https://getbootstrap.com/docs/6.0/guides/webpack",
    "https://getbootstrap.com/docs/6.0/guides/parcel",
    "https://getbootstrap.com/docs/6.0/guides/vite",
    "https://getbootstrap.com/docs/6.0/guides/contribute",
    "https://getbootstrap.com/docs/6.0/guides/migration",
    "https://getbootstrap.com/docs/6.0/customize/overview",
    "https://getbootstrap.com/docs/6.0/customize/sass",
    "https://getbootstrap.com/docs/6.0/customize/options",
    "https://getbootstrap.com/docs/6.0/customize/color",
    "https://getbootstrap.com/docs/6.0/customize/theme",
    "https://getbootstrap.com/docs/6.0/customize/color-modes",
    "https://getbootstrap.com/docs/6.0/customize/components",
    "https://getbootstrap.com/docs/6.0/customize/transitions",
    "https://getbootstrap.com/docs/6.0/customize/rtl",
    "https://getbootstrap.com/docs/6.0/customize/optimize",
    "https://getbootstrap.com/docs/6.0/layout/breakpoints",
    "https://getbootstrap.com/docs/6.0/layout/containers",
    "https://getbootstrap.com/docs/6.0/layout/grid",
    "https://getbootstrap.com/docs/6.0/layout/columns",
    "https://getbootstrap.com/docs/6.0/layout/gutters",
    "https://getbootstrap.com/docs/6.0/layout/utilities",
    "https://getbootstrap.com/docs/6.0/layout/z-index",
    "https://getbootstrap.com/docs/6.0/layout/css-grid",
    "https://getbootstrap.com/docs/6.0/content/reboot",
    "https://getbootstrap.com/docs/6.0/content/typography",
    "https://getbootstrap.com/docs/6.0/content/images",
    "https://getbootstrap.com/docs/6.0/content/tables",
    "https://getbootstrap.com/docs/6.0/content/prose",
    "https://getbootstrap.com/docs/6.0/forms/overview",
    "https://getbootstrap.com/docs/6.0/forms/field",
    "https://getbootstrap.com/docs/6.0/forms/form-control",
    "https://getbootstrap.com/docs/6.0/forms/checkbox",
    "https://getbootstrap.com/docs/6.0/forms/radio",
    "https://getbootstrap.com/docs/6.0/forms/switch",
    "https://getbootstrap.com/docs/6.0/forms/range",
    "https://getbootstrap.com/docs/6.0/forms/input-group",
    "https://getbootstrap.com/docs/6.0/forms/floating-labels",
    "https://getbootstrap.com/docs/6.0/forms/form-adorn",
    "https://getbootstrap.com/docs/6.0/forms/chips",
    "https://getbootstrap.com/docs/6.0/forms/combobox",
    "https://getbootstrap.com/docs/6.0/forms/datepicker",
    "https://getbootstrap.com/docs/6.0/forms/otp-input",
    "https://getbootstrap.com/docs/6.0/forms/password-strength",
    "https://getbootstrap.com/docs/6.0/forms/layout",
    "https://getbootstrap.com/docs/6.0/forms/validation",
    "https://getbootstrap.com/docs/6.0/components/accordion",
    "https://getbootstrap.com/docs/6.0/components/alert",
    "https://getbootstrap.com/docs/6.0/components/avatar",
    "https://getbootstrap.com/docs/6.0/components/badge",
    "https://getbootstrap.com/docs/6.0/components/breadcrumb",
    "https://getbootstrap.com/docs/6.0/components/button",
    "https://getbootstrap.com/docs/6.0/components/button-group",
    "https://getbootstrap.com/docs/6.0/components/card",
    "https://getbootstrap.com/docs/6.0/components/carousel",
    "https://getbootstrap.com/docs/6.0/components/close-button",
    "https://getbootstrap.com/docs/6.0/components/collapse",
    "https://getbootstrap.com/docs/6.0/components/dialog",
    "https://getbootstrap.com/docs/6.0/components/drawer",
    "https://getbootstrap.com/docs/6.0/components/list-group",
    "https://getbootstrap.com/docs/6.0/components/menu",
    "https://getbootstrap.com/docs/6.0/components/nav",
    "https://getbootstrap.com/docs/6.0/components/nav-overflow",
    "https://getbootstrap.com/docs/6.0/components/navbar",
    "https://getbootstrap.com/docs/6.0/components/pagination",
    "https://getbootstrap.com/docs/6.0/components/placeholder",
    "https://getbootstrap.com/docs/6.0/components/popover",
    "https://getbootstrap.com/docs/6.0/components/progress",
    "https://getbootstrap.com/docs/6.0/components/scrollspy",
    "https://getbootstrap.com/docs/6.0/components/spinner",
    "https://getbootstrap.com/docs/6.0/components/stepper",
    "https://getbootstrap.com/docs/6.0/components/tab",
    "https://getbootstrap.com/docs/6.0/components/toasts",
    "https://getbootstrap.com/docs/6.0/components/toggler",
    "https://getbootstrap.com/docs/6.0/components/tooltip",
    "https://getbootstrap.com/docs/6.0/helpers/focus-ring",
    "https://getbootstrap.com/docs/6.0/helpers/hover-lift",
    "https://getbootstrap.com/docs/6.0/helpers/icon-link",
    "https://getbootstrap.com/docs/6.0/helpers/position",
    "https://getbootstrap.com/docs/6.0/helpers/stacks",
    "https://getbootstrap.com/docs/6.0/helpers/stretched-link",
    "https://getbootstrap.com/docs/6.0/helpers/text-truncation",
    "https://getbootstrap.com/docs/6.0/helpers/vertical-rule",
    "https://getbootstrap.com/docs/6.0/helpers/visually-hidden",
    "https://getbootstrap.com/docs/6.0/utilities/api",
    "https://getbootstrap.com/docs/6.0/utilities/colors",
    "https://getbootstrap.com/docs/6.0/utilities/background",
    "https://getbootstrap.com/docs/6.0/utilities/color-scheme",
    "https://getbootstrap.com/docs/6.0/utilities/theme",
    "https://getbootstrap.com/docs/6.0/utilities/aspect-ratio",
    "https://getbootstrap.com/docs/6.0/utilities/container-queries",
    "https://getbootstrap.com/docs/6.0/utilities/display",
    "https://getbootstrap.com/docs/6.0/utilities/float",
    "https://getbootstrap.com/docs/6.0/utilities/object-fit",
    "https://getbootstrap.com/docs/6.0/utilities/overflow",
    "https://getbootstrap.com/docs/6.0/utilities/position",
    "https://getbootstrap.com/docs/6.0/utilities/visibility",
    "https://getbootstrap.com/docs/6.0/utilities/z-index",
    "https://getbootstrap.com/docs/6.0/utilities/align-content",
    "https://getbootstrap.com/docs/6.0/utilities/align-items",
    "https://getbootstrap.com/docs/6.0/utilities/align-self",
    "https://getbootstrap.com/docs/6.0/utilities/flex",
    "https://getbootstrap.com/docs/6.0/utilities/gap",
    "https://getbootstrap.com/docs/6.0/utilities/grid",
    "https://getbootstrap.com/docs/6.0/utilities/justify-content",
    "https://getbootstrap.com/docs/6.0/utilities/justify-items",
    "https://getbootstrap.com/docs/6.0/utilities/place-items",
    "https://getbootstrap.com/docs/6.0/utilities/width",
    "https://getbootstrap.com/docs/6.0/utilities/height",
    "https://getbootstrap.com/docs/6.0/utilities/margin",
    "https://getbootstrap.com/docs/6.0/utilities/padding",
    "https://getbootstrap.com/docs/6.0/utilities/space",
    "https://getbootstrap.com/docs/6.0/utilities/font-family",
    "https://getbootstrap.com/docs/6.0/utilities/font-size",
    "https://getbootstrap.com/docs/6.0/utilities/font-style",
    "https://getbootstrap.com/docs/6.0/utilities/font-weight",
    "https://getbootstrap.com/docs/6.0/utilities/line-height",
    "https://getbootstrap.com/docs/6.0/utilities/link",
    "https://getbootstrap.com/docs/6.0/utilities/text-alignment",
    "https://getbootstrap.com/docs/6.0/utilities/text-decoration",
    "https://getbootstrap.com/docs/6.0/utilities/text-transform",
    "https://getbootstrap.com/docs/6.0/utilities/text-wrapping",
    "https://getbootstrap.com/docs/6.0/utilities/vertical-align",
    "https://getbootstrap.com/docs/6.0/utilities/border",
    "https://getbootstrap.com/docs/6.0/utilities/border-color",
    "https://getbootstrap.com/docs/6.0/utilities/border-radius",
    "https://getbootstrap.com/docs/6.0/utilities/divide",
    "https://getbootstrap.com/docs/6.0/utilities/pointer-events",
    "https://getbootstrap.com/docs/6.0/utilities/user-select",
    "https://getbootstrap.com/docs/6.0/utilities/motion",
    "https://getbootstrap.com/docs/6.0/utilities/opacity",
    "https://getbootstrap.com/docs/6.0/utilities/shadows",
    "https://getbootstrap.com/docs/6.0/forms/form-control/",
    "https://getbootstrap.com/docs/6.0/forms/radio/",
    "https://getbootstrap.com/docs/6.0/",
    "https://getbootstrap.com/docs/6.0/examples",
    "https://getbootstrap.com/docs/6.0/getting-started",
    "https://getbootstrap.com/docs/6.0/examples/starter-template",
    "https://getbootstrap.com/docs/6.0/guides/webpack",
    "https://getbootstrap.com/docs/6.0/guides/parcel",
    "https://getbootstrap.com/docs/6.0/guides/vite"]
    return render_template("crawlerdb.html",awesomelist=awesomelist,schema=result, mylist=mylist, readme=myreadme, repo=repo, username=user, pageno=pageno)

if __name__ == "__main__":
    app.run()
    app.debug = True

