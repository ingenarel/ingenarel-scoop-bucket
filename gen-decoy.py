import json, random

list_of_git_projects = (
        "webcord",
        "discordo",
        "lazygit",
        "zoxide",
        "fzf",
        "gh",
        "ripgrep",
        "vesktop",
        "sheepit",
        "glab",
        )

for project in list_of_git_projects:
    with open(f"decoy/{project}-decoy", "w") as decoy:
        decoy.write(f"This is a decoy file\nIt should not be touched\nRandom bytes to register a scoop update:\n{random.randbytes(100)}\n")

    with open(f"bucket/{project}-git.json", "r") as manifest:
        data = json.load(manifest)
    data["url"] = f"https://raw.githubusercontent.com/ingenarel/ingenarel-scoop-bucket/refs/heads/master/decoy/{project}-decoy"
    with open(f"bucket/{project}-git.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))

    with open(f"bucket/{project}-git-ssh.json", "r") as manifest:
        data = json.load(manifest)
    data["url"] = f"https://raw.githubusercontent.com/ingenarel/ingenarel-scoop-bucket/refs/heads/master/decoy/{project}-decoy"
    with open(f"bucket/{project}-git-ssh.json", "w") as manifest:
        manifest.write(json.dumps(data, indent=4))
