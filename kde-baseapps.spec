%define snapshot 20161117
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define build_iconoverlay 0

Summary:	K Desktop Environment
Name:		kde-baseapps
Version:	16.12.2
%if 0%{snapshot}
Release:	1.%{snapshot}.1
# git archive --format=tar --prefix=kde-baseapps-$(date +%Y%m%d)/ HEAD | xz -vf -T0 > kde-baseapps-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{snapshot}.tar.xz
%else
Release:	1
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
%endif
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
Source1:	%{name}.rpmlintrc
Patch1:		kdebase-4.2.95-Use-Mandriva-Home-Icon.patch
Patch104:	kdebase-4.8.2-dolphin-delete-files-on-flash-drives.patch
Patch107:	kdebase-4.10.0-iconoverlay-plugin.patch
Patch108:	kdebase-4.9.5-iconoverlay-race-fix.patch
#branch patches
#trunk patches
# test patches
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
#BuildRequires:	pkgconfig(Qt5TextToSpeech)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO) >= 5.24.0
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Su)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KDED)
Suggests:	dolphin
Suggests:	kdepasswd
Suggests:	kdialog
Suggests:	kfind
Suggests:	konqueror
Suggests:	keditbookmarks
Obsoletes:	plasma-applet-folderview
Obsoletes:	%{mklibname konqsidebarplugin 5} < 16.08.3

%description
This meta package requires all base %{name} packages.

%files
%doc README

#------------------------------------------------

%package -n kdepasswd
Summary:	User password management for KDE
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Requires:	accountsservice

%description -n kdepasswd
User password management.

%files -n kdepasswd
%{_bindir}/kdepasswd
%{_datadir}/applications/org.kde.kdepasswd.desktop

#------------------------------------------------

%define konq_major 6
%define libkonq %mklibname KF5Konq %{konq_major}

%package -n %{libkonq}
Summary:	Konqueror core library
Group:		System/Libraries
Obsoletes:	%{mklibname konq 5}
Obsoletes:	%{mklibname dolphinprivate4 4}
Obsoletes:	dolphin4

%description -n %{libkonq}
Konqueror core library.

%files -n %{libkonq}
%{_libdir}/libKF5Konq.so.%{konq_major}*
%{_libdir}/libKF5Konq.so.5*

#------------------------------------------------

%define konquerorprivate_major 5
%define libkonquerorprivate %mklibname konquerorprivate %{konquerorprivate_major}

%package -n %{libkonquerorprivate}
Summary:	Konqueror core library
Group:		System/Libraries
Obsoletes:	%{mklibname konquerorprivate 4}

%description -n %{libkonquerorprivate}
Konqueror core library.

%files -n %{libkonquerorprivate}
%{_libdir}/libkonquerorprivate.so.%{konquerorprivate_major}*

#------------------------------------------------

%define kbookmarkmodel_private_major 5
%define libkbookmarkmodel_private %mklibname kbookmarkmodel_private %{kbookmarkmodel_private_major}

%package -n %{libkbookmarkmodel_private}
Summary:	Konqueror core library
Group:		System/Libraries
Obsoletes:	%{mklibname kbookmarkmodel_private 4}

%description -n %{libkbookmarkmodel_private}
Konqueror core library.

%files -n %{libkbookmarkmodel_private}
%{_libdir}/libkbookmarkmodel_private.so.%{kbookmarkmodel_private_major}*
%{_libdir}/libkbookmarkmodel_private.so.6*

#------------------------------------------------

%package -n konq-plugins
Summary:	Konqueror plugins
Group:		Graphical desktop/KDE
Requires:	konqueror
Conflicts:	dolphin < 1:4.7.0

%description -n konq-plugins
This module contains plugins that interact with Konqueror.

