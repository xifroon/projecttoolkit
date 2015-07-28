Creating a Project
==================

Project Toolkit offer `new` command to create new project. When you starting
a project, it is likely that you know what kind of project it is and what's your
build system. Pouring those informations into Project Toolkit through
this command will likely takes you to create project at instance.

List Project Support
--------------------
We support many projects–those which templating bundles are available. The list
of supported projects can be seen by casting `project -l` or `project --list`.

Command Switch
--------------
To create new project, see the shortname of projects type on the above list,
then specify it after `--type` or `-t` options in `project new` command.

The following is the pattern and example:
```sh
$ project new -t type-supported name-of-project
$ project new -t gtk minbar
```

If you want to add additional details, use other options exposed in `--help`.

Interactive
-----------
<!-- Reference: git add -p, pgp key generator -->
