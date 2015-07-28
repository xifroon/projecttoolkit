#
## Initialize
#
AC_INIT([${project_longname}], [0.1.0],[mailto:${project_mail}],[${project_name}])
AM_INIT_AUTOMAKE([-Wall])
AC_CONFIG_SRCDIR([src])
AC_PROG_CC

AC_CONFIG_HEADERS([config.h])

#
## Gnome Section
#
GNOME_COMMON_INIT
GNOME_DEBUG_CHECK
GNOME_COMPILE_WARNINGS([maximum])
GNOME_MAINTAINER_MODE_DEFINES

#
## Requirement
#
pkg_modules="gtk+-3.0 >= 3.40 glib-2.0"
PKG_CHECK_MODULES(MODULE, [$pkg_modules])

#
## Identify makefiles
#
AC_CONFIG_FILES([
	Makefile
	data/Makefile
	src/Makefile
	doc/Makefile
	pixmaps/icons/Makefile
	pixmaps/icons/16x16/Makefile
	pixmaps/icons/24x24/Makefile
	pixmaps/icons/32x32/Makefile
	pixmaps/icons/48x48/Makefile
	pixmaps/icons/64x64/Makefile
	pixmaps/icons/128x128/Makefile
])

#
## Output
#
AC_OUTPUT
