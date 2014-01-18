# NOTE: it's deprecated package, a binding for MATE <= 1.4 APIs;
# when built with MATE 1.6 panel library, some applet APIs are no longer available
#
# Conditional build:
%bcond_with	mate14	# build with pure MATE Desktop <= 1.4 libraries
#
Summary:	Python bindings for MATE Desktop libraries
Summary(pl.UTF-8):	Wiązania Pythona do bibliotek środowiska MATE Desktop
Name:		python-mate-desktop
Version:	1.4.0
Release:	1
License:	LGPL v2.1+/GPL v2+ depending on module (see COPYING)
Group:		Libraries/Python
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	c6c2c168ecf532c31c38d4714cb09c7f
Patch0:		%{name}-panel.patch
Patch1:		%{name}-atril.patch
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libmate-devel >= 1.1.0
BuildRequires:	libmatekeyring-devel >= 1.1.0
BuildRequires:	libmateui-devel >= 1.1.0
BuildRequires:	libmatewnck-devel >= 1.3.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-conf-devel >= 1.1.0
BuildRequires:	mate-desktop-devel >= 1.1.0
%{?with_mate14:BuildRequires:	mate-document-viewer-devel >= 1.1.0}
%{?with_mate14:BuildRequires:	mate-document-viewer-devel < 1.5.0}
%{!?with_mate14:BuildRequires:	mate-document-viewer-devel >= 1.5.0}
%{?with_mate14:BuildRequires:	mate-panel-devel >= 1.1.0}
%{?with_mate14:BuildRequires:	mate-panel-devel < 1.5.0}
%{!?with_mate14:BuildRequires:	mate-panel-devel >= 1.5.0}
BuildRequires:	mate-window-manager-devel >= 1.1.0
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-mate-devel >= 1.1.0
BuildRequires:	python-pygobject-devel >= 2.10.0
BuildRequires:	python-pygtk-devel >= 2:2.10.3
BuildRequires:	libmatecomponent-devel >= 1.1.0
BuildRequires:	libmatecomponentui-devel >= 1.1.0
BuildRequires:	libmatecanvas-devel >= 1.1.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-conf-devel >= 1.1.0
BuildRequires:	mate-vfs-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-matecorba-devel >= 1.1.0
BuildRequires:	python-pygobject-devel >= 2.17.0
BuildRequires:	python-pygtk-devel >= 2:2.10.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libmate-libs >= 1.1.0
Requires:	mate-desktop-libs >= 1.1.0
Requires:	python-pygobject >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define pydefsdir %(pkg-config --variable=defsdir pygtk-2.0)

%description
Python bindings for MATE Desktop libraries.

%description -l pl.UTF-8
Wiązania Pythona do bibliotek środowiska MATE Desktop.

%package -n python-atril
Summary:	Python binding to Atril (MATE Document Viewer) library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki Atril (przeglądarki dokumentów MATE)
Group:		Libraries/Python
Requires:	mate-document-viewer-libs >= 1.5.0
# atexit
Requires:	python-modules
Requires:	python-pygobject >= 2.10.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description -n python-atril
Python binding to Atril (MATE Document Viewer) library.

%description -n python-atril -l pl.UTF-8
Wiązanie Pythona do biblioteki Atril (przeglądarki dokumentów MATE).

%package -n python-marco
Summary:	Python binding to Marco (MATE Window Manager) library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki Marco (zarządcy okien MATE)
Group:		Libraries/Python
Requires:	mate-window-manager-libs >= 1.1.0
Requires:	python-pygobject >= 2.10.0
Requires:	python-pygtk-gtk >= 2:2.10.3
Requires:	python-pygtk-pango >= 2:2.10.3

%description -n python-marco
Python binding to Marco (MATE Window Manager) library.

%description -n python-marco -l pl.UTF-8
Wiązanie Pythona do biblioteki Marco (zarządcy okien MATE).

%package -n python-mate-applet
Summary:	Python binding to MATE Panel Applet library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki apletów panelu MATE
Group:		Libraries/Python
Requires:	libmate-libs >= 1.1.0
Requires:	libmateui >= 1.1.0
Requires:	mate-panel-libs >= 1.1.0
Requires:	python-mate >= 1.1.0
Requires:	python-mate-component-ui >= 1.1.0
Requires:	python-pygobject >= 2.10.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description -n python-mate-applet
Python binding to MATE Panel Applet library.

