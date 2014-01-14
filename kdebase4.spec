%define build_iconoverlay 0

Summary:	K Desktop Environment
Name:		kdebase4
Version:	4.12.1
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/kde-baseapps-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch1:		kdebase-4.2.95-Use-Mandriva-Home-Icon.patch
Patch2:		kdebase-4.8.97-mdvuserface.patch
Patch3:		kdebase-4.10.0-fileplaces.patch
Patch4:		kdebase-4.10.2-konq-templates-cleanup.patch
Patch12:	kdebase-4.8.1-Set-Preview-true.patch
Patch13:	kdebase-4.8.1-kdepasswd-kcm.patch
Patch101:	kdebase-4.12.1-dolphinrcui.patch
Patch104:	kdebase-4.8.2-dolphin-delete-files-on-flash-drives.patch
Patch105:	kdebase-4.12.1-dolphin-klook.patch
Patch106:	kdebase-4.12.1-konqueror-settings-kio-proxy.patch
Patch107:	kdebase-4.10.0-iconoverlay-plugin.patch
Patch108:	kdebase-4.9.5-iconoverlay-race-fix.patch
#branch patches
#trunk patches
# test patches
BuildRequires:	kdelibs4-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	nepomuk-widgets-devel
BuildRequires:	tidy-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libkactivities) >= 4.9.80
Requires:	kdebase4-runtime
Suggests:	dolphin
Suggests:	kdepasswd
Suggests:	kde4-nsplugins
Suggests:	kdialog
Suggests:	kfind
Suggests:	konqueror
Suggests:	keditbookmarks
Requires:	plasma-applet-folderview

%description
This meta package requires all base kdebase 4 packages.

%files
%doc README

#------------------------------------------------

%define dolphinprivate_major 4
%define libdolphinprivate %mklibname dolphinprivate %{dolphinprivate_major}

%package -n %{libdolphinprivate}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libdolphinprivate}
KDE 4 core library.

%files -n %{libdolphinprivate}
%{_kde_libdir}/libdolphinprivate.so.%{dolphinprivate_major}*

#-----------------------------------------------------------------------------

%package -n dolphin
Summary:	File manager for KDE focusing on usability
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	kfind
Provides:	dolphin4
Suggests:	ffmpegthumbs
Suggests:	kde-odf-thumbnail
Suggests:	klook
Provides:	kde4-dolphin = %{EVRD}

%description -n dolphin
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

%files -n dolphin
%doc %{_kde_docdir}/HTML/en/dolphin/
%{_kde_bindir}/dolphin
%{_kde_bindir}/servicemenudeinstallation
%{_kde_bindir}/servicemenuinstallation
%{_kde_applicationsdir}/dolphin.desktop
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
%{_kde_datadir}/config.kcfg/dolphin_*
%{_kde_libdir}/libkdeinit4_dolphin.so
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
Summary:	Kdepasswd
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime

%description -n kdepasswd
User password management

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
Summary:	Netscape plugins wrapper for kde
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
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
Requires:	kdebase4-runtime
Requires:	dolphin
Suggests:	keditbookmarks
Suggests:	konq-plugins
Conflicts:	kdebase4-devel < 1:4.7.90-2

%description -n konqueror
KDE file and web browser

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

#-----------------------------------------------------------------------------

%package -n keditbookmarks
Summary:	Bookmark editor
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime

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
Requires:	kdebase4-runtime

%description -n kfind
Application finder

%files -n kfind
%doc %{_kde_docdir}/HTML/en/kfind/
%{_kde_bindir}/kfind
%{_kde_applicationsdir}/kfind.desktop
%{_kde_iconsdir}/*/*/*/kfind.*
%{_kde_mandir}/man1/kfind.1.*

#-----------------------------------------------------------------------------

%package -n kdialog
Summary:	Dialog KDE base widgets
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Conflicts:	kdebase4-devel < 1:4.7.90-2

%description -n kdialog
Dialog KDE base widgets

%files -n kdialog
%{_datadir}/dbus-1/interfaces/org.kde.kdialog.ProgressDialog.xml
%{_kde_bindir}/kdialog

#-----------------------------------------------------------------------------

%package -n plasma-applet-folderview
Summary:	Display the content of folders (Desktop as default)
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet

%description -n plasma-applet-folderview
Display the content of folders (Desktop as default)

