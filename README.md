### the git versions of packages uses github's workflow to autoupdate. if you encounter a hash error, you can do `--skip-hash-check` or wait for sometime. the automatic workflow runs every 4 hours. (if i do more frequent than that i have a chance of finishing up my monthly workflow run time limit)

bucket list:
1. [sheepit-autoupdater](https://www.sheepit-renderfarm.com/getstarted)
    - version: 7.24244.0
2. [sheepit-java](https://www.sheepit-renderfarm.com/getstarted)
    - version: 7.24244.0
3. [sheepit-git](https://gitlab.com/sheepitrenderfarm/client)
    - when installing this, if you see a gradle build error, saying java is not on path or something, it's a known bug with scoop, make sure your JAVA_HOME enviroment variable is set to the full path. and it should fix it.
    - version: on autoupdate. check the [manifest](https://github.com/ingenarel/ingenarel-scoop-bucket/blob/master/bucket/sheepit-git.json) to get the current commit hash version.
4. [discordo-git](https://github.com/ayn2op/discordo)
    - version: on autoupdate. check the [manifest](https://github.com/ingenarel/ingenarel-scoop-bucket/blob/master/bucket/discordo-git.json) to get the current commit hash version.
