%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053349
%endif

Name: kdebase4
Summary: K Desktop Environment
Version: 4.4.2
Release: %mkrel 4
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar.bz2
%endif
Patch0: kdebase-4.0.84-fix-menu-entries.patch
Patch1: kdebase-4.2.98-mdvuserface.patch
Patch2: kdebase-4.2.95-Use-Mandriva-Home-Icon.patch
Patch3: kdebase-4.3.98-fix-execute-scripts.patch
Patch4: kdebase-folderview-icon-text.patch
Patch5: kdebase-4.4.1-configure-trashbin.patch
Patch6: kdebase-4.4.1-handle-emptytrash.patch
Patch7: kdebase-4.4.2-konsole-add-debug.patch
Patch8: kdebase-dolphin-icon-text.patch
Patch200: kdebase-4.4.1-t1100886-fix-konqueror-crash.patch
Patch300: kdebase-4.4.1-add-kcm-webcam.patch
BuildRequires: kdelibs4-devel >= 2:4.4.1-3
BuildRequires: kdebase4-workspace-devel >= 4.2.98
BuildRequires: kdepimlibs4-devel >= 4.2.98
BuildRequires: strigi-devel
BuildRequires: soprano-devel >= 2.0.98
BuildRequires: fontconfig-devel >= 2.1-9mdk
BuildRequires: pam-devel
BuildRequires: freetype2-devel
BuildRequires: libsasl-devel
BuildRequires: openldap-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: avahi-client-devel
BuildRequires: libsmbclient-devel > 3.0
BuildRequires: libieee1284-devel
BuildRequires: OpenEXR-devel
BuildRequires: hal-devel
BuildRequires: libusb-devel
BuildRequires: libxml2-utils
BuildRequires: X11-devel
BuildRequires: GL-devel
BuildRequires: bdftopcf
BuildRequires: imake
BuildRequires: libraw1394-devel
BuildRequires: libxklavier-devel
BuildRequires: lua-devel
BuildRequires: bluez-devel
BuildRequires: boost-devel
BuildRequires: xrdb
BuildRequires: qimageblitz-devel
BuildRequires: pciutils-devel
BuildRequires: webkitkde-devel
BuildRequires: opencv-devel
Requires: kdebase4-runtime
Requires: kappfinder
Requires: konsole
Requires: dolphin
Requires: kdepasswd
Requires: kde4-nsplugins
Requires: kwrite
Requires: konqueror
Requires: keditbookmarks
Requires: kfind
Requires: kdialog
Requires: kinfocenter
Requires: plasma-applet-folderview
Obsoletes: kdebase-servicemenu < 2007-9

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
%if %mdkversion >= 200910
Obsoletes: kdebase-konsole < 1:3.5.10-9
%endif
%if %mdkversion >= 200100
Obsoletes: kdebase3-konsole < 1:3.5.10-24
%endif

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
Conflicts: kdebase4-workspace < 1:3.93.0
Conflicts: kdebase4 < 1:4.1.0-4
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
%_kde_datadir/kde4/servicetypes/fileviewversioncontrolplugin.desktop
%_kde_datadir/config/servicemenu.knsrc
%_kde_datadir/config.kcfg/dolphin_*
%_kde_libdir/kde4/dolphinpart.so
%_kde_libdir/kde4/kcm_dolphingeneral.so
%_kde_libdir/kde4/kcm_dolphinnavigation.so
%_kde_libdir/kde4/kcm_dolphinservices.so
%_kde_libdir/kde4/kcm_dolphinviewmodes.so
%_kde_appsdir/dolphinpart/dolphinpart.rc
%_kde_appsdir/dolphin
%_kde_docdir/*/*/dolphin

#-----------------------------------------------------------------------------

%package -n kappfinder
Summary:    Utility to search and update the list of installed applications
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Obsoletes:  kde4-kappfinder < 1:4.0.68
Provides:   kde4-kappfinder = %epoch:%version
%if %mdkversion >= 200910
Conflicts:  kdemultimedia-common < 1:3.5.9-4
Conflicts:  kdebase-common < 1:3.5.9-38
Conflicts:  kdebase-progs < 1:3.5.9-38
%endif

