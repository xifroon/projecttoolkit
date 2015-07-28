Xifroon Project Toolkit
=======================

Xifroon Project Toolkit is utility software used to manage software better:
enabling faster project creation, linting project structure, and adding
template files at a blink.

It is used internally in Xifroon Lab. but open sourced to make wider audience
and receive various feedback. This software goal is matching with Xifroon
Lab's standard guidelines: maintain uniformity and apply objective approach
for __better maintainability__.

Xifroon Lab standard guideline itself is not yet stable, needs more feedback.
The standard is a [separate project](https://github.com/xifroon/standard-guidelines) on Xifroon Lab at GitHub.

Features
--------
Below features already implemented,
+ Create supported project directory structure
+ Specification based on JSON and stock (template) file
+ Variable-enabled template file
+ Inheritable templating specification

For planned features, please refer to [TODO file](TODO.md).

Install
-------
To install, simply use usual tricast installer:
```sh
$ ./configure
$ make
$ sudo make install
```
or build them as package then install with your package manager.
As it is utilizing autotools build system, packaging guide should be widely
available.

### Alternate Prefix
The default prefix seems to point to `/usr/local/`, if you want to change this
simply use `--prefix` on `./configure`:
```sh
$ ./configure --prefix=/path/to/prefix
```
Look for more options on `./configure --help` or autotools docs.

Usage
-----
Once installed, make sure the `project` and `project-[command]` files are on
directory which listed on `$PATH` environment variable.

Then, you can start using it happily:
```sh
# Look for help
$ project --help
# Cast project command help
$ project new --help
# ..etc.
```
Those commands provided as starting point.

### List Supported Project
Another lookup is listing project supported. It is available as command also:
```sh
$ project --list
X0 Project Toolkit v1.0

Supported project type:
  common     X0 Standard Template Project
  autotools  GNU Autotools project
  gtk+       GTK C/C++ project
  ...
```

### Create New Project
To create new project, see the shortname of projects type on the above list,
then specify it after `--type` or `-t` options in `project new` command.

The following is the pattern and example:
```sh
# Pattern
$ project new -t type-supported name-of-project
# Example
$ project new -t gtk minbar
```

More on this topic see wiki [Creating Project](doc/wiki/creating_project.md).

Contributing
------------
See [Contributing to X0 Projext] for general guide.

### Modify Template
If you notice on `data/template` dir, this project utilize templating system.
For you who interested, please refer to [Template System](doc/wiki/template_system.md) documentation.

Contact
-------
+ [Hernawan Fa'iz Abdillah](mailto:hernawan.faiz.a@mail.ugm.ac.id) – author

License
-------
Apache Common License v2.0

[Contributing to X0 Projext]: (https://github.com/Xifroon/standard-guidelines/guideline/contributing.md)
