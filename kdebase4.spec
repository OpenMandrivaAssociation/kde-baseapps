%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 752228

Name: kdebase4
Summary: K Desktop Environment
Version: 3.97.1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Release: %mkrel 2.%revision.1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.%revision.tar.bz2
%else
Release: %mkrel 2
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar.bz2
%endif
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: strigi-devel
BuildRequires: soprano-devel
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
BuildRequires: resmgr-devel
BuildRequires: libnetworkmanager-util-devel
BuildRequires: networkmanager-devel
BuildRequires: bluez-devel
BuildRequires: boost-devel
BuildRequires: xrdb
BuildRequires: qimageblitz-devel
Requires: kdebase4-runtime
Requires: kde4-kappfinder
Requires: kde4-konsole
Requires: kde4-dolphin
Requires: kde4-kdepasswd
Requires: kde4-nsplugins
Requires: kde4-kwrite
Requires: kde4-konqueror
Requires: kde4-keditbookmarks
Requires: kde4-kfind
Requires: kde4-kdialog
Requires: kde4-kinfocenter
Requires: phonon-xine

%description
This meta package requires all base kdebase 4 packages.

%files
%doc README

#-----------------------------------------------------------------------------

%package -n kde4-konsole
Summary: Konsole
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: konsole4
Obsoletes: kdebase4-konsole < 1:3.93.0-0.714129.2

%description -n kde4-konsole
A shell program similar to xterm for KDE

