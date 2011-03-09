%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdebase4
Summary: K Desktop Environment
Version: 4.6.1
%if %branch
Release: %mkrel -c %kde_snapshot 1
%else
Release: %mkrel 2
%endif
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar.bz2
%endif
Patch1: kdebase-4.2.98-mdvuserface.patch
Patch2: kdebase-4.2.95-Use-Mandriva-Home-Icon.patch
Patch3: kdebase-4.3.98-fix-execute-scripts.patch
Patch4: kdebase-folderview-icon-text.patch
Patch7: kdebase-4.4.2-konsole-add-debug.patch
#fwang: patch8,10 does not apply in kde 4.6
Patch8: kdebase-dolphin-icon-text.patch
Patch10: dolphin-annotationmenu.patch
#branch patches
#trunk patches
# test patches
BuildRequires: kdelibs4-devel >= 2:4.5.60
BuildRequires: strigi-devel
BuildRequires: zlib-devel
BuildRequires: qimageblitz-devel
BuildRequires: shared-desktop-ontologies-devel
BuildRequires: glib2-devel
BuildRequires: libxt-devel
Requires: kdebase4-runtime
Suggests: konsole
Suggests: dolphin
Suggests: kdepasswd
Suggests: kde4-nsplugins
Suggests: kwrite
Suggests: konqueror
Suggests: keditbookmarks
Suggests: kfind
Suggests: kdialog
Requires: plasma-applet-folderview

BuildRoot: %_tmppath/%name-%version-%release-root

%description
This meta package requires all base kdebase 4 packages.

%files
%doc README

#-----------------------------------------------------------------------------

%package -n konsole
Summary: A shell program similar to xterm for KDE
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: konsole4
Obsoletes: kdebase4-konsole < 1:3.93.0-0.714129.2
Obsoletes: kde4-konsole < 1:4.0.68
Provides: kde4-konsole = %epoch:%version
Requires: x11-font-misc-misc

%description -n konsole
A shell program similar to xterm for KDE

%files -n konsole
%defattr(-,root,root)
%_kde_bindir/konsole
%_kde_bindir/konsoleprofile
%_kde_libdir/kde4/libkonsolepart.so
%_kde_libdir/libkdeinit4_konsole.so
%_kde_libdir/libkonsoleprivate.so
%_kde_datadir/applications/kde4/konsole.desktop
%_kde_appsdir/konsole
%_kde_datadir/kde4/services/konsolepart.desktop
%_kde_datadir/kde4/servicetypes/terminalemulator.desktop
%_kde_datadir/kde4/services/ServiceMenus/konsolehere.desktop
%_kde_docdir/*/*/konsole

#------------------------------------------------

%define dolphinprivate_major 4
%define libdolphinprivate %mklibname dolphinprivate %dolphinprivate_major

%package -n %libdolphinprivate
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}dolphinprivate5 < 1:3.93.0-0.714129.2
Obsoletes: %{_lib}dolphinprivate1 < 1:4.0.83-6

%description -n %libdolphinprivate
KDE 4 core library.

%files -n %libdolphinprivate
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so.%{dolphinprivate_major}*

#-----------------------------------------------------------------------------