%files -n konq-plugins
%{_bindir}/fsview
%{_libdir}/qt5/plugins/akregatorkonqfeedicon.so
%{_libdir}/qt5/plugins/autorefresh.so
%{_libdir}/qt5/plugins/babelfishplugin.so
%{_libdir}/qt5/plugins/dirfilterplugin.so
%{_libdir}/qt5/plugins/domtreeviewerplugin.so
%{_libdir}/qt5/plugins/fsviewpart.so
%{_libdir}/qt5/plugins/khtmlsettingsplugin.so
%{_libdir}/qt5/plugins/kimgallery.so
%{_libdir}/qt5/plugins/minitoolsplugin.so
%{_libdir}/qt5/plugins/rellinksplugin.so
%{_libdir}/qt5/plugins/searchbarplugin.so
%{_libdir}/qt5/plugins/validatorsplugin.so
%{_libdir}/qt5/plugins/webarchiverplugin.so
%{_libdir}/qt5/plugins/webarchivethumbnail.so
%{_libdir}/qt5/plugins/khtmlttsplugin.so
%{_datadir}/akregator/pics/feed.png
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.rc
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.rc
%{_datadir}/domtreeviewer/domtreeviewerui.rc
%{_datadir}/fsview/fsview_part.rc
%{_datadir}/khtml/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/khtml/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/khtml/kpartplugins/autorefresh.desktop
%{_datadir}/khtml/kpartplugins/autorefresh.rc
%{_datadir}/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/khtml/kpartplugins/minitoolsplugin.desktop
%{_datadir}/khtml/kpartplugins/minitoolsplugin.rc
%{_datadir}/khtml/kpartplugins/plugin_babelfish.rc
%{_datadir}/khtml/kpartplugins/plugin_domtreeviewer.desktop
%{_datadir}/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_datadir}/khtml/kpartplugins/plugin_rellinks.desktop
%{_datadir}/khtml/kpartplugins/plugin_rellinks.rc
%{_datadir}/khtml/kpartplugins/plugin_translator.desktop
%{_datadir}/khtml/kpartplugins/plugin_validators.desktop
%{_datadir}/khtml/kpartplugins/plugin_validators.rc
%{_datadir}/khtml/kpartplugins/plugin_webarchiver.desktop
%{_datadir}/khtml/kpartplugins/plugin_webarchiver.rc
%{_datadir}/khtml/kpartplugins/khtmltts.desktop
%{_datadir}/khtml/kpartplugins/khtmltts.rc
%{_datadir}/konqueror/kpartplugins/searchbar.desktop
%{_datadir}/konqueror/kpartplugins/searchbar.rc
%{_datadir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/kwebkitpart/kpartplugins/autorefresh.desktop
%{_datadir}/kwebkitpart/kpartplugins/autorefresh.rc
%{_datadir}/kwebkitpart/kpartplugins/plugin_babelfish.rc
%{_datadir}/kwebkitpart/kpartplugins/plugin_translator.desktop
%{_datadir}/kwebkitpart/kpartplugins/plugin_validators.desktop
%{_datadir}/kwebkitpart/kpartplugins/plugin_validators.rc
%{_datadir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/kwebkitpart/kpartplugins/khtmltts.desktop
%{_datadir}/kwebkitpart/kpartplugins/khtmltts.rc
%{_datadir}/config.kcfg/validators.kcfg
%{_datadir}/icons/*/*/apps/fsview.png
%{_datadir}/icons/*/*/actions/babelfish.png
%{_datadir}/icons/*/*/actions/cssvalidator.png
%{_datadir}/icons/*/*/actions/htmlvalidator.png
%{_datadir}/icons/*/*/actions/imagegallery.png
%{_datadir}/icons/*/*/actions/validators.png
%{_datadir}/icons/*/*/actions/webarchiver.png
%{_datadir}/icons/*/scalable/actions/htmlvalidator.svgz
%{_datadir}/icons/*/scalable/actions/validators.svgz
%{_datadir}/kservices5/fsview_part.desktop
%{_datadir}/kservices5/webarchivethumbnail.desktop

#-----------------------------------------------------------------------------

%package -n konqueror
Summary:	KDE file and web browser
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Requires:	dolphin
Suggests:	keditbookmarks
Suggests:	konq-plugins
Conflicts:	kdebase4-devel < 1:4.7.90-2
Obsoletes:	kde4-nsplugins < 2:16.06

%description -n konqueror
KDE file and web browser.

%files -n konqueror
%{_sysconfdir}/xdg/translaterc
%{_sysconfdir}/xdg/autostart/konqy_preload.desktop
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml
%{_bindir}/kfmclient
%{_bindir}/konqueror
%{_datadir}/kxmlgui5/konqueror
%{_libdir}/qt5/plugins/kcm_bookmarks.so
%{_libdir}/qt5/plugins/kcm_konq.so
%{_libdir}/qt5/plugins/kcm_konqhtml.so
%{_libdir}/qt5/plugins/kcm_performance.so
%{_libdir}/qt5/plugins/konq_aboutpage.so
%{_libdir}/qt5/plugins/konq_shellcmdplugin.so
%{_libdir}/libkdeinit5_kfmclient.so
%{_libdir}/libkdeinit5_konqueror.so
%{_datadir}/config.kcfg/konqueror*
%{_datadir}/applications/kfmclient.desktop
%{_datadir}/applications/kfmclient_html.desktop
%{_datadir}/applications/kfmclient_war.desktop
%{_datadir}/kcmcss/template.css
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.rc
%{_datadir}/kf5/kbookmark/directory_bookmarkbar.desktop
%{_datadir}/kservices5/filebehavior.desktop
%{_datadir}/kservices5/kcmkonqyperformance.desktop
%{_datadir}/kservices5/kcmperformance.desktop
%{_datadir}/kservices5/khtml_behavior.desktop
%{_datadir}/kservices5/khtml_filter.desktop
%{_datadir}/kservices5/khtml_general.desktop
%{_datadir}/kservices5/khtml_java_js.desktop
%{_datadir}/kservices5/konq_aboutpage.desktop
%{_datadir}/kservices5/khtml_appearance.desktop
%{_datadir}/kservicetypes5/konqaboutpage.desktop
%{_datadir}/konqueror/
%{_datadir}/icons/*/*/*/konqueror.*
%exclude %{_datadir}/konqueror/kpartplugins/searchbar.desktop
%exclude %{_datadir}/konqueror/kpartplugins/searchbar.rc
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%{_datadir}/kcontrol/pics/onlyone.png
%{_datadir}/kcontrol/pics/overlapping.png
%{_datadir}/applications/konqbrowser.desktop
# (tpg) move it to separate subpackage ?
%{_libdir}/qt5/plugins/kf5/parts/webenginepart.so
%{_datadir}/icons/hicolor/*/*/webengine.png
%{_datadir}/kservices5/org.kde.konqueror.desktop
%{_datadir}/kservices5/webenginepart.desktop
%{_datadir}/kxmlgui5/webenginepart/webenginepart.rc

#-----------------------------------------------------------------------------

%package -n keditbookmarks
Summary:	Bookmark editor
Group:		Graphical desktop/KDE
Requires:	kde-runtime

%description -n keditbookmarks
Bookmark editor.

%files -n keditbookmarks
%{_bindir}/kbookmarkmerger
%{_bindir}/keditbookmarks
%{_datadir}/applications/org.kde.keditbookmarks.desktop
%{_datadir}/kservices5/bookmarks.desktop
%{_datadir}/config.kcfg/keditbook*
%{_datadir}/kxmlgui5/keditbookmarks

#-----------------------------------------------------------------------------

%package -n kfind
Summary:	Application finder
Group:		Graphical desktop/KDE
Requires:	kde-runtime

%description -n kfind
Application finder.

%files -n kfind
%doc %{_docdir}/HTML/en/kfind/
%{_bindir}/kfind
%{_datadir}/applications/org.kde.kfind.desktop
%{_datadir}/icons/*/*/*/kfind.*
%{_mandir}/man1/kfind.1.*
%{_datadir}/metainfo/org.kde.kfind.appdata.xml

#-----------------------------------------------------------------------------

%package -n kdialog
Summary:	Dialog KDE base widgets
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Conflicts:	kdebase4-devel < 1:4.7.90-2

%description -n kdialog
Dialog KDE base widgets.

%files -n kdialog
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_bindir}/kdialog

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs-devel
Requires:	%{libkonq} = %{EVRD}
Requires:	%{libkbookmarkmodel_private} = %{EVRD}
%rename		kdebase4-devel

%description devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%{_libdir}/libkwebenginepartlib.so
%{_libdir}/libKF5Konq.so
%{_libdir}/libkbookmarkmodel_private.so
%{_includedir}/KF5/*.h
%{_libdir}/cmake/KF5Konq

#-----------------------------------------------------------------------------

%prep
%if 0%{snapshot}
%setup -qn %{name}-%{snapshot}
%else
%setup -q -n kde-baseapps-%{version}
%endif

# Rediff ???
#patch1 -p0 -b .mdvicon
#patch104 -p1
%if %{build_iconoverlay}
%patch107 -p1 -b .icon-plugin
%patch108 -p1 -b .icon-race
%endif

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
