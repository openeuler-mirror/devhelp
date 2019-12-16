Name:              devhelp
Epoch:             1
Version:           3.30.1
Release:           2 
Summary:           GTK API documentation browser

License:           GPLv2+
URL:               https://wiki.gnome.org/Apps/Devhelp
Source0:           https://download.gnome.org/sources/%{name}/3.30/%{name}-%{version}.tar.xz

BuildRequires:     chrpath desktop-file-utils gettext gobject-introspection-devel gtk-doc itstool meson
BuildRequires:     pkgconfig(amtk-5) pkgconfig(gsettings-desktop-schemas) pkgconfig(gtk+-3.0) pkgconfig(webkit2gtk-4.0)
BuildRequires:     libappstream-glib
Provides:          %{name}-libs = %{version}-%{release}
Obsoletes:         %{name}-libs <= %{version}-%{release}

%description
A browser to show API documentation generated by gtk-doc.

%package devel 
Summary:           Include development library when using devhelp 
Requires:          %{name}%{?_isa} = %{version}-%{release}
%description devel
Development packages contains header files and library that can be used
for embedding devhelp into other applications.

%package_help

%prep
%autosetup -p1 

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install

install -d $RPM_BUILD_ROOT%{_datadir}/devhelp/books

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/devhelp

rm -rf ${RPM_BUILD_ROOT}%{_libdir}/gedit/plugins/__pycache__

%find_lang devhelp --with-gnome

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/devhelp
%{_datadir}/devhelp
%{_datadir}/applications/org.gnome.Devhelp.desktop
%{_datadir}/dbus-1/services/org.gnome.Devhelp.service
%{_datadir}/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Devhelp.png
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Devhelp-symbolic.svg
%{_datadir}/metainfo/org.gnome.Devhelp.appdata.xml
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins

%files devel
%{_includedir}/devhelp-3/
%{_libdir}/libdevhelp-3.so.6*
%{_libdir}/girepository-1.0/Devhelp-3.0.typelib
%{_libdir}/libdevhelp-3.so
%{_libdir}/pkgconfig/*
%{_datadir}/glib-2.0/schemas/org.gnome.libdevhelp-3.gschema.xml
%{_datadir}/gir-1.0/Devhelp-3.0.gir

%files help 
%{_datadir}/gtk-doc/*
%{_mandir}/man1/devhelp.1*


%changelog
* Sun Dec 1 2019  jiaxiya <jiaxiyajiaxiya@168.com> - 1:3.30.1-2
- Package init
