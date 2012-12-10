Summary:	Send files from caja using with mail or IM
Name:		mate-file-manager-sendto
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gupnp-1.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mateconf-2.0)

Requires:	mate-file-manager
Provides:	caja-sendto = %{version}-%{release}
#suggest the most important plugins
Suggests:	%{name}-bluetooth
Provides:	caja-sendto-pidgin = %{version}-%{release}
# the old eds is needed to build for eds support
#Suggests:	%{name}-evolution

%description
This application provides integration between caja and mail or IM clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary:	Send files from caja to pidgin
Group:		Graphical desktop/GNOME
Requires:	pidgin
Requires:	%{name} = %{version}-%{release}
Provides:	caja-sendto-pidgin = %{version}-%{release}

%description pidgin
This application provides integration between caja and pidgin.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package upnp
Summary:	Send files from caja via UPNP
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}
Provides:	caja-sendto-upnp = %{version}-%{release}

%description upnp
This application provides integration between caja and UPNP.
It adds a Nautilus context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package evolution
Summary:	Send files from caja to evolution
Group:		Graphical desktop/GNOME
Requires:	evolution
Requires:	%{name} = %{version}-%{release}
Provides:	caja-sendto-evolution = %{version}-%{release}

%description evolution
This application provides integration between caja and evolution.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package devel
Summary:	Development files for caja-sendto
Group:		Graphical desktop/GNOME

%description devel
This package provides development files needed to build plugins upon
caja-sendto.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
%find_lang caja-sendto

find %buildroot -name *.la | xargs rm 

%files -f caja-sendto.lang
%doc NEWS AUTHORS ChangeLog
%{_bindir}/caja-sendto
%dir %{_libdir}/caja-sendto/
%dir %{_libdir}/caja-sendto/plugins
# this might need to be removed
%{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%{_libdir}/caja-sendto/plugins/libnstburn.so
%{_libdir}/caja-sendto/plugins/libnstemailclient.so
%{_libdir}/caja-sendto/plugins/libnstgajim.so
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_datadir}/caja-sendto/
%{_datadir}/MateConf/gsettings/caja-sendto-convert
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_mandir}/man1/caja-sendto.1*

%files pidgin
%{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files upnp
%{_libdir}/caja-sendto/plugins/libnstupnp.so

#%files evolution	 
#%{_libdir}/caja-sendto/plugins/libnstevolution.so

%files devel
%doc %{_datadir}/gtk-doc/html/caja-sendto/
%{_includedir}/caja-sendto/
%{_libdir}/pkgconfig/caja-sendto.pc



%changelog
* Mon Jun 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802250
- imported package mate-file-manager-sendto

