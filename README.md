## This repo is inspired by aur -git packages. what are these git packages? they download a github repo and compiles the program from the source code. These packages are not release builds, not even nightly builds, they are the most up to date with the latest source code.


the normal git packages are using https to clone. and the -git-ssh packages are gonna use ssh to clone. i personally prefer ssh cloning that's why i made these versions an option. altho if you want to install the -git-ssh packages make sure that you have ssh setup with the repo hosting service. for example, for gh-git-ssh package, you need to have an ssh setup with github, and for glab-git-ssh, you need to have a ssh setup with gitlab.


### this bucket is for people who:

    > want the bleeding edge stuff
    > likes to compile shit from source
    > doesn't mind a bit of waiting for stuff to compile
    > doesn't mind stuff breaking once in a while.
    > has a bit of storage to spare (having all the source code and the nessesarry dependencies might take more space than downlading an .exe file)

### this bucket is NOT for people who:

    > want a stable version
    > is an impatient bitch.
    > has a panic attack by the thought of something breaking
    > is short on storage.


The git versions of packages uses github's workflow to autoupdate. I'm also using [this decoy file](https://github.com/ingenarel/ingenarel-scoop-bucket/blob/master/decoy) to get around scoop's hash check, so the hash check doesn't break every if there is a new commit in between the update checks. Whenever the file hash changes. The version check is done every hour. The commit hash version that you see might not always be up to date with the original lates commit hash, but that isn't a problem too much, it will always download the latest repo, because i don't use a download link, i do `git clone`, and if you need to update really badly in between the update checks, you can always do `scoop update packagename --force`


![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ingenarel/ingenarel-scoop-bucket/main.yml?style=for-the-badge&logo=githubactions&logoColor=ff0000&label=update%20checks&labelColor=000000)


bucket list:

- [sheepit](https://gitlab.com/sheepitrenderfarm/client)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/sheepit-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)
    - when installing this, if you see a gradle build error, saying java is not on path or something, it's a known bug with scoop, make sure your JAVA_HOME enviroment variable is set to the full path. and it should fix it.

- [discordo](https://github.com/ayn2op/discordo)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/discordo-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

- [lazygit](https://github.com/jesseduffield/lazygit)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/lazygit-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

- [zoxide](https://github.com/ajeetdsouza/zoxide)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/zoxide-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)
    - when installing this, you need to make sure that you have the windows sdk, and msvc build tools, you can install them by going to [this link](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then either install full c++ dev guide, or you can also do a minimal install (still like 2-3 gigs or something), by selecting "individual components", then selecting windows sdk, and msvc build tools(the latest version should be the best)

- [fzf](https://github.com/junegunn/fzf)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/fzf-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

- [gh](https://github.com/cli/cli)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/gh-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

- [glab](https://gitlab.com/gitlab-org/cli)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/glab-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

- [ripgrep](https://github.com/BurntSushi/ripgrep)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/ripgrep-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)
    - when installing this, you need to make sure that you have the windows sdk, and msvc build tools, you can install them by going to [this link](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then either install full c++ dev guide, or you can also do a minimal install (still like 2-3 gigs or something), by selecting "individual components", then selecting windows sdk, and msvc build tools(the latest version should be the best)

- [webcord](https://github.com/SpacingBat3/WebCord)(-git)(-git-ssh)    ![Scoop Version](https://img.shields.io/scoop/v/webcord-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

### this repo was made out of frustration. i personally used arch linux and i love it with all my life. I'm a big fan of the aur, and it's git repos, but it's been a while since i was able to use arch because of some wifi driver issues. (i'm really broke, can't buy another wifi adapter), so i've been stuck on windows for a few days. I got bored eventually, so i thought, why not package your own -git packages?

Am i trying to AUR-eify scoop? yes. Will I succed? maybe not. but it's fun anyways.
