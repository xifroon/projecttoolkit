TEMPLATE_ARCHIVE = template.tar.xz
dist_pkgdata_DATA = $(TEMPLATE_ARCHIVE)

template.tar.xz:
	tar --format=gnu --xz -cf $(TEMPLATE_ARCHIVE) template

install-exec-local:
	test -f $(TEMPLATE_ARCHIVE) && rm -f $(TEMPLATE_ARCHIVE)

install-data-hook:
	cd $(DESTDIR)$(pkgdatadir); \
	tar -xvf $(TEMPLATE_ARCHIVE)

uninstall-local:
	rm --force -Rd $(TEMPLATE_ARCHIVE)
	cd $(DESTDIR)$(pkgdatadir); \
	rm --force -Rd template $(TEMPLATE_ARCHIVE)

CLEANFILES = $(TEMPLATE_ARCHIVE)

MAINTAINERCLEANFILES = \
	Makefile.in
