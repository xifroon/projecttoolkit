#
## Autoconf init
#
AC_INIT([X0 Project Toolkit], [0.1.0], [mailto:hernawan.faiz.a@ugm.ac.id], [projecttoolkit])
AC_CONFIG_SRCDIR([src])
AC_PROG_CC
AC_CONFIG_MACRO_DIRS([aclocal.cache])

#
## Automake init
#
AM_INIT_AUTOMAKE([-Wall foreign])
AM_PATH_PYTHON([2.7],, [:])

#
## Requirement
#
# pkg_modules=""
# PKG_CHECK_MODULES(MODULE, [$pkg_modules])

#
## Makefiles
#
AC_CONFIG_FILES([
	Makefile
	src/Makefile
	data/Makefile
	python/Makefile
	python/projecttoolkit/Makefile
	python/projecttoolkit/template/Makefile
])

#
## Output
#
AC_OUTPUT
