SUBDIRS = src pixmaps data po doc

desktopdir = $(datadir)/applications
desktop_in_files = minbar.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

EXTRA_DIST = \
	intltool-extract.in	\
	intltool-merge.in	\
	intltool-update.in	\
	README.md			\
	CHANGELOG.md		\
	TODO.md				\
	$(desktop_in_files)

DISTCLEANFILES = \
	intltool-extract	\
	intltool-merge		\
	intltool-update

@INTLTOOL_DESKTOP_RULE@
