import requests, hashlib, json

def github_project_latest_commit_hash_check(name_and_repo:str) -> str:
    github_project_latest_commit_url = f"https://api.github.com/repos/{name_and_repo}/commits"
    return requests.get(github_project_latest_commit_url).json()[0]["sha"]

def github_project_latest_zip_hash_check(name_and_repo:str, commit_hash:str) -> str:
    github_project_latest_zip_hash_url = f"https://github.com/{name_and_repo}/archive/{commit_hash}.zip"
    hash_obj = hashlib.new('sha256')
    with requests.get(github_project_latest_zip_hash_url, stream=True) as response:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                hash_obj.update(chunk)
    return hash_obj.hexdigest()

def read_github_project_commit_hash(package_name:str) -> str:
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return data["version"]

def read_github_project_zip_hash(package_name:str) -> str:
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    return data["hash"]

def write_github_project_commit_hash(package_name:str, github_commit_hash:str):
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    data["version"] = github_commit_hash
    with open(f"bucket/{package_name}.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
    print(f"{package_name} commit hash changed to {github_commit_hash}")

def write_github_project_zip_hash(package_name:str, github_zip_hash:str):
    with open(f'bucket/{package_name}.json', 'r') as manifest:
        data = json.load(manifest)
    data["hash"] = github_zip_hash
    with open(f"bucket/{package_name}.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
    print(f"{package_name} zip hash changed to {github_zip_hash}")

def main():
    list_of_github_projects = (
        ("ayn2op/discordo", "discordo-git"),
    )

    for projectdata in list_of_github_projects:
        project = projectdata[0]
        package = projectdata[1]
        last_commit_hash = github_project_latest_commit_hash_check(project)
        last_zip_hash = github_project_latest_zip_hash_check(project, last_commit_hash)
        manifest_commit_hash = read_github_project_commit_hash(package)
        manifest_zip_hash = read_github_project_zip_hash(package)

        if last_commit_hash != manifest_commit_hash:
            write_github_project_commit_hash(package, last_commit_hash)

        if last_zip_hash != manifest_zip_hash:
            write_github_project_zip_hash(package, last_zip_hash)

if __name__ == "__main__":
    main()