%files -n plasma-applet-folderview
%{_kde_libdir}/kde4/plasma_applet_folderview.so
%{_kde_services}/plasma-applet-folderview.desktop

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for kdebase 4
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libdolphinprivate} = %{EVRD}
Requires:	%{libkonq} = %{EVRD}
Requires:	%{libkonqsidebarplugin} = %{EVRD}
Requires:	%{libkbookmarkmodel_private} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%{_kde_libdir}/libdolphinprivate.so
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
%patch12 -p1
%patch13 -p1
%patch101 -p1
#patch104 -p1
%patch105 -p1 -b .0105~
%patch106 -p1 -b .0106~
%if %{build_iconoverlay}
%patch107 -p1 -b .icon-plugin
%patch108 -p1 -b .icon-race
%endif

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_datadir}/applications/kde4/konqbrowser.desktop
rm -f %{buildroot}%{_kde_datadir}/applications/kde4/konquerorsu.desktop

%changelog
* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1
- Re-diff dolphinrcui patch
- Re-diff klook patch
- Re-diff konqueror-settings-kio-proxy patch

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4
- Drop no longer needed revert-unsupported patch

* Wed Nov 27 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-2
- Add revert-unsupported patch from upstream to fix regression in Dolphin

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- Drop dolphin-showdelete patch
- Re-diff dolphin-klook patch
- Update files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5
- Re-diff dolphin-klook patch

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Thu May 23 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-2
- Update konq-templates-cleanup patch to remove more entries in Create menu

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Fri Apr 26 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-2
- Add konq-templates-cleanup patch to remove some useless entries in Create menu

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Mon Feb 11 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-2
- Make iconoverlay stuff optional and disable it for now

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Re-diff some patches
- Add patch 108 (fixes a race in IconOverlay plugin for Dolphin (Rosa bug #1519))
- Drop konq-templates-cleanup patch because it's really no longer needed due to
  template cleanups in upstream
- Add BuildRequires nepomuk-core-devel, nepomuk-widgets-devel, tidy-devel,
  pkgconfig(glib-2.0), pkgconfig(libkactivities)
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Fri Nov 04 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 1:4.9.3-4
- New Klook patch

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-3
- New version 4.9.2
- Add kdebase-4.8.3-konqueror-settings-kio-proxy patch and update files
- Add rpmlint filters

* Fri Sep 28 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 1:4.9.1-2
- Adapted Klook patches to KDE 4.9

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Fri Aug 03 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Re-diff konq-templates-cleanup patch

* Wed Jul 25 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-3
- Add fileplaces patch to fix issue with missing custom translations in
  Dolphin (Music, Pictures etc)

* Tue Jul 24 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-2
- Re-diff and enable mdvuserface patch

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Drop no longer needed Conflicts and Obsoletes
- Improve KDE4 macros path usage is files
- Change kdebase-devel to kdebase4-devel in Conflicts
- Convert BuildRequires to pkgconfig style

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Tue Jun 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Many patches require re-diff, comment them out for now

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu Jun 1 2012 Evgeniy Auzhin <evgeniy.augin@osinit.ru> 1:4.8.3-4
- Patch to add Klook overlay icon for items in file views in Dolphin

* Thu May 31 2012 Alexander Skakov <alexander.skakov@osinit.ru> 1:4.8.3-3
- Patch to immediately remove files from removable medias instead of using trash bin in dolphin

* Fri May 18 2012 Alexander Skakov <alexander.skakov@osinit.ru> 1:4.8.3-2
- Fixed patch kdebase-4.8.2-konq-templates-cleanup.patch

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Fri Apr 27 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:4.8.2-11
- Fixed mandriva user face patch

* Wed Apr 18 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-10
- bump release

* Tue Apr 17 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-9
- drop konqueror desktop files

* Sat Apr 14 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:4.8.2-8
- Fixed konq templates cleanup patch

* Fri Apr 13 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 1:4.8.2-7
- Fixed dolphin Delete context menu item

* Mon Apr 9 2012 Mikhail Kompaniets <mkompan@mezon.ru> 1:4.8.2-2
- localization patch for .desktop files

* Sun Apr  6 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Tue Apr 03 2012 Alexander Skakov <alexandr.skakov@osinit.ru> 1:4.8.1-10
- Added old patch to display "Create Symlink" item in dolphin context menu

* Tue Apr 03 2012 Alexander Skakov <alexandr.skakov@osinit.ru> 1:4.8.1-9
- Added old patch to fix dolphin context menu

* Thu Mar 29 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 1:4.8.1-7
- Replaced patch for kdepasswd

* Wed Mar 28 2012 Alexander Skakov <alexandr.skakov@osinit.ru> 1:4.8.1-6
- Removed unnecessary menu items in "Create new" menu throughout KDE

* Wed Mar 28 2012 Sergey Borovkov <sergey.borovkov@osinit.ru> 1:4.8.1-5
- Fix bug that cause control centre hanging when user tried to change name

* Wed Mar 28 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-4
- enable icons preview

* Mon Mar 26 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-3
- klook import

* Fri Mar 16 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-2
- use internal dolphin

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1
- fix dolphin show delete

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762415
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758116
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748790
- New version

  + Zé <ze@mandriva.org>
    - clean defattr
    - dbus insterface .xml files are not development files
    - tag doc files

* Tue Dec 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 740654
- Fix file list
- Try to fix buildrequire
- Add missing source
- New upstream tarball

* Wed Nov 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732747
- New upstream tarball

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:4.7.41-5
+ Revision: 702915
- attempt to relink against libpng15.so.15

* Fri Sep 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-4
+ Revision: 699091
- Fix file list
- Fix file list
- Fix file list
- Fix file list
- Remove konsole it is on it own package now
- Update to kde 4.7.41

* Wed Jun 29 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:4.6.4-4
+ Revision: 688289
- Proper buildrequires

  + Alex Burmashev <burmashev@mandriva.org>
    - one more spec change
    - buildrequires fix
    - buildrequires fix
    - fixed requires for Sync
    - spec fix
    - added dolphin sync patch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo
    - Fix typo

* Mon Jun 27 2011 Alex Burmashev <burmashev@mandriva.org> 1:4.6.4-3
+ Revision: 687451
- small spec fix for patch13
- Changed dolphin preview option to true

* Tue Jun 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-2
+ Revision: 686515
- Add new dolphin UI

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684416
- New version 4.6.4
- Fix avatar size ( from eugeni)

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674400
- new version 4.6.3

* Tue Apr 26 2011 Alex Burmashev <burmashev@mandriva.org> 1:4.6.2-2
+ Revision: 659349
- dolphin ui change

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650767
- Remove mkrel
- New version 4.6.2

* Wed Mar 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-2
+ Revision: 643082
- Use new tarball
- Disable patch4
- Fix patches
- Use new tarball
- New version 4.6.1

* Thu Feb 17 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-2
+ Revision: 638106
- Suggests konq-plugins
  CCBUG: 62519

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-1
+ Revision: 634351
- BR libxt

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629133
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624076
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616358
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601449
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599109
- new version 4.5.77

* Sat Nov 13 2010 Funda Wang <fwang@mandriva.org> 1:4.5.76-0.svn1196353.1mdv2011.0
+ Revision: 597050
- new snapshot 4.5.76

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589737
- new snapshot 4.5.74

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1183606.1mdv2011.0
+ Revision: 584108
- update file list
- New snapshot 4.5.71
- kdebase apps has nothing to do with workspace

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578401
- apply more patches
- patch9 does not apply any more
- empty trash patch merged upstream
- transbin configure menu merged upstream
- apply patches again
- apply mdvuserface patch
- use home-mdk icon from all themes
- there is no kappfinder and dolphin is using correct category now
- New snapshot 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576411
- Remove old conflicts
- New version 4.5.67

* Tue Aug 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.65-2mdv2011.0
+ Revision: 574948
- Rebuild
- Update to kde 4.5.65

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566581
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562629
- kde 4.4.95

* Fri May 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-7mdv2010.1
+ Revision: 546486
- Requires kde-odf-thumbnail
  CCBUG: 59429

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-6mdv2010.1
+ Revision: 546024
- Fixed typo
- Fix dolphin annotation patch

* Tue May 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-5mdv2010.1
+ Revision: 545910
- Fix dolphin annotation

* Mon May 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-4mdv2010.1
+ Revision: 545821
- Add pcpa patch fixing konsole fonts ( P301 )
  CCBUG: 57564

* Thu May 13 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-3mdv2010.1
+ Revision: 544669
- Add ffmpegthumbs as suggests for dolphin
  Change requires into suggests

* Mon May 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-2mdv2010.1
+ Revision: 544366
- Add nepomuk-scribo as buildrequire
- Fix typo
- Sync patches with branch
- Add an nepomuk anotation in dolphin

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542140
- Update to version 4.4.3

* Fri Apr 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-6mdv2010.1
+ Revision: 541380
- Move template files into the dolphin package
  CCBUG: 58999
- Add a default shortcut for hidding the menubar

* Thu Apr 15 2010 Funda Wang <fwang@mandriva.org> 1:4.4.2-4mdv2010.1
+ Revision: 534982
- rebuild

* Thu Apr 01 2010 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:4.4.2-2mdv2010.1
+ Revision: 530725
- Added patch that adds text eliding on first line of a dolphin icon

* Tue Mar 30 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 529661
- Fix compilation, thanks to rodrigo
- Add a debug in konsole
- Update to version 4.4.2

* Thu Mar 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-13mdv2010.1
+ Revision: 527507
- Handle the emptytrash case

* Thu Mar 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-12mdv2010.1
+ Revision: 527398
- Add an option to allow to configure the trash bin

* Sat Mar 20 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-11mdv2010.1
+ Revision: 525395
- Remove unwanted part of the patch
- New version of the kcm_accountmanager patch

* Sat Mar 20 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-9mdv2010.1
+ Revision: 525385
- Fix a crash in kdepasswd where there is no plugged webcam

* Tue Mar 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-8mdv2010.1
+ Revision: 522507
- Fix BuildRequires
- Use kcm-webcam in main kdepasswd

* Wed Mar 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-6mdv2010.1
+ Revision: 513840
- Remove merged patch
- Update to version 4.4.1

  + Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com>
    - Changing patch for folderview (added an slider to change the icon frame width)

* Thu Feb 25 2010 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:4.4.0-5mdv2010.1
+ Revision: 511232
- Added patch that allow user to use a fadding effect on the icon label (folderview)

* Wed Feb 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-4mdv2010.1
+ Revision: 507315
- Backport nepomuk fixes from branch

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-3mdv2010.1
+ Revision: 503459
- Fix file list
- Update to version 4.4.0

* Sun Feb 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-2mdv2010.1
+ Revision: 501525
- Allow to execute script in dolphin

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498940
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Tue Jan 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 496511
- Fix file list
- Remove unused buildrequire
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488241
- Fix  file list
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480695
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 473158
- Update to kde 4.4 Beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470773
- add webkitkde-devel as buildrequire
- Update to kde 4.3.77

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 466596
- Update to kde 4.3.75
  Removed webkitkde Buildrequire until the rpm is fixed
  Fix file list

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-3mdv2010.1
+ Revision: 464591
- Rebuild

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 462459
- Remove wrong Require

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 462389
- Update to kde 4.3.73

* Wed Oct 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-3mdv2010.0
+ Revision: 459627
- Fix password modification in kdepasswd ( BKO #212004)

* Sun Oct 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.2-2mdv2010.0
+ Revision: 459204
- Add 2 patches fixing xdg-user issues

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454426
- New upstream release 4.3.2.

* Thu Sep 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-4mdv2010.0
+ Revision: 444183
- Obsolete kde3 packages

* Thu Sep 17 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-3mdv2010.0
+ Revision: 443987
- Rebuild against mistaken removal

* Sat Sep 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 438578
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423204
- New upstream release 4.3.1.

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409400
- New upstream release 4.3.0.

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.98-1mdv2010.0
+ Revision: 398723
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394584
- Update to Rc2

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-3mdv2010.0
+ Revision: 389816
- Apply previous patch
- Use mandriva icon for Home.desktop

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389158
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 382682
- Update to beta2

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.88-3mdv2010.0
+ Revision: 381065
- Remove requires on konqueror in the dolphin package
- Konqueror must requires dolphin, if not the file manager part does not work

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.88-1mdv2010.0
+ Revision: 380732
- Update to kde 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378779
- Update to kde   4.2.87

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373517
- Update to kde 4.2.85

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371518
- Update to kde 4.2.71

* Thu Apr 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369154
- Update to kde 4.2.70
  Rediff patches
  Remove merged patches
  Fix File list

* Fri Apr 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-7mdv2009.1
+ Revision: 367879
- Really apply patch110

* Wed Apr 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-6mdv2009.1
+ Revision: 367593
- Fix panel size when hovering files

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-5mdv2009.1
+ Revision: 365928
- Add some upstream patches from branch
        - Patch108: Show tab names containing '&' correctly in Konqueror. ( KDE bug #189281 )
        - Patch109: Adjust the first column width to the maximum needed   ( KDE bug #178794 )

* Tue Apr 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-4mdv2009.1
+ Revision: 364679
- Add two patches from trunk
    - Fix shortcuts in folderview
    - Allow to add cashew actions in the folderview right click

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-3mdv2009.1
+ Revision: 364381
- Add Upstream patches from the 4.2 branch
    - Patch107: Fixed regression introduced with KDE 4.2.0 that the column width setting was ignored.

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-2mdv2009.1
+ Revision: 364123
- Add some upstream patches from branch
        - Patch100: Fix local service menus and built-in local services not being shown
        - Patch101: When looking for a frame by name, look first in the calling part
        - Patch102: Use a better way to ensure that the popup is closed when the user clicks outside of it.
        - Patch103: Fix openUrlRequest
        - Patch104: Fixes the problem that multiple tabs might get opened on middle clicking a folder in Columns View.
        - Patch105: Folderview: Fix a valgrind warning about an uninitialized variable.
        - Patch106: KFind: Now using "locate" returns results properly

* Sun Mar 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 362076
- Update to kde 4.2.2
  Remove merged patches

* Wed Mar 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.1-5mdv2009.1
+ Revision: 357245
- Obsoletes old kde3 konsole
- Obsolete old kdebase-nsplugins

* Wed Mar 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-3mdv2009.1
+ Revision: 348467
- Added konqueror conflicts for old kde4-nsplugins in 2009.0

* Wed Mar 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-2mdv2009.1
+ Revision: 348383
- New "smart" detection code in konsole braking completly the selction behavior. Reverting to 4.2.0 process until upstream is notified

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 346118
- KDE 4.2.1 try#1 upstream release

* Wed Feb 25 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.0-9mdv2009.1
+ Revision: 344931
- Make Mandriva systemn settings user dialog compliant with faces dir used in our distro

* Tue Feb 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-8mdv2009.1
+ Revision: 344529
- remove patch200

* Sun Feb 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-7mdv2009.1
+ Revision: 343999
- Fix patch
- [Trunk] Allow to move tabs
- Revert the revert ( was not the origin of the issue)

* Wed Feb 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-6mdv2009.1
+ Revision: 342556
- Revert upstream commit 903395 for tests purposes

* Sun Feb 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-5mdv2009.1
+ Revision: 340649
- Remove SuperUser profile, asked by upstream

* Sun Feb 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-4mdv2009.1
+ Revision: 340607
- Fix konsole with Vim
- Add a SuperUser profiles ( proposed upstream)

* Mon Feb 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 336401
- Enable testing to allow to copy/paste on folderview

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.0-1mdv2009.1
+ Revision: 334608
- Bring back the webkit part
- Update with official 4.2.0 upstream tarball

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires (Bug  #47250)

* Thu Jan 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-2mdv2009.1
+ Revision: 329938
- Rebuild

* Thu Jan 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327284
- Fix file list
- Remove merged patches

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 1:4.1.85-3mdv2009.1
+ Revision: 320842
- rebuild for new raw1394

* Wed Dec 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-2mdv2009.1
+ Revision: 318325
- fix write of mimeapps.list
- Testing patch from dfaure when adding file association

* Fri Dec 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 313755
- Fix File list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 312977
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-1mdv2009.1
+ Revision: 308577
- Update to kde 4.1.81
- Fix folderview description and summary

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304866
- Fix BuildRequires ( because of KNewPasswordDialog::checkAndGetPassword )

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303168
- Fix install
- Update to kde 4.1.73
  Fix file list
  Use %%makeinstall macros
  Remove the rm -fr on a non existant file

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-1mdv2009.1
+ Revision: 297014
- Update to kde 4.1.71

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.70-2mdv2009.1
+ Revision: 295842
- Update to kde 4.1.70

* Sun Sep 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.2-4mdv2009.0
+ Revision: 289072
- fix parsing Konsole command in profiles ( from trunk )

* Sat Sep 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.2-3mdv2009.0
+ Revision: 288958
- [BUGFIX] Allow to rename folder on the sidebar (Bug #43796)

* Fri Sep 26 2008 Daniel Pestana de Gouveia <dpg@mandriva.com.br> 1:4.1.2-2mdv2009.0
+ Revision: 288662
- Fix drag-and-dropping files to the sidebar in Konqueror (#44095)

* Fri Sep 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288331
- KDE 4.1.2 arriving.

* Thu Sep 18 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-5mdv2009.0
+ Revision: 285652
- Post 4.1.1 branch past - konqueror masking ssl connections in listbox

* Wed Sep 17 2008 Michael Scherer <misc@mandriva.org> 1:4.1.1-4mdv2009.0
+ Revision: 285421
- enhance konsole, kappfinder and konqueror summary
- automated end of line fix ( vim macro that remove whitespace at the end )
- fix Summary of kwrite and dolphin, fix #42918 and #42919, dolphin desc take from the old contrib package

* Fri Sep 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-3mdv2009.0
+ Revision: 284172
- kdecore already requests a phonon backend, so we should not requires here

* Thu Sep 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-2mdv2009.0
+ Revision: 280648
- Convenience requires

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277483
- Upgrade to forthcoming 4.1.1 packages
- Prepare for 4.1.1. Added requires for misc-misc improving konsole font

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add kfind as require of dolphin

* Sun Aug 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.0-4mdv2009.0
+ Revision: 273110
- Move kcm_filetypes in dolphin

* Mon Aug 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-3mdv2009.0
+ Revision: 263380
- Update with current branch 4.1 patches
- Update with current branch 4.1 patches

* Mon Jul 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-2mdv2009.0
+ Revision: 251559
- We should not requires pieces of kdeplasma-addons

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247543
- Update with Release Candidate 1 - 4.1.0

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add keditbookmarks as a suggest of Konqueror

* Fri Jul 11 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-2mdv2009.0
+ Revision: 233636
- Update with Release Candidate 1 - 4.0.98

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix dolphin menu location

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232351
- Update to kde 4.0.85
- Move dolphin on the office section (menu cleaning task)

* Thu Jul 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-3mdv2009.0
+ Revision: 231402
- Add patch0 : Do not show kappfinder on tthe menu

* Wed Jul 02 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-2mdv2009.0
+ Revision: 230824
- recompile against plasma applet changes

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-1mdv2009.0
+ Revision: 229402
- Update with new snapshot tarballs 4.0.84

  + Anssi Hannula <anssi@mandriva.org>
    - fix wrong major in libkonquerorprivate and libdolphinprivate
    - ensure major correctness in file lists
    - add another conflict for smooth upgrade

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-5mdv2009.0
+ Revision: 226121
- Update with new snapshot tarballs 4.0.83
- Fix packaging bug found by anssi on libkonq
- Obsoletes 4.0.3 packages released before

  + Anssi Hannula <anssi@mandriva.org>
    - add more conflicts for smooth upgrade

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-3mdv2009.0
+ Revision: 218616
- Fixed name os applet to match other ones in kdeplasma

* Thu Jun 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.82-2mdv2009.0
+ Revision: 218587
- Fix Requires on plasma-applets-folderview

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-1mdv2009.0
+ Revision: 218482
- And now we reach a proper nomenclature for plasma items arriving
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-2mdv2009.0
+ Revision: 214855
- Update with new snapshot tarballs 4.0.81

* Fri May 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 213313
- New snapshot 4.0.81

* Sat May 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 210924
- Own %%_kde_appsdir/plugin
- Remove unneeded Buildrequires
- Rebuild against new soprano

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

* Sat May 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-3mdv2009.0
+ Revision: 208373
- Rebuild because of BS failure
- Versionate BuildRequires
- Rebuild against new kdepimlibs4

  + Funda Wang <fwang@mandriva.org>
    - New version 4.0.74

* Wed May 14 2008 Anssi Hannula <anssi@mandriva.org> 1:4.0.73-4mdv2009.0
+ Revision: 207347
- add another conflict with old kde3 for smooth upgrade

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-3mdv2009.0
+ Revision: 204709
- Update to kde 4.0.73

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-3mdv2009.0
+ Revision: 203292
- Fix conflicts against old kde3

* Tue May 06 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.72-2mdv2009.0
+ Revision: 202261
- No need conflicts with nsplugin from kdebase4 for now

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-1mdv2009.0
+ Revision: 202052
- Fix BuildRequires
- Update to kde 4.0.72
- Fix file list
- New snapshot 4.0.70
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 190991
- Update for last stable release 4.0.3

* Mon Mar 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-4mdv2008.1
+ Revision: 183935
- Backport 2 patches of kde 4.0.3
  	* Fix size in dolphin
  	* Fix crash in dolphin

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-3mdv2008.1
+ Revision: 182139
- Rebuild against new qt4 changes

* Sun Mar 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 177691
- Fix conflict with kde4-kinfocenter (part 2)

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177439
- New upstream bugfix release 4.0.2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add ifdef statement to allow backports again

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized
    - fix description-line-too-long

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 164770
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE Team

* Sun Jan 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-1.765555.2mdv2008.1
+ Revision: 158702
- Rebuild because of missing signatures

* Thu Jan 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1.765555.1mdv2008.1
+ Revision: 157668
- Update for current 4.0 branch

* Tue Jan 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 146492
- Updated to official 4.0.0
- Added xine-devel >= 1.1.9 as build requires

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-2.752228.1mdv2008.1
+ Revision: 137367
- New snapshot
- Clean %%doc

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fixed wrong excludes

* Thu Dec 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-2mdv2008.1
+ Revision: 119572
- Fix Kinfocenter file list

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-1mdv2008.1
+ Revision: 117068
- New Snapshot
  Kinfocenter is now on kdebase4 instead of kdebase4-runtime

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updating to official kdebase 3.97.0
    - kdebase 4 now contains only apps part from kde 4 kdebase. The other parts are in kdebase4 runtime and workspace

* Thu Dec 06 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.0-0.745416.1mdv2008.1
+ Revision: 115857
- KDE 4 Rc 2

* Sun Dec 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.743949.1mdv2008.1
+ Revision: 114413
- New Snapshot
  (Icons on the systray are now transparent )

* Thu Nov 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.743105.1mdv2008.1
+ Revision: 113985
- New snapshot

* Wed Nov 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.742711.1mdv2008.1
+ Revision: 113761
- New snapshot

* Mon Nov 26 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.741587.1mdv2008.1
+ Revision: 112014
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740034.1mdv2008.1
+ Revision: 111252
- New snapshot
  Add libkonquerorprivate package

* Fri Nov 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.737290.1mdv2008.1
+ Revision: 109015
- KDE 4 RC1

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734846.1mdv2008.1
+ Revision: 107491
- New snapshot ( say hello back to nepomuk )

* Thu Nov 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.1-0.731791.1mdv2008.1
+ Revision: 104759
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730896.1mdv2008.1
+ Revision: 103760
- Fix File list
- New snapshot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.729034.1mdv2008.1
+ Revision: 102035
- New snapshot

* Wed Oct 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.728613.1mdv2008.1
+ Revision: 101690
- Try to completly fix conflicts
- Fix File list
- New snapshot
- New svn snapshot
- Fix conflicts
- Fix conflicts
- Fix file list
- Remove icons as kicker is dead

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727635.1mdv2008.1
+ Revision: 100859
- New svn  snapshot

* Thu Oct 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.726654.2mdv2008.1
+ Revision: 100005
- Fix File list

* Thu Oct 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.726385.2mdv2008.1
+ Revision: 99968
+ rebuild (emptylog)

* Thu Oct 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.726385.1mdv2008.1
+ Revision: 99883
- Kde 4 Beta 3

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.93.0-0.726042.1mdv2008.1
+ Revision: 99520
- Fix File list
- New svn snapshot

* Thu Oct 04 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.4mdv2008.0
+ Revision: 95494
- Removing kcalc.svgz to avoid kicker crashes
- Bump release

* Thu Sep 27 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.3mdv2008.0
+ Revision: 93395
- Bumping release
- Fixing kmenu icon file
- Removing mdv2008.0 from Obsoletes tags.

* Thu Sep 20 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.2mdv2008.0
+ Revision: 91247
- Making Obsoletes tags versioned

* Mon Sep 17 2007 Anssi Hannula <anssi@mandriva.org> 1:3.93.0-0.712549.2mdv2008.0
+ Revision: 89315
- obsolete libkdebase46-devel instead of libkdebase4-devel (fixes #31484)

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.712549.1mdv2008.0
+ Revision: 85759
- Update with revision 712549
- Invalid source
- Update with revision 708844

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add missing conflicts

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.708282.1mdv2008.0
+ Revision: 79237
- Update with revision 708282
- Update with revision 708142

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.706306.1mdv2008.0
+ Revision: 75070
- Update with revision 706306

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.705487.2mdv2008.0
+ Revision: 72365
- Update with revision 705487
- Update with revision 704399
- Update with revision 702959
- Update to revision 700912

* Thu Aug 02 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.695685.1mdv2008.0
+ Revision: 58317
- Update for revision 695685
- Update for revision 695647

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92-0.693361.2mdv2008.0
+ Revision: 56445
- Update to revision 693361
- Disable klipper start for a while
- Using new simplified build
- Update for revision 690341

* Wed Jul 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.689200.2mdv2008.0
+ Revision: 53295
- Better add an svg image than a shell script...

* Wed Jul 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.689200.1mdv2008.0
+ Revision: 53162
- Fix soname now in kdebase
- Update with revision 689200
- Fixed file list
- Fix plasma wallpaper ( hope so )
- Update to revision 688743

* Mon Jul 16 2007 Olivier Blin <blino@mandriva.org> 1:3.91-0.686880.3mdv2008.0
+ Revision: 52444
- require xmessage in the workspace package, it is used in startkde

* Sat Jul 14 2007 Olivier Blin <blino@mandriva.org> 1:3.91-0.686880.2mdv2008.0
+ Revision: 51904
- require xprop and xset in the workspace package, they are used in startkde

* Thu Jul 12 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.686880.1mdv2008.0
+ Revision: 51575
- Fix Mandriva background wallpaper
- Update for revision 686880

* Wed Jul 11 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.686593.1mdv2008.0
+ Revision: 51431
- Update for match new kdelibs
- Update with revision 683926

* Wed Jul 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682706.1mdv2008.0
+ Revision: 47973
- Fix Conflicts
- New snapshot after monday BIC

* Tue Jul 03 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682449.1mdv2008.0
+ Revision: 47387
- Put them on the right place
- New snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix file list
    - Update from svn pos 3.91
    - New svn snapshot with more dolphin fixes
    - Update from svn

* Tue Jun 26 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.680516mdv2008.0
+ Revision: 44518
- Finally a working build of current svn. Kdesktop is about to die.
- Revision 680516
- Update for svn revision 678468

* Tue Jun 19 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.677668mdv2008.0
+ Revision: 41649
- Added nepomuk start/stop scripts on env/shutdown. Is not perfect yet but will help Sebastian to
  demonstrate nepomuk on akademy
- Updated to lates branch. Preview back to work

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Mon Jun 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.677187mdv2008.0
+ Revision: 41115
- Make dm session works. Previous startkde patch was broken
- Remove dups in file list
- Now we have some background :-)

* Sun Jun 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.676742mdv2008.0
+ Revision: 40552
- Added startup by command line. Just need type kde4
- Added env for running kde4 apps. Now just need type kde4env
- Fixed dm entry
- New svn update. Oxygen kwin avaiable

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.676117mdv2008.0
+ Revision: 40370
- New revision from svn
- New kdebase 4 package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix File list
    - New svn snapshot

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 1:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25645
- Update release
- new snapshot
- It's possible to compile with enable final

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.6mdv2008.0
+ Revision: 20514
- new snapshot
- new snapshot


* Sat Apr 07 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070406.6mdv2007.1
+ Revision: 150902
- new snapshot
- Update
- new snapshot
- Add buildrequires
  Cleanup
- new snapshot

* Thu Mar 01 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.3-0.20070228.6mdv2007.1
+ Revision: 130607
- Kate is moved into kdesdk
- Fix spec file
- Fix
- new snapshot
- 3.80.3
- fix spec file
- Forgot to commit it previously
- new snapshot
- new snapshot
- Fix spec file
- Bye bye mandrake-mime
- Not necessary for the moment
- Fix error
- new snapshot
- Add missing sources
- new snapshot
- Port Mandriva splashscreen to kde4

* Wed Jan 17 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.2mdv2007.1
+ Revision: 109760
- Update

* Tue Jan 09 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.1mdv2007.1
+ Revision: 106367
- Update
- Create session-plugins for allow to install kdm
  without kdebase
- Clean up
- Change name for session

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.1mdv2007.1
+ Revision: 103562
- Fix spec file
- Fix spec files
- new update
- Byebye menu

* Fri Dec 29 2006 Laurent Montel <lmontel@mandriva.com> 1:3.80-8mdv2007.1
+ Revision: 102493
- Add buildrequires
- fix conflict
- Import kdebase4

* Fri Dec 01 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-9mdv2007.0
- First package