%package -n dolphin
Summary: File manager for KDE focusing on usability
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Requires: kfind
Provides: dolphin4
Suggests: ffmpegthumbs
Suggests:  kde-odf-thumbnail
Conflicts: kdebase4-workspace < 1:3.93.0
Conflicts: kdebase4 < 1:4.1.0-4
Conflicts: konqueror < 1:4.4.2-6 
Obsoletes: kde4-dolphin < 1:4.0.68
Provides: kde4-dolphin = %epoch:%version

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
%defattr(-,root,root)
%_kde_bindir/dolphin
%_kde_bindir/servicemenudeinstallation
%_kde_bindir/servicemenuinstallation
%_kde_datadir/applications/kde4/dolphin.desktop
%_kde_datadir/kde4/services/dolphinpart.desktop
%_kde_datadir/kde4/services/kcmdolphingeneral.desktop
%_kde_datadir/kde4/services/kcmdolphinnavigation.desktop
%_kde_datadir/kde4/services/kcmdolphinservices.desktop
%_kde_datadir/kde4/services/kcmdolphinviewmodes.desktop
%_kde_datadir/kde4/services/filenamesearch.protocol
%_kde_datadir/kde4/servicetypes/fileviewversioncontrolplugin.desktop
%_kde_datadir/config/servicemenu.knsrc
%_kde_datadir/config.kcfg/dolphin_*
%_kde_libdir/libkdeinit4_dolphin.so
%_kde_libdir/kde4/dolphinpart.so
%_kde_libdir/kde4/kcm_dolphingeneral.so
%_kde_libdir/kde4/kcm_dolphinnavigation.so
%_kde_libdir/kde4/kcm_dolphinservices.so
%_kde_libdir/kde4/kcm_dolphinviewmodes.so
%_kde_libdir/kde4/kio_filenamesearch.so
%_kde_appsdir/dolphinpart/dolphinpart.rc
%_kde_appsdir/dolphin
%_kde_datadir/templates
%_kde_docdir/*/*/dolphin

#-----------------------------------------------------------------------------

%package -n kdepasswd
Summary: Kdepasswd
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n kdepasswd
User password management

%files -n kdepasswd
%defattr(-,root,root)
%_kde_bindir/kdepasswd
%_kde_libdir/kde4/kcm_useraccount.so
%_kde_datadir/applications/kde4/kdepasswd.desktop
%_kde_datadir/kde4/services/kcm_useraccount.desktop
%_kde_datadir/config.kcfg/kcm_useracc*
%_kde_datadir/apps/kdm/*
%_kde_docdir/*/*/kdepasswd

#-----------------------------------------------------------------------------

%package -n kde4-nsplugins
Summary: Netscape plugins wrapper for kde
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n kde4-nsplugins
Netscape plugins wrapper for kde.

%files -n kde4-nsplugins
%defattr(-,root,root)
%_kde_bindir/nspluginscan
%_kde_bindir/nspluginviewer
%_kde_libdir/kde4/libkcminit_nsplugins.so
%_kde_libdir/kde4/libnsplugin.so
%_kde_appsdir/plugin
%_kde_datadir/kde4/services/khtml_plugins.desktop

#-----------------------------------------------------------------------------

%package -n kwrite
Summary: Simple text editor for KDE
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n kwrite
Simple text editor for KDE

%files -n kwrite
%defattr(-,root,root)
%_kde_bindir/kwrite
%_kde_libdir/libkdeinit4_kwrite.so
%_kde_datadir/applications/kde4/kwrite.desktop
%_kde_appsdir/kwrite
%_kde_docdir/*/*/kwrite

#------------------------------------------------

%define konq_major 5
%define libkonq %mklibname konq %konq_major

%package -n %libkonq
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: konqueror <  1:4.0.82-5

%description -n %libkonq
KDE 4 core library.

%files -n %libkonq
%defattr(-,root,root)
%_kde_libdir/libkonq.so.%{konq_major}*

#------------------------------------------------

%define konqsidebarplugin_major 4
%define libkonqsidebarplugin %mklibname konqsidebarplugin %konqsidebarplugin_major

%package -n %libkonqsidebarplugin
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}konqsidebarplugin5 < 1:3.93.0-0.714129.2
Obsoletes: %{_lib}kdebase46 <= 1:3.80.3

%description -n %libkonqsidebarplugin
KDE 4 core library.

%files -n %libkonqsidebarplugin
%defattr(-,root,root)
%_kde_libdir/libkonqsidebarplugin.so.%{konqsidebarplugin_major}*

#------------------------------------------------

%define konquerorprivate_major 4
%define libkonquerorprivate %mklibname konquerorprivate %konquerorprivate_major

%package -n %libkonquerorprivate
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}konquerorprivate1 < 1:4.0.83-6

%description -n %libkonquerorprivate
KDE 4 core library.

%files -n %libkonquerorprivate
%defattr(-,root,root)
%_kde_libdir/libkonquerorprivate.so.%{konquerorprivate_major}*