%description -n python-mate-applet -l pl.UTF-8
Wiązanie Pythona do biblioteki apletów panelu MATE.

%package -n python-mate-keyring
Summary:	Python binding to MATE Keyring library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki MATE Keyring
Group:		Libraries/Python
Requires:	libmatekeyring >= 1.1.0
Requires:	python-pygobject >= 2.10.0

%description -n python-mate-keyring
Python binding to MATE Keyring library.

%description -n python-mate-keyring -l pl.UTF-8
Wiązanie Pythona do biblioteki MATE Keyring.

%package -n python-mate-wnck
Summary:	Python binding to MateWnck library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki MateWnck
Group:		Libraries/Python
Requires:	libmatewnck >= 1.3.0
Requires:	python-pygobject >= 2.10.0
Requires:	python-pygtk-gtk >= 2:2.10.3

%description -n python-mate-wnck
Python binding to MateWnck library.

%description -n python-mate-wnck -l pl.UTF-8
Wiązanie Pythona do biblioteki MateWnck.

%package common
Summary:	Common files for Python MATE Desktop bindings
Summary(pl.UTF-8):	Pliki wspólne wiązań Pythona do biblioteka MATE Desktop
Group:		Libraries/Python
Requires:	python-mate-common >= 1.4

%description common
Common files for Python MATE Desktop bindings.

%description common -l pl.UTF-8
Pliki wspólne wiązań Pythona do bibliotek MATE Desktop.

%package devel
Summary:	Development files for Python MATE Desktop bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do bibliotek MATE Desktop
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-atril = %{version}-%{release}
Requires:	python-marco = %{version}-%{release}
Requires:	python-mate-applet = %{version}-%{release}
Requires:	python-mate-keyring = %{version}-%{release}
Requires:	python-mate-wnck = %{version}-%{release}
Requires:	python-pygobject-devel >= 2.10.0
Requires:	python-pygtk-devel >= 2:2.10.3

%description devel
Development files for Python MATE Desktop bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do bibliotek MATE Desktop.

%package apidocs
Summary:	API documentation for Python MATE Desktop bindings
Summary(pl.UTF-8):	Dokumentacja API wiązań Pythona do bibliotek MATE Desktop
Group:		Documentation

%description apidocs
API documentation for Python MATE Desktop bindings.

%description apidocs -l pl.UTF-8
Dokumentacja API wiązań Pythona do bibliotek MATE Desktop.

%prep
%setup -q
%{!?with_mate14:%patch0 -p1}
%{!?with_mate14:%patch1 -p1}

%build
# NOTE: although configure.ac contains autotools build system deprecation note,
# it's maintained in MATE unlike waf (and there won't be any "future version")
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# fake broken condition (affects only printed summary)
export have_pymatecorba=true
# disable: bugbuddy, gtksourceview, gtop, mediaprofiles, rsvg, totem_plparser (these belong to python-gnome-desktop)
# disable: mateprint, mateprintui (obsolete libraries, not released for MATE >= 1.1)
%configure \
	--disable-bugbuddy \
	--enable-gtk-doc \
	--disable-gtksourceview \
	--disable-gtop \
	--enable-marco \
	--disable-mateprint \
	--disable-mateprintui \
	--disable-mediaprofiles \
	--disable-rsvg \
	--disable-totem_plparser \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0{,/matedesktop}/*.la
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/gtk-2.0/matedesktop
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matedesktop/_matedesktop.so
%{py_sitedir}/gtk-2.0/matedesktop/__init__.py[co]

%files -n python-atril
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/atril.so

%files -n python-marco
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/marco.so

%files -n python-mate-applet
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/mateapplet.so
%{py_sitedir}/gtk-2.0/mate/applet.py[co]

%files -n python-mate-keyring
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matekeyring.so

%files -n python-mate-wnck
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gtk-2.0/matewnck.so

%files common
%defattr(644,root,root,755)
# note: COPYING specifies which license applies to particular modules
%doc AUTHORS COPYING ChangeLog NEWS README

%files devel
%defattr(644,root,root,755)
%{pydefsdir}/_matedesktop.defs
%{pydefsdir}/applet.defs
%{pydefsdir}/atril.defs
%{pydefsdir}/marco.defs
%{pydefsdir}/matekeyring.defs
%{pydefsdir}/matewnck.defs
%{_pkgconfigdir}/mate-python-desktop-2.0.pc

#%files apidocs - only for mateprint and mateprintui, so not packaged
