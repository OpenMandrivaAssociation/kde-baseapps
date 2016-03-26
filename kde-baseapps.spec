%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define build_iconoverlay 0

Summary:	K Desktop Environment 4
Name:		kde-baseapps
Version:	15.12.3
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch1:		kdebase-4.2.95-Use-Mandriva-Home-Icon.patch
Patch2:		kdebase-4.8.97-mdvuserface.patch
Patch3:		kdebase-4.10.0-fileplaces.patch
Patch4:		kdebase-4.10.2-konq-templates-cleanup.patch
Patch5:		kdebase-4.11.4-folderview-preview.patch
Patch12:	kdebase-4.8.1-Set-Preview-true.patch
Patch101:	kdebase-14.11.97-dolphinrcui.patch
Patch104:	kdebase-4.8.2-dolphin-delete-files-on-flash-drives.patch
Patch105:	kdebase-14.11.97-dolphin-klook.patch
Patch106:	kdebase-4.12.1-konqueror-settings-kio-proxy.patch
Patch107:	kdebase-4.10.0-iconoverlay-plugin.patch
Patch108:	kdebase-4.9.5-iconoverlay-race-fix.patch
#branch patches
#trunk patches
# test patches
BuildRequires:	baloo-devel
BuildRequires:	baloo-widgets-devel
BuildRequires:	kdelibs-devel >= 5:4.14.8
BuildRequires:	kfilemetadata-devel
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)
Requires:	kde-runtime
Suggests:	dolphin
Suggests:	kdepasswd
Suggests:	kde4-nsplugins
Suggests:	kdialog
Suggests:	kfind
Suggests:	konqueror
Suggests:	keditbookmarks
Requires:	plasma-applet-folderview

%description
This meta package requires all base %{name} packages.

%files
%doc README

#------------------------------------------------

%define dolphinprivate_major 4
%define libdolphinprivate %mklibname dolphinprivate4 %{dolphinprivate_major}

%package -n %{libdolphinprivate}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libdolphinprivate}
KDE 4 core library.

%files -n %{libdolphinprivate}
%{_kde_libdir}/libdolphinprivate4.so.%{dolphinprivate_major}*

#-----------------------------------------------------------------------------

%package -n dolphin4
Summary:	File manager for KDE focusing on usability
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Requires:	kfind
Suggests:	ffmpegthumbs
Suggests:	kde-odf-thumbnail
Suggests:	klook
Provides:	kde-dolphin = %{EVRD}

%description -n dolphin4
Dolphin is a file manager for KDE focusing on usability.
The main features of Dolphin are:
- Navigation bar for URLs, which allows to navigate quickly
     through the file hierarchy.
- View properties are remembered for each folder.
- Split of views is supported.
- Network transparency.
- Undo/redo functionality.
- Renaming of a variable number of selected items in one step.

Dolphin is not intended to be a competitor to Konqueror: Konqueror
acts as universal viewer being able to show HTML pages, text documents,
directories and a lot more, whereas Dolphin focuses on being only a file
manager. This approach allows to optimize the user interface for the task
of file management.

%files -n dolphin4
%{_kde_bindir}/dolphin4
%{_kde_services}/dolphinpart.desktop
%{_kde_services}/kcmdolphingeneral.desktop
%{_kde_services}/kcmdolphinnavigation.desktop
%{_kde_services}/kcmdolphinservices.desktop
%{_kde_services}/kcmdolphinviewmodes.desktop
%{_kde_services}/filenamesearch.protocol
%{_kde_servicetypes}/fileviewversioncontrolplugin.desktop
%if %{build_iconoverlay}
%{_kde_servicetypes}/iconviewoverlaycontrolplugin.desktop
%endif
%{_kde_configdir}/servicemenu.knsrc
%{_kde_libdir}/libkdeinit4_dolphin4.so
%{_kde_libdir}/kde4/dolphinpart.so
%{_kde_libdir}/kde4/kcm_dolphingeneral.so
%{_kde_libdir}/kde4/kcm_dolphinnavigation.so
%{_kde_libdir}/kde4/kcm_dolphinservices.so
%{_kde_libdir}/kde4/kcm_dolphinviewmodes.so
%{_kde_libdir}/kde4/kio_filenamesearch.so
%{_kde_appsdir}/dolphinpart/dolphinpart.rc
%{_kde_appsdir}/dolphin/
%{_kde_datadir}/templates/

