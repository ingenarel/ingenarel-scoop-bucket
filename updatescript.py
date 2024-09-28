import requests, hashlib, json

def git_project_latest_commit_hash_check(
    name_and_repo:str,
    provider:str,
    project_id=None
    ) -> str:
    """
    This checks a git project and returns the latest commit hash.
    the name_and_repo is for the name and the repo.
    the provider is a git hosting provider, it currently supports github, and gitlab
    if the provider is gitlab, you need to give the project_id.
    """
    provider = provider.strip().lower()
    if provider == "github":
        return requests.get(f"https://api.github.com/repos/{name_and_repo}/commits").json()[0]["sha"]
    elif provider == "gitlab":
        return requests.get(f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits").json()[0]["id"]

def git_project_latest_zip_hash_check(
        name_and_repo:str,
        branch:str,
        provider:str,
        project_name=None
    ) -> str:
    """
    This checks a git project and returns the latest git repo's zip file's hash.
    The provider is a git hosting provider. it currently supports github and gitlab.
    if it's something else, it raises a NotImplementedError.
    the branch is the branch it should check,
    the the provider is github, then the name_and_repo is the project owner's name and the repo name.
    if the provider is gitlab, then the name_and_repo is the project id,
    and you would also need to provide the package_name variable, which is the repo name.
    """
    if provider == "github":
        git_project_latest_zip_hash_url = f"https://github.com/{name_and_repo}/archive/refs/heads/{branch}.zip"
    elif provider == "gitlab":
        git_project_latest_zip_hash_url = f"https://gitlab.com/{name_and_repo}/-/archive/{branch}/heads/{project_name}-{branch}.zip"
    else:
        raise NotImplementedError
    
    # chatgpt written code starts here
    hash_obj = hashlib.new('sha256')
    with requests.get(git_project_latest_zip_hash_url, stream=True) as response:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
    return hash_obj.hexdigest()
    # chatgpt written code ends here

def read_project_commit_hash(package_name:str) -> str:
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return data["version"]

def read_project_zip_hash(package_name:str) -> str:
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return data["hash"]

def write_project_commit_hash(package_name:str, commit_hash:str):
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    data["version"] = commit_hash
    with open(f"bucket/{package_name}.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
    print(f"{package_name} commit hash changed to {commit_hash}")

def write_project_zip_hash(package_name:str, zip_hash:str):
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    data["hash"] = zip_hash
    with open(f"bucket/{package_name}.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
    print(f"{package_name} zip hash changed to {zip_hash}")

def main():
    list_of_github_projects = (
        {
            "name_and_repo": "ayn2op/discordo",
            "package_name": "discordo-git",
            "branch": "main",
        },
        {
            "name_and_repo": "jesseduffield/lazygit",
            "package_name": "lazygit-git",
            "branch": "master",
        },
        {
            "name_and_repo": "ajeetdsouza/zoxide",
            "package_name": "zoxide-git",
            "branch": "main",
        },
        {
            "name_and_repo": "junegunn/fzf",
            "package_name": "fzf-git",
            "branch": "master",
        },
        {
            "name_and_repo": "cli/cli",
            "package_name": "gh-git",
            "branch": "trunk",
        },
        {
            "name_and_repo": "BurntSushi/ripgrep",
            "package_name": "ripgrep-git",
            "branch": "master",
        },
    )

    for projectdata in list_of_github_projects:
        project = projectdata["name_and_repo"]
        package = projectdata["package_name"]
        branch = projectdata["branch"]

        last_commit_hash = git_project_latest_commit_hash_check(
            name_and_repo=project,
            provider="github",
        )
        manifest_commit_hash = read_project_commit_hash(package)
        if last_commit_hash != manifest_commit_hash:
            write_project_commit_hash(package, last_commit_hash)

            last_zip_hash = git_project_latest_zip_hash_check(
                name_and_repo=project,
                branch=branch,
                provider="github",
            )
            # manifest_zip_hash = read_project_zip_hash(package)
        # if last_zip_hash != manifest_zip_hash:
            write_project_zip_hash(package, last_zip_hash)

    list_of_gitlab_projects = (
        {
            "projectid":"20825969",
            "package_name": "sheepit-git",
            "branch":"master",
            "project_name": "client",
        },
        {
            "projectid":"34675721",
            "package_name": "glab-git",
            "branch":"main",
            "project_name": "cli",
        },
    )

    for projectdata in list_of_gitlab_projects:
        projectid = projectdata["projectid"]
        package = projectdata["package_name"]
        branch = projectdata["branch"]
        project_name = projectdata["project_name"]

        last_commit_hash = git_project_latest_commit_hash_check(
            name_and_repo=projectid,
            provider="gitlab",
            project_id=projectid,
        )
        manifest_commit_hash = read_project_commit_hash(package)
        if last_commit_hash != manifest_commit_hash:
            write_project_commit_hash(package, last_commit_hash)

            last_zip_hash = git_project_latest_zip_hash_check(
                name_and_repo=projectid,
                branch=branch,
                provider="gitlab",
                project_name=project_name,
            )
            # manifest_zip_hash = read_project_zip_hash(package)
        # if last_zip_hash != manifest_zip_hash:
            write_project_zip_hash(package, last_zip_hash)

if __name__ == "__main__":
    main()
