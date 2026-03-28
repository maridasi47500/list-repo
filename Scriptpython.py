import requests

def list_github_repos(username, token=None):
    """
    List all public repositories of a GitHub user.
    
    :param username: GitHub username (string)
    :param token: Optional GitHub Personal Access Token for higher rate limits
    :return: List of repository names
    """
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Username must be a non-empty string.")

    url = f"https://api.github.com/users/{username}/repos"
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


if __name__ == "__main__":
    # Example usage
    user = input("Enter GitHub username: ").strip()
    # Optional: token = "your_personal_access_token_here"
    token = None  # Set to your token string if you have one

    repos = list_github_repos(user, token)
    if repos:
        print(f"\nPublic repositories of '{user}':")
        for repo in repos:
            print(f"- {repo}")
    else:
        print("No repositories found or an error occurred.")
