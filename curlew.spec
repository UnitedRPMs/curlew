%global debug_package %{nil}
%global gitdate 20170613
%global commit0 042109ba05e3c82dd801b3ac24b87607259212c7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:    curlew
Version: 0.2.4
Release: 1%{?gver}%{dist}
Summary: Multimedia converter
License: Waqf 
Url:    https://github.com/chamfay/Curlew
Source0: https://github.com/chamfay/Curlew/archive/%{commit0}.tar.gz#/%{name}-%{version}.tar.gz
Group: Applications/Multimedia
BuildArch: noarch
BuildRequires: python3-devel 
BuildRequires: python3-setuptools 
BuildRequires: librsvg2-tools
BuildRequires: gettext intltool
Requires: ffmpeg 
Requires: mediainfo 
Requires: hicolor-icon-theme
Requires: pygobject3
Requires: python-configparser


%description
Easy to use, Free and Open-Source Multimedia converter for Linux.

%prep
%autosetup -n Curlew-%{commit0}

%build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot} 

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

* Tue Jun 13 2017 David Vásquez <davidjeremias82 AT gmail DOT com> 0.2.4-1.git042109b
- Initial build
