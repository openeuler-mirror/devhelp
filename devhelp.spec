Name:              devhelp
Epoch:             1
Version:           3.38.1
Release:           1
Summary:           GTK API documentation browser

License:           GPLv2+
URL:               https://wiki.gnome.org/Apps/Devhelp
Source0:           https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires:     chrpath desktop-file-utils gettext gobject-introspection-devel gtk-doc itstool meson
BuildRequires:     pkgconfig(amtk-5) pkgconfig(gsettings-desktop-schemas) pkgconfig(gtk+-3.0) pkgconfig(webkit2gtk-4.0)
BuildRequires:     libappstream-glib
Provides:          %{name}-libs = %{version}-%{release}
Obsoletes:         %{name}-libs <= %{version}-%{release}

%description
A browser to show API documentation generated by gtk-doc.

%package devel 
Summary:           Include development library when using devhelp 
Requires:          %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Development packages contains header files and library that can be used
for embedding devhelp into other applications.

%package_help

%prep
%autosetup -p1 

%build
%meson -Dgtk_doc=true -Dplugin_gedit=true
%meson_build

%install
%meson_install

install -d $RPM_BUILD_ROOT%{_datadir}/devhelp/books

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/devhelp

rm -rf ${RPM_BUILD_ROOT}%{_libdir}/gedit/plugins/__pycache__

%find_lang devhelp --with-gnome

%files -f devhelp.lang
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/devhelp
%{_datadir}/devhelp
%{_datadir}/applications/org.gnome.Devhelp.desktop
%{_datadir}/dbus-1/services/org.gnome.Devhelp.service
%{_datadir}/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Devhelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Devhelp-symbolic.svg
%{_datadir}/metainfo/org.gnome.Devhelp.appdata.xml
%dir %{_libdir}/gedit
%dir %{_libdir}/gedit/plugins
%{_libdir}/gedit/plugins/devhelp.*
%{_libdir}/libdevhelp-3.so.6*
%{_libdir}/girepository-1.0/Devhelp-3.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.libdevhelp-3.gschema.xml

%files devel
%{_includedir}/devhelp-3/
%{_libdir}/libdevhelp-3.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Devhelp-3.0.gir

%files help 
%{_datadir}/gtk-doc/*
%{_mandir}/man1/devhelp.1*

%changelog
* Wed Jun 30 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 1:3.38.1-1
- Upgrade to 1:3.38.1

* Thu Sep 17 2020 chengzihan <chengzihan2@huawei.com> - 1:3.30.1-4
- Add %{epoch} to Requires of devhelp-devel, to resolve installing problem.

* Tue Dec 31 2019 yanzhihua <yanzhihua4@huawei.com> - 1:3.30.1-3
- Modify spec

* Sun Dec 1 2019  jiaxiya <jiaxiyajiaxiya@168.com> - 1:3.30.1-2
- Package init
