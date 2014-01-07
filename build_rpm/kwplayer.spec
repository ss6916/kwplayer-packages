# kwplayer.spec
# Used to build rpm for kwplayer on Fedora 19/20
# Released by wangjiezhe <wangjiezhe@gmail.com>
# This spec file is published under the GPLv3 license

# Template is originally generated by "rpmdev-newspec -t python"

%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           kwplayer
Version:        3.2.6
Release:        2%{?dist}
Summary:        An elegant music player which can get songs from kuwo.cn

License:        GPLv3
URL:            https://github.com/LiuLang/kwplayer
Source:         %{name}-%{version}.tar.gz

# Followings are not needed by Fedora after 17 and will be ignored by rpmbuild
# Group:  Applications/Multimedia
# BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:  python3
Requires:  python3-dbus
Requires:  python3-gobject
Requires:  gstreamer1-plugins-base
Requires:  gstreamer1-plugins-good
Requires:  gstreamer1-plugins-ugly
Requires:  gstreamer1-libav
Requires:  gstreamer1
Requires:  gstreamer-python
Requires:  pulseaudio
Requires:  pulseaudio-module-x11
# Not installed by default in KDE
Requires:  gnome-icon-theme-symbolic
# Optional:
# Requires:  leveldb
# Requires:  python3-plyvel
# Requires:  mutagenx
# Requires:  python3-keybinder

%description
KW music player is used to get music resources from Internet.
It can also play MV, show lyrics and show photo albums of artists.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc LICENSE README.md HISTORY
%{_datadir}/icons/*
%{_datadir}/kuwo/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/*
# following sections for the compatition with Debian wheezy and Ubuntu 12.04 are removed.
%exclude %{_datadir}/icons/hicolor/scalable/mimetypes
%exclude %{_datadir}/icons/hicolor/scalable/places
%exclude %{_datadir}/icons/hicolor/scalable/status
# generated by python3
%exclude %{python3_sitelib}/kuwo/__pycache__

%post
cd /usr/lib/python3.3/site-packages/
for file in `ls|grep 'kwplayer-[0-9]*\.[0-9]*\.[0-9]*-py3\.3\.egg-info'`
do
	if [ $file != "kwplayer-%{version}-py3.3.egg-info" ]
	then
		rm $file
	fi
done