#-----------------------------------------------------------------------------

%package -n kdepasswd
Summary:	User password management for KDE
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Requires:	accountsservice

%description -n kdepasswd
User password management.

%files -n kdepasswd
%doc %{_kde_docdir}/HTML/en/kdepasswd/
%{_kde_bindir}/kdepasswd
%{_kde_libdir}/kde4/kcm_useraccount.so
%{_kde_applicationsdir}/kdepasswd.desktop
%{_kde_services}/kcm_useraccount.desktop
%{_kde_datadir}/config.kcfg/kcm_useracc*
%{_kde_appsdir}/kdm/pics/users/*.png

#-----------------------------------------------------------------------------

%package -n kde4-nsplugins
Summary:	Netscape plugins wrapper for KDE
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Conflicts:	kdebase4-devel < 1:4.7.90-2

%description -n kde4-nsplugins
Netscape plugins wrapper for kde.

%files -n kde4-nsplugins
%{_datadir}/dbus-1/interfaces/org.kde.nsplugins.*.xml
%{_kde_bindir}/nspluginscan
%{_kde_bindir}/nspluginviewer
%{_kde_appsdir}/nsplugin/nspluginpart.rc
%{_kde_libdir}/kde4/libkcminit_nsplugins.so
%{_kde_libdir}/kde4/libnsplugin.so
%{_kde_services}/khtml_plugins.desktop

#------------------------------------------------

%define konq_major 5
%define libkonq %mklibname konq %{konq_major}

%package -n %{libkonq}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkonq}
KDE 4 core library.

%files -n %{libkonq}
%{_kde_libdir}/libkonq.so.%{konq_major}*

#------------------------------------------------

%define konqsidebarplugin_major 4
%define libkonqsidebarplugin %mklibname konqsidebarplugin %{konqsidebarplugin_major}

%package -n %{libkonqsidebarplugin}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkonqsidebarplugin}
KDE 4 core library.

%files -n %{libkonqsidebarplugin}
%{_kde_libdir}/libkonqsidebarplugin.so.%{konqsidebarplugin_major}*

#------------------------------------------------

%define konquerorprivate_major 4
%define libkonquerorprivate %mklibname konquerorprivate %{konquerorprivate_major}

%package -n %{libkonquerorprivate}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkonquerorprivate}
KDE 4 core library.

%files -n %{libkonquerorprivate}
%{_kde_libdir}/libkonquerorprivate.so.%{konquerorprivate_major}*

#------------------------------------------------

%define kbookmarkmodel_private_major 4
%define libkbookmarkmodel_private %mklibname kbookmarkmodel_private %{kbookmarkmodel_private_major}

%package -n %{libkbookmarkmodel_private}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkbookmarkmodel_private}
KDE 4 core library.

%files -n %{libkbookmarkmodel_private}
%{_kde_libdir}/libkbookmarkmodel_private.so.%{kbookmarkmodel_private_major}*

#------------------------------------------------

%package -n konq-plugins
Summary:	Konqueror plugins
Group:		Graphical desktop/KDE
Requires:	konqueror
Conflicts:	dolphin < 1:4.7.0

%description -n konq-plugins
This module contains plugins that interact with Konqueror.

%files -n konq-plugins
%{_kde_bindir}/fsview
%{_kde_libdir}/kde4/adblock.so
%{_kde_libdir}/kde4/akregatorkonqfeedicon.so
%{_kde_libdir}/kde4/autorefresh.so
%{_kde_libdir}/kde4/babelfishplugin.so
%{_kde_libdir}/kde4/dirfilterplugin.so
%{_kde_libdir}/kde4/domtreeviewerplugin.so
%{_kde_libdir}/kde4/fsviewpart.so
%{_kde_libdir}/kde4/khtmlsettingsplugin.so
%{_kde_libdir}/kde4/kimgallery.so
%{_kde_libdir}/kde4/minitoolsplugin.so
%{_kde_libdir}/kde4/rellinksplugin.so
%{_kde_libdir}/kde4/searchbarplugin.so
%{_kde_libdir}/kde4/uachangerplugin.so
%{_kde_libdir}/kde4/validatorsplugin.so
%{_kde_libdir}/kde4/webarchiverplugin.so
%{_kde_libdir}/kde4/webarchivethumbnail.so
%{_kde_appsdir}/akregator/pics/feed.png
%{_kde_appsdir}/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_kde_appsdir}/dolphinpart/kpartplugins/dirfilterplugin.rc
%{_kde_appsdir}/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_kde_appsdir}/dolphinpart/kpartplugins/kimgalleryplugin.rc
%{_kde_appsdir}/domtreeviewer/domtreeviewerui.rc
%{_kde_appsdir}/fsview/fsview_part.rc
%{_kde_appsdir}/khtml/kpartplugins/akregator_konqfeedicon.desktop
%{_kde_appsdir}/khtml/kpartplugins/akregator_konqfeedicon.rc
%{_kde_appsdir}/khtml/kpartplugins/autorefresh.desktop
%{_kde_appsdir}/khtml/kpartplugins/autorefresh.rc
%{_kde_appsdir}/khtml/kpartplugins/khtmlsettingsplugin.desktop
%{_kde_appsdir}/khtml/kpartplugins/khtmlsettingsplugin.rc
%{_kde_appsdir}/khtml/kpartplugins/minitoolsplugin.desktop
%{_kde_appsdir}/khtml/kpartplugins/minitoolsplugin.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_adblock.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_adblock.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_babelfish.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_domtreeviewer.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_domtreeviewer.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_rellinks.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_rellinks.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_translator.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_validators.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_validators.rc
%{_kde_appsdir}/khtml/kpartplugins/plugin_webarchiver.desktop
%{_kde_appsdir}/khtml/kpartplugins/plugin_webarchiver.rc
%{_kde_appsdir}/khtml/kpartplugins/uachangerplugin.desktop
%{_kde_appsdir}/khtml/kpartplugins/uachangerplugin.rc
%{_kde_appsdir}/konqueror/icons/oxygen/*/actions/google.png
%{_kde_appsdir}/konqueror/icons/oxygen/scalable/actions/google.svgz
%{_kde_appsdir}/konqueror/kpartplugins/searchbar.desktop
%{_kde_appsdir}/konqueror/kpartplugins/searchbar.rc
%{_kde_appsdir}/konqueror/opensearch/google.xml
%{_kde_appsdir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.rc
%{_kde_appsdir}/kwebkitpart/kpartplugins/autorefresh.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/autorefresh.rc
%{_kde_appsdir}/kwebkitpart/kpartplugins/plugin_babelfish.rc
%{_kde_appsdir}/kwebkitpart/kpartplugins/plugin_translator.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/plugin_validators.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/plugin_validators.rc
%{_kde_appsdir}/kwebkitpart/kpartplugins/uachangerplugin.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/uachangerplugin.rc
%{_kde_appsdir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.rc
%{_kde_datadir}/config.kcfg/validators.kcfg
%{_kde_configdir}/translaterc
%{_kde_iconsdir}/hicolor/*/apps/fsview.png
%{_kde_iconsdir}/oxygen/*/actions/babelfish.png
%{_kde_iconsdir}/oxygen/*/actions/cssvalidator.png
%{_kde_iconsdir}/oxygen/*/actions/htmlvalidator.png
%{_kde_iconsdir}/oxygen/*/actions/imagegallery.png
%{_kde_iconsdir}/oxygen/*/actions/validators.png
%{_kde_iconsdir}/oxygen/*/actions/webarchiver.png
%{_kde_iconsdir}/oxygen/scalable/actions/htmlvalidator.svgz
%{_kde_iconsdir}/oxygen/scalable/actions/validators.svgz
%{_kde_services}/ServiceMenus/imageconverter.desktop
%{_kde_services}/fsview_part.desktop
%{_kde_services}/webarchivethumbnail.desktop

#-----------------------------------------------------------------------------

%package -n konqueror
Summary:	KDE file and web browser
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Requires:	dolphin
Suggests:	keditbookmarks
Suggests:	konq-plugins
Conflicts:	kdebase4-devel < 1:4.7.90-2

%description -n konqueror
KDE file and web browser.

%files -n konqueror
%{_datadir}/dbus-1/interfaces/org.kde.FavIcon.xml
%{_datadir}/dbus-1/interfaces/org.kde.?onqueror.*.xml
%doc %{_kde_docdir}/HTML/en/konqueror/
%{_kde_bindir}/kfmclient
%{_kde_bindir}/konqueror
%{_kde_libdir}/kde4/kded_konqy_preloader.so
%{_kde_libdir}/kde4/kcm_kio.so
%{_kde_libdir}/kde4/kcm_konq.so
%{_kde_libdir}/kde4/kcm_konqhtml.so
%{_kde_libdir}/kde4/kcm_kurifilt.so
%{_kde_libdir}/kde4/kcm_performance.so
%{_kde_libdir}/kde4/konq_aboutpage.so
%{_kde_libdir}/kde4/konq_shellcmdplugin.so
%{_kde_libdir}/kde4/konq_sidebar.so
%{_kde_libdir}/kde4/konq_sidebartree_dirtree.so
%{_kde_libdir}/kde4/konqsidebar_tree.so
%{_kde_libdir}/kde4/konqsidebar_web.so
%{_kde_libdir}/kde4/khtmlkttsdplugin.so
%{_kde_libdir}/libkdeinit4_kfmclient.so
%{_kde_libdir}/libkdeinit4_konqueror.so
%{_kde_libdir}/kde4/kcm_history.so
%{_kde_libdir}/kde4/kded_favicons.so
%{_kde_libdir}/kde4/konq_sound.so
%{_kde_libdir}/kde4/konq_sidebartree_bookmarks.so
%{_kde_libdir}/kde4/konqsidebar_history.so
%{_kde_libdir}/kde4/konqsidebar_places.so
%{_kde_libdir}/kde4/libexec/kcmproxyhelper
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmproxy.conf
%{_kde_datadir}/polkit-1/actions/org.kde.kcontrol.kcmproxy.policy
%{_kde_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmproxy.service
%{_kde_appsdir}/kcontrol/*
%{_kde_datadir}/config.kcfg/konqueror*
%{_kde_applicationsdir}/Home.desktop
%{_kde_applicationsdir}/kfmclient.desktop
%{_kde_applicationsdir}/kfmclient_dir.desktop
%{_kde_applicationsdir}/kfmclient_html.desktop
%{_kde_applicationsdir}/kfmclient_war.desktop
%{_kde_appsdir}/kcmcss/template.css
%{_kde_appsdir}/khtml/kpartplugins/khtmlkttsd.desktop
%{_kde_appsdir}/khtml/kpartplugins/khtmlkttsd.rc
%{_kde_appsdir}/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_kde_appsdir}/dolphinpart/kpartplugins/kshellcmdplugin.rc
%{_kde_appsdir}/konqsidebartng
%{_kde_appsdir}/kbookmark/directory_bookmarkbar.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/khtmlkttsd.desktop
%{_kde_appsdir}/kwebkitpart/kpartplugins/khtmlkttsd.rc
%{_kde_datadir}/autostart/konqy_preload.desktop
%{_kde_configdir}/konqsidebartngrc
%{_kde_services}/cache.desktop
%{_kde_services}/cookies.desktop
%{_kde_services}/ebrowsing.desktop
%{_kde_services}/filebehavior.desktop
%{_kde_services}/kcmkonqyperformance.desktop
%{_kde_services}/kcmperformance.desktop
%{_kde_services}/kded/konqy_preloader.desktop
%{_kde_services}/khtml_behavior.desktop
%{_kde_services}/khtml_filter.desktop
%{_kde_services}/khtml_general.desktop
%{_kde_services}/khtml_java_js.desktop
%{_kde_services}/konq_aboutpage.desktop
%{_kde_services}/konq_sidebartng.desktop
%{_kde_services}/konqueror.desktop
%{_kde_services}/netpref.desktop
%{_kde_services}/proxy.desktop
%{_kde_services}/smb.desktop
%{_kde_services}/useragent.desktop
%{_kde_services}/useragentstrings
%{_kde_services}/khtml_appearance.desktop
%{_kde_services}/kcmhistory.desktop
%{_kde_servicetypes}/konqaboutpage.desktop
%{_kde_servicetypes}/uasprovider.desktop
%{_kde_servicetypes}/konqdndpopupmenuplugin.desktop
%{_kde_appsdir}/konqueror/
%{_kde_iconsdir}/*/*/*/konqueror.*
%{_kde_services}/kded/favicons.desktop
%{_kde_servicetypes}/konqpopupmenuplugin.desktop
%exclude %{_kde_appsdir}/konqueror/icons/oxygen/*/actions/google.png
%exclude %{_kde_appsdir}/konqueror/icons/oxygen/scalable/actions/google.svgz
%exclude %{_kde_appsdir}/konqueror/kpartplugins/searchbar.desktop
%exclude %{_kde_appsdir}/konqueror/kpartplugins/searchbar.rc
%exclude %{_kde_appsdir}/konqueror/opensearch/google.xml
%{_datadir}/appdata/konqueror.appdata.xml

#-----------------------------------------------------------------------------

%package -n keditbookmarks
Summary:	Bookmark editor
Group:		Graphical desktop/KDE
Requires:	kde-runtime

%description -n keditbookmarks
Bookmark editor.

%files -n keditbookmarks
%{_kde_bindir}/kbookmarkmerger
%{_kde_bindir}/keditbookmarks
%{_kde_libdir}/libkdeinit4_keditbookmarks.so
%{_kde_applicationsdir}/keditbookmarks.desktop
%{_kde_services}/bookmarks.desktop
%{_kde_appsdir}/keditbookmarks
%{_kde_datadir}/config.kcfg/keditbook*
%{_kde_mandir}/man1/kbookmarkmerger.1.*

#-----------------------------------------------------------------------------

%package -n kfind
Summary:	Application finder
Group:		Graphical desktop/KDE
Requires:	kde-runtime

%description -n kfind
Application finder.

%files -n kfind
%doc %{_kde_docdir}/HTML/en/kfind/
%{_kde_bindir}/kfind
%{_kde_applicationsdir}/kfind.desktop
%{_kde_iconsdir}/*/*/*/kfind.*
%{_kde_mandir}/man1/kfind.1.*
%{_datadir}/appdata/kfind.appdata.xml

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
%{_kde_bindir}/kdialog

#-----------------------------------------------------------------------------

%package -n plasma-applet-folderview
Summary:	Display the content of folders (Desktop as default)
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Provides:	plasma-applet

%description -n plasma-applet-folderview
Display the content of folders (Desktop as default).

%files -n plasma-applet-folderview
%{_kde_libdir}/kde4/plasma_applet_folderview.so
%{_kde_services}/plasma-applet-folderview.desktop

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs-devel
Requires:	%{libdolphinprivate} = %{EVRD}
Requires:	%{libkonq} = %{EVRD}
Requires:	%{libkonqsidebarplugin} = %{EVRD}
Requires:	%{libkbookmarkmodel_private} = %{EVRD}
%rename		kdebase4-devel

%description devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%{_kde_libdir}/libdolphinprivate4.so
%{_kde_libdir}/libkonq.so
%{_kde_libdir}/libkonqsidebarplugin.so
%{_kde_libdir}/libkbookmarkmodel_private.so
%{_kde_includedir}/*.h

#-----------------------------------------------------------------------------

%prep
%setup -q -n kde-baseapps-%{version}

# Rediff
%patch1 -p0 -b .mdvicon
%patch2 -p1 -b .mdvface
%patch3 -p1 -b .fileplaces
%patch4 -p1 -b .konq-templates
%patch5 -p1 -b .folder-preview
%patch12 -p1
%patch101 -p1 -b .uirc~
#patch104 -p1
%patch105 -p1 -b .0105~
%patch106 -p1 -b .0106~
%if %{build_iconoverlay}
%patch107 -p1 -b .icon-plugin
%patch108 -p1 -b .icon-race
%endif

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_datadir}/applications/kde4/konqbrowser.desktop
rm -f %{buildroot}%{_kde_datadir}/applications/kde4/konquerorsu.desktop