#------------------------------------------------

%define kbookmarkmodel_private_major 4
%define libkbookmarkmodel_private %mklibname kbookmarkmodel_private %kbookmarkmodel_private_major

%package -n %libkbookmarkmodel_private
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkbookmarkmodel_private
KDE 4 core library.

%files -n %libkbookmarkmodel_private
%defattr(-,root,root)
%_kde_libdir/libkbookmarkmodel_private.so.%{kbookmarkmodel_private_major}*

#------------------------------------------------

%package -n konqueror
Summary:    KDE file and web browser
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Requires:   dolphin
Suggests:   keditbookmarks
SUggests:   konq-plugins

%description -n konqueror
KDE file and web browser

%files -n konqueror
%defattr(-,root,root)
%_kde_bindir/kfmclient
%_kde_bindir/konqueror
%_kde_libdir/kde4/kded_konqy_preloader.so
%_kde_libdir/kde4/kcm_kio.so
%_kde_libdir/kde4/kcm_konq.so
%_kde_libdir/kde4/kcm_konqhtml.so
%_kde_libdir/kde4/kcm_kurifilt.so
%_kde_libdir/kde4/kcm_performance.so
%_kde_libdir/kde4/konq_aboutpage.so
%_kde_libdir/kde4/konq_shellcmdplugin.so
%_kde_libdir/kde4/konq_sidebar.so
%_kde_libdir/kde4/konq_sidebartree_dirtree.so
%_kde_libdir/kde4/konqsidebar_tree.so
%_kde_libdir/kde4/konqsidebar_web.so
%_kde_libdir/kde4/khtmlkttsdplugin.so
%_kde_libdir/libkdeinit4_kfmclient.so
%_kde_libdir/libkdeinit4_konqueror.so
%_kde_libdir/kde4/kcm_history.so
%_kde_libdir/kde4/kded_favicons.so
%_kde_libdir/kde4/konq_sound.so
%_kde_libdir/kde4/konq_sidebartree_bookmarks.so
%_kde_libdir/kde4/konqsidebar_history.so
%_kde_libdir/kde4/konqsidebar_places.so
%_kde_datadir/apps/kcontrol/*
%_kde_datadir/config.kcfg/konqueror*
%_kde_datadir/applications/kde4/Home.desktop
%_kde_datadir/applications/kde4/kfmclient.desktop
%_kde_datadir/applications/kde4/kfmclient_dir.desktop
%_kde_datadir/applications/kde4/kfmclient_html.desktop
%_kde_datadir/applications/kde4/kfmclient_war.desktop
%_kde_datadir/applications/kde4/konqbrowser.desktop
%_kde_datadir/applications/kde4/konquerorsu.desktop
%_kde_appsdir/kcmcss/template.css
%_kde_appsdir/kconf_update/kfmclient_3_2.upd
%_kde_appsdir/kconf_update/kfmclient_3_2_update.sh
%_kde_appsdir/khtml/kpartplugins/khtmlkttsd.desktop
%_kde_appsdir/khtml/kpartplugins/khtmlkttsd.rc
%_kde_appsdir/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%_kde_appsdir/dolphinpart/kpartplugins/kshellcmdplugin.rc
%_kde_appsdir/konqsidebartng
%_kde_appsdir/kbookmark/directory_bookmarkbar.desktop
%_kde_appsdir/kconf_update/favicons.upd
%_kde_appsdir/kconf_update/move_favicons.sh
%_kde_appsdir/kwebkitpart/kpartplugins/khtmlkttsd.desktop
%_kde_appsdir/kwebkitpart/kpartplugins/khtmlkttsd.rc
%_kde_datadir/autostart/konqy_preload.desktop
%_kde_datadir/config/konqsidebartngrc
%_kde_datadir/kde4/services/cache.desktop
%_kde_datadir/kde4/services/cookies.desktop
%_kde_datadir/kde4/services/ebrowsing.desktop
%_kde_datadir/kde4/services/filebehavior.desktop
%_kde_datadir/kde4/services/kcmkonqyperformance.desktop
%_kde_datadir/kde4/services/kcmperformance.desktop
%_kde_datadir/kde4/services/kded/konqy_preloader.desktop
%_kde_datadir/kde4/services/khtml_behavior.desktop
%_kde_datadir/kde4/services/khtml_filter.desktop
%_kde_datadir/kde4/services/khtml_general.desktop
%_kde_datadir/kde4/services/khtml_java_js.desktop
%_kde_datadir/kde4/services/konq_aboutpage.desktop
%_kde_datadir/kde4/services/konq_sidebartng.desktop
%_kde_datadir/kde4/services/konqueror.desktop
%_kde_datadir/kde4/services/netpref.desktop
%_kde_datadir/kde4/services/proxy.desktop
%_kde_datadir/kde4/services/smb.desktop
%_kde_datadir/kde4/services/useragent.desktop
%_kde_datadir/kde4/services/useragentstrings
%_kde_datadir/kde4/services/khtml_appearance.desktop
%_kde_datadir/kde4/services/kcmhistory.desktop
%_kde_datadir/kde4/servicetypes/konqaboutpage.desktop
%_kde_datadir/kde4/servicetypes/uasprovider.desktop
%_kde_datadir/kde4/servicetypes/konqdndpopupmenuplugin.desktop
%_kde_appsdir/konqueror
%_kde_iconsdir/*/*/*/konqueror.*
%_kde_docdir/*/*/konqueror
%_kde_datadir/kde4/services/kded/favicons.desktop
%_kde_datadir/kde4/servicetypes/konqpopupmenuplugin.desktop