%description -n kappfinder
Utility to search and update the list of installed applications

%files -n kappfinder
%defattr(-,root,root)
%_kde_bindir/kappfinder
%_kde_datadir/applications/kde4/kappfinder.desktop
%_kde_appsdir/kappfinder
%_kde_iconsdir/*/*/*/*
%_kde_mandir/man1/kappfinder.1.*
%exclude %_kde_iconsdir/*/*/*/konqueror.*
%exclude %_kde_iconsdir/*/*/*/kfind.*

#-----------------------------------------------------------------------------

%package -n kinfocenter
Summary:    Kinfocenter
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Provides:   kinfocenter4
Conflicts:  kdebase4-runtime < 1:4.0.68
Conflicts:  kdebase4-workspace < 1:4.0.2-1
Obsoletes: kde4-kinfocenter < 1:4.0.68
Provides: kde4-kinfocenter = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

%description -n kinfocenter
Kinfocenter is a utility in KDE that provides information
about a computer system.

%files -n kinfocenter
%defattr(-,root,root)
%_kde_bindir/kinfocenter
%_kde_libdir/libkdeinit4_kinfocenter.so
%dir %_kde_appsdir/kinfocenter
%_kde_appsdir/kinfocenter/*
%_kde_appsdir/kcmusb
%_kde_appsdir/kcmview1394
%_kde_libdir/kde4/kcm_info.so
%_kde_libdir/kde4/kcm_opengl.so
%_kde_libdir/kde4/kcm_solidproc.so
%_kde_libdir/kde4/kcm_nic.so
%_kde_libdir/kde4/kcm_usb.so
%_kde_libdir/kde4/kcm_view1394.so
%_kde_libdir/kde4/kcm_ioslaveinfo.so
%_kde_libdir/kde4/kcm_memory.so
%_kde_libdir/kde4/kcm_pci.so
%_kde_libdir/kde4/kcm_samba.so
%_kde_libdir/kde4/kcm_partition.so
%_kde_datadir/applications/kde4/kinfocenter.desktop
%_kde_docdir/*/*/kinfocenter
%_kde_datadir/kde4/services/devices.desktop
%_kde_datadir/kde4/services/dma.desktop
%_kde_datadir/kde4/services/interrupts.desktop
%_kde_datadir/kde4/services/ioports.desktop
%_kde_datadir/kde4/services/kcmusb.desktop
%_kde_datadir/kde4/services/kcmsolidproc.desktop
%_kde_datadir/kde4/services/kcmview1394.desktop
%_kde_datadir/kde4/services/nic.desktop
%_kde_datadir/kde4/services/opengl.desktop
%_kde_datadir/kde4/services/scsi.desktop
%_kde_datadir/kde4/services/sound.desktop
%_kde_datadir/kde4/services/xserver.desktop
%_kde_datadir/kde4/services/ioslaveinfo.desktop
%_kde_datadir/kde4/services/kcm_memory.desktop
%_kde_datadir/kde4/services/kcm_pci.desktop
%_kde_datadir/kde4/services/smbstatus.desktop
%_kde_datadir/kde4/services/kcm_partition.desktop

#-----------------------------------------------------------------------------

%package -n kdepasswd
Summary: Kdepasswd
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kdepasswd < 1:3.93.0-0.714129.2
Obsoletes: kde4-kdepasswd < 1:4.0.68
Provides: kde4-kdepasswd = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-kdm < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

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
Obsoletes: kdebase4-nsplugins < 1:3.93.0-0.714129.2
%if %mdkversion >= 200910
Obsoletes: kdebase-nsplugins < 1:3.5.10-8
%endif
%if %mdkversion >= 200100
Obsoletes: kdebase3-nsplugins < 1:3.5.10-24
%endif

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
Obsoletes: kdebase4-kwrite < 1:3.93.0-0.714129.2
Obsoletes: kde4-kwrite < 1:4.0.68
Provides: kde4-kwrite = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

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

#-----------------------------------------------------------------------------

