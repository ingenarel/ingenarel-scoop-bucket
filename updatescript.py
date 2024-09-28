import requests, hashlib, json

def git_project_latest_commit_hash_check(
    provider:str,
    name_and_repo=None,
    project_id=None
    ) -> str:
    # print(provider)
    # print(name_and_repo)
    # print(project_id)
    # print()
    """
    This checks a git project and returns the latest commit hash.
    the name_and_repo is for the name and the repo.
    the provider is a git hosting provider, it currently supports github, and gitlab
    if the provider is gitlab, you need to give the project_id.
    """
    provider = provider.strip().lower()
    if provider == "github" and name_and_repo != None:
        try:
            return requests.get(f"https://api.github.com/repos/{name_and_repo}/commits").json()[0]["sha"]
        except:
            pass
    elif provider == "github" and name_and_repo == None:
        raise Exception("provider was github but name_and_repo was not provided")
    elif provider == "gitlab" and project_id != None:
        return requests.get(f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits").json()[0]["id"]
    elif provider == "gitlab" and project_id == None:
        raise Exception("provider was gitlab but a project_id was not provided")
    else:
        raise NotImplementedError(f"this function doesn't support {provider}")

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
        git_project_latest_zip_url = f"https://github.com/{name_and_repo}/archive/refs/heads/{branch}.zip"
    elif provider == "gitlab" and project_name != None:
        git_project_latest_zip_url = f"https://gitlab.com/{name_and_repo}/-/archive/{branch}/heads/{project_name}-{branch}.zip"
    elif provider == "gitlab" and project_name == None:
        raise Exception("provider was gitlab but a project_name was not provided")
    else:
        raise NotImplementedError(f"this function doesn't support {provider}")
    
    # chatgpt written code starts here
    hash_obj = hashlib.new('sha256')
    with requests.get(git_project_latest_zip_url, stream=True) as response:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
    return hash_obj.hexdigest()
    # chatgpt written code ends here

def read_project_commit_and_zip_hash(package_name:str) -> tuple:
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return (data["version"], data["hash"])

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

def git_project_check_and_fix(list_of_git_projects:dict) -> None:
    for provider_name in list_of_git_projects:
        # print(provider_name)
        for projectdata in list_of_git_projects[provider_name]:
            # print(projectdata)
            if provider_name == "github":
                git_project = projectdata["name_and_repo"]
                projectname = None
            elif provider_name == "gitlab":
                git_project = projectdata["projectid"]
                projectname = projectdata["project_name"]
            else:
                raise NotImplementedError(f"given a git provider \"{provider_name}\" that isn't supported")
            # print(git_project)
            package = projectdata["package_name"]
            branch = projectdata["branch"]

            last_commit_hash = git_project_latest_commit_hash_check(
                provider=provider_name,
                name_and_repo=git_project,
                project_id=git_project,
            )
            # print(f"{provider_name} | {git_project} commit hash: {last_commit_hash}")
            manifest_commit_hash, manifest_zip_hash = read_project_commit_and_zip_hash(package)
            if last_commit_hash != manifest_commit_hash:
                write_project_commit_hash(package, last_commit_hash)

                # print(projectname)
                last_zip_hash = git_project_latest_zip_hash_check(
                    name_and_repo=git_project,
                    branch=branch,
                    provider=provider_name,
                    project_name=projectname
                )
                if last_zip_hash != manifest_zip_hash:
                    write_project_zip_hash(package, last_zip_hash)

def main():
    list_of_git_projects = {
        "github": (
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
        ),
        "gitlab": (
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
        ),
    }
    git_project_check_and_fix(list_of_git_projects=list_of_git_projects)

if __name__ == "__main__":
    main()
