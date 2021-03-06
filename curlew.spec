%global debug_package %{nil}
%global gitdate 20180528
%global commit0 10aa181c3839a3ec31faea849ed02fac0a5f9d91
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:    curlew
Version: 0.2.5
Release: 8%{?gver}%{dist}
Summary: Multimedia converter
License: Waqf 
Url:    https://github.com/chamfay/Curlew
Source0: https://github.com/chamfay/Curlew/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Group: Applications/Multimedia
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-rpm-macros
BuildRequires: librsvg2-tools
BuildRequires: gettext intltool
Requires: ffmpeg 
Requires: mediainfo 
Requires: hicolor-icon-theme
Requires: python3-gobject
Requires: python3-configparser
Requires: python3-dbus


%description
Easy to use, Free and Open-Source Multimedia converter for Linux.

%prep
%autosetup -n Curlew-%{commit0}

%build

%py3_build

%install
%py3_install

%find_lang %{name}

%post
/usr/bin/update-desktop-database &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%{_bindir}/curlew
%{python3_sitelib}/curlew*
%{_datadir}/applications/curlew.desktop
%{_datadir}/doc/curlew
%{_datadir}/icons/hicolor/scalable/apps/curlew.svg
%{_datadir}/icons/hicolor/*/apps/curlew.png
%{_datadir}/curlew/modules/
%{_datadir}/curlew/formats.cfg
%{_datadir}/curlew/done.ogg
%{_datadir}/pixmaps/curlew.svg


%changelog

* Mon Oct 05 2020 David Va <davidva AT tuta DOT io> 0.2.5-8.git10aa181
- Rebuilt

* Wed Jun 10 2020 David Va <davidva AT tuta DOT io> 0.2.5-6.git10aa181
- Rebuilt for python3.9

* Thu Jan 09 2020 David Va <davidva AT tuta DOT io> 0.2.5-5.git10aa181
- Rebuilt
- Renamed dependencias for deprecation of python2

* Sun Dec 29 2019 David Va <davidva AT tuta DOT io> 0.2.5-4.git10aa181
- Rebuilt

* Fri Aug 03 2018 David Va <davidva AT tuta DOT io> 0.2.5-3.git10aa181
- Rebuilt 

* Wed Jul 04 2018 David Va <davidva AT tuta DOT io> 0.2.5-2.git10aa181
- Rebuilt for Python3.7

* Mon May 28 2018 David Vásquez <davidjeremias82 AT gmail DOT com> 0.2.5-1.git10aa181
- Updated to 0.2.5-1.git10aa181

* Tue Jun 13 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 0.2.4-1.git042109b
- Initial build
