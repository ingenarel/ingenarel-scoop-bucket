### the git versions of packages uses github's workflow to autoupdate. if you encounter a hash error, you can do `--skip-hash-check` or wait for sometime. the automatic workflow runs every hour.
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ingenarel/ingenarel-scoop-bucket/main.yml?style=for-the-badge&logo=githubactions&logoColor=ff0000&label=update%20checks&labelColor=000000)



bucket list:
1. [sheepit-autoupdater](https://www.sheepit-renderfarm.com/getstarted)    ![Scoop Version](https://img.shields.io/scoop/v/sheepit-autoupdater?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

3. [sheepit-jar](https://www.sheepit-renderfarm.com/getstarted)    ![Scoop Version](https://img.shields.io/scoop/v/sheepit-jar?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

4. [sheepit-git](https://gitlab.com/sheepitrenderfarm/client)    ![Scoop Version](https://img.shields.io/scoop/v/sheepit-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)
    - when installing this, if you see a gradle build error, saying java is not on path or something, it's a known bug with scoop, make sure your JAVA_HOME enviroment variable is set to the full path. and it should fix it.

5. [discordo-git](https://github.com/ayn2op/discordo)    ![Scoop Version](https://img.shields.io/scoop/v/discordo-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

6. [lazygit-git](https://github.com/jesseduffield/lazygit)    ![Scoop Version](https://img.shields.io/scoop/v/lazygit-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)

7. [zoxide-git](https://github.com/ajeetdsouza/zoxide)    ![Scoop Version](https://img.shields.io/scoop/v/zoxide-git?bucket=https%3A%2F%2Fgithub.com%2Fingenarel%2Fingenarel-scoop-bucket&label=version)
    - when installing this, you need to make sure that you have the windows sdk, and msvc build tools, you can install them by going to [this link](https://visualstudio.microsoft.com/visual-cpp-build-tools/), then either install full c++ dev guide, or you can also do a minimal install (still like 2-3 gigs or something), by selecting "individual components", then selecting windows sdk, and msvc build tools(the latest version should be the best)
