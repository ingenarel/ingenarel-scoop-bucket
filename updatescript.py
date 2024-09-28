import requests, hashlib, json

def github_project_latest_commit_hash_check(name_and_repo:str) -> str:
    github_project_latest_commit_url = f"https://api.github.com/repos/{name_and_repo}/commits"
    return requests.get(github_project_latest_commit_url).json()[0]["sha"]

def gitlab_project_latest_commit_hash_check(project_id:str) -> str:
    gitlab_project_latest_commit_url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/commits"
    return requests.get(gitlab_project_latest_commit_url).json()[0]["id"]

def github_project_latest_zip_hash_check(name_and_repo:str, branch:str) -> str:
    github_project_latest_zip_hash_url = f"https://github.com/{name_and_repo}/archive/refs/heads/{branch}.zip"
    hash_obj = hashlib.new('sha256')
    with requests.get(github_project_latest_zip_hash_url, stream=True) as response:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
    return hash_obj.hexdigest()

def gitlab_project_latest_zip_hash_check(name_and_repo:str, branch:str, project_name:str) -> str:
    github_project_latest_zip_hash_url = f"https://gitlab.com/{name_and_repo}/-/archive/{branch}/heads/{project_name}-{branch}.zip"
    hash_obj = hashlib.new('sha256')
    with requests.get(github_project_latest_zip_hash_url, stream=True) as response:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
    return hash_obj.hexdigest()

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
            "branch": "main"
        },
        {
            "name_and_repo": "jesseduffield/lazygit",
            "package_name": "lazygit-git",
            "branch": "master"
        },
        {
            "name_and_repo": "ajeetdsouza/zoxide",
            "package_name": "zoxide-git",
            "branch": "main"
        },
        {
            "name_and_repo": "junegunn/fzf",
            "package_name": "fzf-git",
            "branch": "master"
        },
        {
            "name_and_repo": "cli/cli",
            "package_name": "gh-git",
            "branch": "trunk"
        },
    )

    for projectdata in list_of_github_projects:
        project = projectdata["name_and_repo"]
        package = projectdata["package_name"]
        branch = projectdata["branch"]

        last_commit_hash = github_project_latest_commit_hash_check(project)
        manifest_commit_hash = read_project_commit_hash(package)
        if last_commit_hash != manifest_commit_hash:
            write_project_commit_hash(package, last_commit_hash)

            last_zip_hash = github_project_latest_zip_hash_check(project, branch)
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

        last_commit_hash = gitlab_project_latest_commit_hash_check(projectid)
        manifest_commit_hash = read_project_commit_hash(package)
        if last_commit_hash != manifest_commit_hash:
            write_project_commit_hash(package, last_commit_hash)

            last_zip_hash = gitlab_project_latest_zip_hash_check(projectid, branch, project_name)
            # manifest_zip_hash = read_project_zip_hash(package)
        # if last_zip_hash != manifest_zip_hash:
            write_project_zip_hash(package, last_zip_hash)

if __name__ == "__main__":
    main()