%package -n konqueror
Summary:    KDE file and web browser
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Requires:   dolphin
Obsoletes:  kdebase4-konqueror < 1:3.93.0-0.714129.2
Obsoletes: kde4-konqueror < 1:4.0.68
Provides: kde4-konqueror = %epoch:%version
Conflicts: %{libkonq} <  1:4.0.82-5
Conflicts: kde4-nsplugins < 1:4.2.1
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif
Suggests:  keditbookmarks

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
%_kde_datadir/apps/kcontrol/*
%_kde_datadir/config.kcfg/konqueror*
%_kde_libdir/kde4/fileviewsvnplugin.so
%_kde_datadir/kde4/services/fileviewsvnplugin.desktop
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
%_kde_datadir/autostart/konqy_preload.desktop
%_kde_datadir/config/konqsidebartngrc
%_kde_datadir/kde4/services/cache.desktop
%_kde_datadir/kde4/services/cookies.desktop
%_kde_datadir/kde4/services/desktoppath.desktop
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
#%_kde_datadir/kde4/services/lanbrowser.desktop
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
%_kde_datadir/templates

#-----------------------------------------------------------------------------

%package -n keditbookmarks
Summary: Bookmark editor
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-keditbookmarks < 1:3.93.0-0.714129.2
Obsoletes: kde4-keditbookmarks < 1:4.0.68
Provides: kde4-keditbookmarks = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

%description -n keditbookmarks
Bookmark editor.

%files -n keditbookmarks
%defattr(-,root,root)
%_kde_bindir/kbookmarkmerger
%_kde_bindir/keditbookmarks
%_kde_libdir/libkdeinit4_keditbookmarks.so
%_kde_datadir/kde4/services/bookmarks.desktop
%_kde_appsdir/keditbookmarks
%_kde_datadir/config.kcfg/keditbook*
%_kde_mandir/man1/kbookmarkmerger.1.*

#-----------------------------------------------------------------------------

%package -n kfind
Summary: Application finder
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kfind < 1:3.93.0-0.714129.2
Obsoletes: kde4-kfind < 1:4.0.68
Provides: kde4-kfind = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-common < 1:3.5.9-38
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

%description -n kfind
Application finder

%files -n kfind
%defattr(-,root,root)
%_kde_bindir/kfind
%_kde_libdir/kde4/libkfindpart.so
%_kde_datadir/applications/kde4/kfind.desktop
%_kde_datadir/kde4/services/kfindpart.desktop
%_kde_datadir/kde4/servicetypes/findpart.desktop
%_kde_iconsdir/*/*/*/kfind.*
%_kde_mandir/man1/kfind.1.*
%_kde_docdir/*/*/kfind

#-----------------------------------------------------------------------------

%package -n kdialog
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kdialog < 1:3.93.0-0.714129.2
Obsoletes: kde4-kdialog < 1:4.0.68
Provides: kde4-kdialog = %epoch:%version
%if %mdkversion >= 200910
Conflicts: kdebase-progs < 1:3.5.9-38
%endif

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
Obsoletes: plasma-applets-folderview

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
Requires: kde4-macros
Requires: kdelibs4-devel >= 2:4.2.98
Requires: %libdolphinprivate = %epoch:%version
Requires: %libkonq = %epoch:%version
Requires: %libkonqsidebarplugin = %epoch:%version
Requires: %libkonquerorprivate = %epoch:%version
Requires: kdebase4-workspace-devel
Obsoletes: %{_lib}kdebase46-devel < 1:3.93.0-0.714129.2
Conflicts: kde4-kdialog < 1:4.0.68
Conflicts: kde4-konqueror < 1:4.0.68
Conflicts: kde4-nsplugins < 1:4.2.1
%if %mdkversion >= 200910
Conflicts: kdebase3-devel < 1:3.5.9-38
%endif

%description  devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so
%_kde_libdir/libkonq.so
%_kde_libdir/libkonqsidebarplugin.so
%_kde_libdir/libkonquerorprivate.so
%_kde_includedir/*.h
%_kde_datadir/dbus-1/interfaces/*

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdebase-%version%kde_snapshot
%else
%setup -q -n kdebase-%version
%endif

%patch0 -p0
%patch1 -p0 -b .userface
%patch2 -p0 -b .Mdv_Home_icon
%patch3 -p0
%patch4 -p0
%patch5 -p1
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch300 -p0

%build
%cmake_kde4

%make


%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