#-----------------------------------------------------------------------------

%package -n keditbookmarks
Summary: Bookmark editor
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n keditbookmarks
Bookmark editor.

%files -n keditbookmarks
%defattr(-,root,root)
%_kde_bindir/kbookmarkmerger
%_kde_bindir/keditbookmarks
%_kde_libdir/libkdeinit4_keditbookmarks.so
%_kde_datadir/applications/kde4/keditbookmarks.desktop
%_kde_datadir/kde4/services/bookmarks.desktop
%_kde_appsdir/keditbookmarks
%_kde_datadir/config.kcfg/keditbook*
%_kde_mandir/man1/kbookmarkmerger.1.*

#-----------------------------------------------------------------------------

%package -n kfind
Summary: Application finder
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n kfind
Application finder

%files -n kfind
%defattr(-,root,root)
%_kde_bindir/kfind
%_kde_datadir/applications/kde4/kfind.desktop
%_kde_iconsdir/*/*/*/kfind.*
%_kde_mandir/man1/kfind.1.*
%_kde_docdir/*/*/kfind

#-----------------------------------------------------------------------------

%package -n kdialog
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: kdebase4-runtime

%description -n kdialog
Dialog KDE base widgets

%files -n kdialog
%defattr(-,root,root)
%_kde_bindir/kdialog

#-----------------------------------------------------------------------------

%package -n plasma-applet-folderview
Summary: Display the content of folders (Desktop as default)
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-applet

%description -n plasma-applet-folderview
Display the content of folders (Desktop as default)

%files -n plasma-applet-folderview
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_folderview.so
%_kde_datadir/kde4/services/plasma-applet-folderview.desktop

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdebase 4
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:4.5.60
Requires: %libdolphinprivate = %epoch:%version
Requires: %libkonq = %epoch:%version
Requires: %libkonqsidebarplugin = %epoch:%version
Requires: %libkbookmarkmodel_private = %epoch:%version

%description  devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so
%_kde_libdir/libkonq.so
%_kde_libdir/libkonqsidebarplugin.so
%_kde_libdir/libkbookmarkmodel_private.so
%_kde_includedir/*.h
%_kde_datadir/dbus-1/interfaces/*

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdebase-%version%kde_snapshot
%else
%setup -q -n kdebase-%version
%endif

%patch1 -p0 -b .mdvuserface
%patch2 -p0 -b .mdvicon
%patch3 -p0 -b .execute-scripts
#%patch4 -p0 -b .folderview
%patch7 -p0 -b .konsoledebug

%build
%cmake_kde4

%make


%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

