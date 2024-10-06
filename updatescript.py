import requests, json, os

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
        return requests.get(f"https://api.github.com/repos/{name_and_repo}/commits").json()[0]["sha"]
    elif provider == "github" and name_and_repo == None:
        raise Exception("provider was github but name_and_repo was not provided")
    elif provider == "gitlab" and project_id != None:
        return requests.get(f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits").json()[0]["id"]
    elif provider == "gitlab" and project_id == None:
        raise Exception("provider was gitlab but a project_id was not provided")
    else:
        raise NotImplementedError(f"this function doesn't support {provider}")

def read_project_commit_hash(package_name:str) -> str:
    """
    this reads the manifest and return the commit hash.
    package_name should be the manifest name. it should not contain the the .json extension or bucket/
    It returns the commit hash.
    """
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return data["version"]

def write_project_commit_hash(package_name:str, commit_hash:str):
    with open(f'bucket/{package_name}-git.json', 'r') as manifest:
        data = json.load(manifest)
    data["version"] = commit_hash
    with open(f"bucket/{package_name}-git.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
    print(f"{package_name} commit hash changed to {commit_hash}")

    with open(f'bucket/{package_name}-git-ssh.json', 'r') as manifest:
        data = json.load(manifest)
    data["version"] = commit_hash
    with open(f"bucket/{package_name}-git-ssh.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))

    print(f"{package_name}-ssh commit hash changed to {commit_hash}")
    os.system(f"git add bucket/{package_name}-git.json bucket/{package_name}-git-ssh.json'")
    os.system(f"git commit -m '{package_name} updated to {commit_hash}'")


def git_project_check_and_fix(list_of_git_projects:dict) -> None:
    for provider_name in list_of_git_projects:
        # print(provider_name)
        for projectdata in list_of_git_projects[provider_name]:
            # print(projectdata)
            if provider_name == "github":
                git_project = projectdata["name_and_repo"]
            elif provider_name == "gitlab":
                git_project = projectdata["projectid"]
            else:
                raise NotImplementedError(f"given a git provider \"{provider_name}\" that isn't supported")
            # print(git_project)
            package = projectdata["package_name"]

            last_commit_hash = git_project_latest_commit_hash_check(
                provider=provider_name,
                name_and_repo=git_project,
                project_id=git_project,
            )
            # print(f"{provider_name} | {git_project} commit hash: {last_commit_hash}")
            manifest_commit_hash = read_project_commit_hash(package)
            if last_commit_hash != manifest_commit_hash:
                write_project_commit_hash(package, last_commit_hash)
                # print(projectname)

def main():
    list_of_git_projects = {
        "github": (
            {
                "name_and_repo": "SpacingBat3/WebCord",
                "package_name": "webcord",
            },
            {
                "name_and_repo": "ayn2op/discordo",
                "package_name": "discordo",
            },
            {
                "name_and_repo": "jesseduffield/lazygit",
                "package_name": "lazygit",
            },
            {
                "name_and_repo": "ajeetdsouza/zoxide",
                "package_name": "zoxide",
            },
            {
                "name_and_repo": "junegunn/fzf",
                "package_name": "fzf",
            },
            {
                "name_and_repo": "cli/cli",
                "package_name": "gh",
            },
            {
                "name_and_repo": "BurntSushi/ripgrep",
                "package_name": "ripgrep",
            },
            {
                "name_and_repo": "Vencord/Vesktop",
                "package_name": "vesktop",
            },
        ),
        "gitlab": (
            {
                "projectid":"20825969",
                "package_name": "sheepit",
            },
            {
                "projectid":"34675721",
                "package_name": "glab",
            },
        ),
    }
    git_project_check_and_fix(list_of_git_projects=list_of_git_projects)

if __name__ == "__main__":
    main()
