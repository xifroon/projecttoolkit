bin_SCRIPTS = project project-new
CLEANFILES = project project-new
EXTRA_DIST = project.py.in project-new.py.in

do_subst = sed -e 's,[@]prefix[@],$(prefix),g' \
	-e 's,[@]datadir[@],$(datadir),g' \
	-e 's,[@]datarootdir[@],$(datarootdir),g' \
	-e 's,[@]PACKAGE_NAME[@],$(PACKAGE_NAME),g' \
	-e 's,[@]PACKAGE[@],$(PACKAGE),g' \
	-e 's,[@]VERSION[@],$(VERSION),g'

project: project.py.in Makefile
	$(do_subst) < $(srcdir)/project.py.in > project

project-new: project-new.py.in Makefile
	$(do_subst) < $(srcdir)/project-new.py.in > project-new

MAINTAINERCLEANFILES = \
	Makefile.in