%files -n kde4-konsole
%defattr(-,root,root)
%_kde_bindir/konsole
%_kde_bindir/konsoleprofile
%_kde_libdir/kde4/kded_kwrited.so
%_kde_libdir/kde4/libkonsolepart.so
%_kde_libdir/libkdeinit4_konsole.so
%_kde_datadir/applications/kde4/konsole.desktop
%_kde_datadir/applications/kde4/quick-access-konsole.desktop
%_kde_appsdir/konsole
%_kde_datadir/kde4/services/kded/kwrited.desktop
%_kde_datadir/kde4/services/konsole-script.desktop
%_kde_datadir/kde4/services/konsolepart.desktop
%_kde_datadir/kde4/servicetypes/terminalemulator.desktop
%_kde_datadir/kde4/services/ServiceMenus/konsolehere.desktop
%_kde_iconsdir/*/*/*/konsole.*
%dir %_kde_docdir/HTML/en/konsole
%doc %_kde_docdir/HTML/en/konsole/index.cache.bz2
%doc %_kde_docdir/HTML/en/konsole/index.docbook
%doc %_kde_docdir/HTML/en/konsole/*.png

#------------------------------------------------	

%define libdolphinprivate %mklibname dolphinprivate 1

%package -n %libdolphinprivate
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}dolphinprivate5 < 1:3.93.0-0.714129.2

%description -n %libdolphinprivate
KDE 4 core library.

%post -n %libdolphinprivate -p /sbin/ldconfig
%postun -n %libdolphinprivate -p /sbin/ldconfig

%files -n %libdolphinprivate
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so.*

#-----------------------------------------------------------------------------

%package -n kde4-dolphin
Summary: dolphin
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: dolphin4
Conflicts: kdebase4-workspace < 1:3.93.0

%description -n kde4-dolphin
A shell program similar to xterm for KDE

%files -n kde4-dolphin
%defattr(-,root,root)
%_kde_bindir/dolphin
%_kde_datadir/applications/kde4/dolphin.desktop
%_kde_datadir/kde4/services/dolphinpart.desktop
%_kde_datadir/config.kcfg/dolphin_*
%_kde_libdir/kde4/dolphinpart.so
%_kde_appsdir/dolphinpart/dolphinpart.rc
%_kde_appsdir/dolphin

%dir %_kde_docdir/HTML/en/dolphin
%doc %_kde_docdir/HTML/en/dolphin/index.cache.bz2
%doc %_kde_docdir/HTML/en/dolphin/index.docbook
%doc %_kde_docdir/HTML/en/dolphin/*.png

#-----------------------------------------------------------------------------

%package -n kde4-kappfinder
Summary: kappfinder
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: kappfinder4

%description -n kde4-kappfinder
A shell program similar to xterm for KDE

%files -n kde4-kappfinder
%defattr(-,root,root)
%_kde_bindir/kappfinder
%_kde_datadir/applications/kde4/kappfinder.desktop
%_kde_appsdir/kappfinder
%_kde_iconsdir/*/*/*/*
%exclude %_kde_iconsdir/*/*/*/konqueror.*
%exclude %_kde_iconsdir/*/*/*/konsole.*
%exclude %_kde_iconsdir/*/*/*/kfind.*

#-----------------------------------------------------------------------------

%package -n kde4-kinfocenter
Summary:    kinfocenter
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Provides:   kinfocenter4
Conflicts:  kdebase4-runtime < 3.97.1

%description -n kde4-kinfocenter
Kinfocenter is a utility in KDE that provides information 
about a computer system.

%files -n kde4-kinfocenter
%defattr(-,root,root)
%_kde_bindir/kinfocenter
%_kde_libdir/libkdeinit4_kinfocenter.so
%dir %_kde_appsdir/kinfocenter
%dir %_kde_appsdir/kinfocenter/about
%_kde_appsdir/kinfocenter/about/kinfocenter.css
%_kde_appsdir/kinfocenter/about/main.html
%_kde_appsdir/kinfocenter/about/top-right-kinfocenter.png
%_kde_appsdir/kinfocenter/kinfocenterui.rc
%_kde_datadir/kde4/services/kinfocenter.desktop

#-----------------------------------------------------------------------------

%package -n kde4-kdepasswd
Summary: kdepasswd
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kdepasswd < 1:3.93.0-0.714129.2

%description -n kde4-kdepasswd
User password management

%files -n kde4-kdepasswd
%defattr(-,root,root)
%_kde_bindir/kdepasswd
%_kde_libdir/kde4/kcm_useraccount.so
%_kde_datadir/applications/kde4/kdepasswd.desktop
%_kde_datadir/kde4/services/kcm_useraccount.desktop
%_kde_datadir/config.kcfg/kcm_useracc*
%_kde_datadir/apps/kdm/*

#-----------------------------------------------------------------------------

%package -n kde4-nsplugins
Summary: Netscape plugins wrapper for kde
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-nsplugins < 1:3.93.0-0.714129.2

%description -n kde4-nsplugins
Netscape plugins wrapper for kde.

%files -n kde4-nsplugins
%defattr(-,root,root)
%_kde_bindir/nspluginscan
%_kde_bindir/nspluginviewer
%_kde_libdir/kde4/libkcminit_nsplugins.so
%_kde_libdir/kde4/libnsplugin.so
%_kde_appsdir/plugin/nspluginpart.rc
%_kde_datadir/kde4/services/khtml_plugins.desktop
%_datadir/dbus-1/interfaces/org.kde.nsplug*

#-----------------------------------------------------------------------------

%package -n kde4-kwrite
Summary: kwrite
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kwrite < 1:3.93.0-0.714129.2

%description -n kde4-kwrite
User password management

%files -n kde4-kwrite
%defattr(-,root,root)
%_kde_bindir/kwrite
%_kde_libdir/libkdeinit4_kwrite.so
%_kde_datadir/applications/kde4/kwrite.desktop
%_kde_appsdir/kwrite

%dir %_kde_docdir/HTML/en/kwrite
%doc %_kde_docdir/HTML/en/kwrite/index.cache.bz2
%doc %_kde_docdir/HTML/en/kwrite/index.docbook

#------------------------------------------------	

%define libkonq %mklibname konq 5

%package -n %libkonq
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkonq
KDE 4 core library.

%post -n %libkonq -p /sbin/ldconfig
%postun -n %libkonq -p /sbin/ldconfig

%files -n %libkonq
%defattr(-,root,root)
%_kde_libdir/kde4/kded_favicons.so
%_kde_libdir/kde4/konq_sound.so
%_kde_libdir/libkonq.so.*
%_kde_appsdir/kbookmark/directory_bookmarkbar.desktop
%_kde_appsdir/kconf_update/favicons.upd
%_kde_appsdir/kconf_update/move_favicons.sh
%_kde_datadir/kde4/services/kded/favicons.desktop
%_kde_datadir/kde4/servicetypes/konqpopupmenuplugin.desktop
%_kde_datadir/templates
%_datadir/dbus-1/interfaces/org.kde.libkonq*

#------------------------------------------------	

%define libkonqsidebarplugin %mklibname konqsidebarplugin 4

%package -n %libkonqsidebarplugin
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}konqsidebarplugin5 < 1:3.93.0-0.714129.2
Obsoletes: %{_lib}kdebase46 <= 1:3.80.3

%description -n %libkonqsidebarplugin
KDE 4 core library.

%post -n %libkonqsidebarplugin -p /sbin/ldconfig
%postun -n %libkonqsidebarplugin -p /sbin/ldconfig

%files -n %libkonqsidebarplugin
%defattr(-,root,root)
%_kde_libdir/libkonqsidebarplugin.so.*

#------------------------------------------------

%define libkonquerorprivate %mklibname konquerorprivate 1

%package -n %libkonquerorprivate
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkonquerorprivate
KDE 4 core library.

%post -n %libkonquerorprivate -p /sbin/ldconfig
%postun -n %libkonquerorprivate -p /sbin/ldconfig

%files -n %libkonquerorprivate
%defattr(-,root,root)
%_kde_libdir/libkonquerorprivate.so.*

#-----------------------------------------------------------------------------

%package -n kde4-konqueror
Summary:    konqueror
Group:      Graphical desktop/KDE
Requires:   kdebase4-runtime
Obsoletes:  kdebase4-konqueror < 1:3.93.0-0.714129.2
Conflicts:  kdebase4-workspace < 3.91
%description -n kde4-konqueror
KDE Browser

%files -n kde4-konqueror
%defattr(-,root,root)
%_kde_bindir/keditfiletype
%_kde_bindir/kfmclient
%_kde_bindir/konqueror
%_kde_libdir/kde4/kded_konqy_preloader.so
%_kde_libdir/kde4/kcm_css.so
%_kde_libdir/kde4/kcm_filetypes.so
%_kde_libdir/kde4/kcm_history.so
%_kde_libdir/kde4/kcm_kio.so
%_kde_libdir/kde4/kcm_konq.so
%_kde_libdir/kde4/kcm_konqhtml.so
%_kde_libdir/kde4/kcm_kurifilt.so
%_kde_libdir/kde4/kcm_performance.so
%_kde_libdir/kde4/konq_aboutpage.so
%_kde_libdir/kde4/konq_remoteencoding.so
%_kde_libdir/kde4/konq_shellcmdplugin.so
%_kde_libdir/kde4/konq_sidebar.so
%_kde_libdir/kde4/konq_sidebartree_bookmarks.so
%_kde_libdir/kde4/konq_sidebartree_dirtree.so
%_kde_libdir/kde4/konq_sidebartree_history.so
%_kde_libdir/kde4/konqsidebar_tree.so
%_kde_libdir/kde4/konqsidebar_web.so
%_kde_libdir/kde4/libkhtmlkttsdplugin.so
%_kde_libdir/libkdeinit4_kfmclient.so
%_kde_libdir/libkdeinit4_konqueror.so
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
%_kde_appsdir/kconf_update/konqsidebartng.upd
%_kde_appsdir/kconf_update/move_konqsidebartng_entries.sh
%_kde_appsdir/kconf_update/socks.upd
%_kde_appsdir/khtml/kpartplugins/khtmlkttsd.desktop
%_kde_appsdir/khtml/kpartplugins/khtmlkttsd.rc
%_kde_appsdir/konqiconview/kpartplugins/kremoteencodingplugin.desktop
%_kde_appsdir/konqiconview/kpartplugins/kremoteencodingplugin.rc
%_kde_appsdir/konqiconview/kpartplugins/kshellcmdplugin.desktop
%_kde_appsdir/konqiconview/kpartplugins/kshellcmdplugin.rc
%_kde_appsdir/konqlistview/kpartplugins/kremoteencodingplugin.desktop
%_kde_appsdir/konqlistview/kpartplugins/kremoteencodingplugin.rc
%_kde_appsdir/konqlistview/kpartplugins/kshellcmdplugin.desktop
%_kde_appsdir/konqlistview/kpartplugins/kshellcmdplugin.rc
%_kde_appsdir/konqsidebartng
%_kde_datadir/autostart/konqy_preload.desktop
%_kde_datadir/config/konqsidebartng.rc
%_kde_datadir/kde4/services/cache.desktop
%_kde_datadir/kde4/services/cookies.desktop
%_kde_datadir/kde4/services/desktoppath.desktop
%_kde_datadir/kde4/services/ebrowsing.desktop
%_kde_datadir/kde4/services/filebehavior.desktop
%_kde_datadir/kde4/services/filebrowser.desktop
%_kde_datadir/kde4/services/filepreviews.desktop
%_kde_datadir/kde4/services/filetypes.desktop
%_kde_datadir/kde4/services/kcmcss.desktop
%_kde_datadir/kde4/services/kcmhistory.desktop
%_kde_datadir/kde4/services/kcmkonqyperformance.desktop
%_kde_datadir/kde4/services/kcmperformance.desktop
%_kde_datadir/kde4/services/kded/konqy_preloader.desktop
%_kde_datadir/kde4/services/khtml_behavior.desktop
%_kde_datadir/kde4/services/khtml_filter.desktop
%_kde_datadir/kde4/services/khtml_general.desktop
%_kde_datadir/kde4/services/khtml_java_js.desktop
%_kde_datadir/kde4/services/konq_aboutpage.desktop
%_kde_datadir/kde4/services/konq_sidebartng.desktop
%_kde_datadir/kde4/services/konqfilemgr.desktop
%_kde_datadir/kde4/services/konqueror.desktop
%_kde_datadir/kde4/services/lanbrowser.desktop
%_kde_datadir/kde4/services/netpref.desktop
%_kde_datadir/kde4/services/proxy.desktop
%_kde_datadir/kde4/services/smb.desktop
%_kde_datadir/kde4/services/useragent.desktop
%_kde_datadir/kde4/services/useragentstrings
%_kde_datadir/kde4/servicetypes/konqaboutpage.desktop
%_kde_datadir/kde4/servicetypes/uasprovider.desktop
%_kde_datadir/kde4/services/khtml_fonts.desktop
%_kde_appsdir/konqueror
%_datadir/dbus-1/interfaces/org.kde.Konq*
%_datadir/dbus-1/interfaces/org.kde.konq*
%_datadir/dbus-1/interfaces/org.kde.FavIcon*
%_kde_iconsdir/*/*/*/konqueror.*

%dir %_kde_docdir/HTML/en/konqueror
%doc %_kde_docdir/HTML/en/konqueror/*.png
%doc %_kde_docdir/HTML/en/konqueror/*.docbook
%doc %_kde_docdir/HTML/en/konqueror/*.bz2

#-----------------------------------------------------------------------------

%package -n kde4-keditbookmarks
Summary: Bookmark editor
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-keditbookmarks < 1:3.93.0-0.714129.2

%description -n kde4-keditbookmarks
Bookmar editor

%files -n kde4-keditbookmarks
%defattr(-,root,root)
%_kde_bindir/kbookmarkmerger
%_kde_bindir/keditbookmarks
%_kde_libdir/libkdeinit4_keditbookmarks.so
%_kde_appsdir/keditbookmarks
%_kde_datadir/config.kcfg/keditbook*

#-----------------------------------------------------------------------------

%package -n kde4-kfind
Summary: Application finder
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kfind < 1:3.93.0-0.714129.2

%description -n kde4-kfind
Application finder

%files -n kde4-kfind
%defattr(-,root,root)
%_kde_bindir/kfind
%_kde_libdir/kde4/libkfindpart.so
%_kde_datadir/applications/kde4/kfind.desktop
%_kde_datadir/kde4/services/kfindpart.desktop
%_kde_datadir/kde4/servicetypes/findpart.desktop
%_kde_iconsdir/*/*/*/kfind.*

%dir %_kde_docdir/HTML/en/kfind
%doc %_kde_docdir/HTML/en/kfind/index.cache.bz2
%doc %_kde_docdir/HTML/en/kfind/*.docbook

#-----------------------------------------------------------------------------

%package -n kde4-kdialog
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kdialog < 1:3.93.0-0.714129.2

%description -n kde4-kdialog
Dialog KDE base widgets

%files -n kde4-kdialog
%defattr(-,root,root)
%_kde_bindir/kdialog
%_datadir/dbus-1/interfaces/org.kde.kdialog*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdebase 4
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libdolphinprivate = %epoch:%version
Requires: %libkonq = %epoch:%version
Requires: %libkonqsidebarplugin = %epoch:%version
Requires: %libkonquerorprivate = %epoch:%version
Obsoletes: %{_lib}kdebase46-devel < 1:3.93.0-0.714129.2

%description  devel
This package contains header files needed if you wish to build applications based on kdebase.

%files devel
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so
%_kde_libdir/libkonq.so
%_kde_libdir/libkonqsidebarplugin.so
%_kde_libdir/libkonquerorprivate.so
%_kde_includedir/*.h

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdebase-%version

%build
%cmake_kde4 

%make 


%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# kcalc.svgz crashes kicker
rm -rf %buildroot/%_kde_iconsdir/oxygen/scalable/apps/small/16x16/kcalc.svgz

%clean
rm -fr %buildroot

