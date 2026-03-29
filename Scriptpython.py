import requests
import subprocess
from flask import Flask, render_template, request

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
    repo_names = [repo["name"] for repo in repos_data]
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
        bdd=request.form["bdd"].split("\n")


        with open("pleasecopynow"+repo+".sh", "w") as f:
            f.write("echo 'banana'")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("echo \"`cat << EOF")

        for x in bdd:
            if len(x.strip()) > 0:
                with open("pleasecopynow"+repo+".sh", "a") as f:
                    f.write("\npython3 scaffold.py "+x)
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("EOF`\" > \"$1/demofile.sh\"")





        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\ncp scaffold.py ~/")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\ncp hellopython.sh ~/")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nalias proj=\"(cd ~ && . ./hellopython.sh "+repo+")\"")
        with open("pleasecopynow"+repo+".sh", "a") as f:
            f.write("\nproj")


    else:
        bdd=[]



    return render_template("crawler.html", readme=myreadme, repo=repo, username=user)

if __name__ == "__main__":
    app.run()
    app.debug = True

