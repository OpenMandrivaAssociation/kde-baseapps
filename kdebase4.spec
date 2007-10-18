%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 726385

Name: kdebase4
Summary: K Desktop Environment
Version: 3.94.0
Release: %mkrel 0.%revision.1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.%revision.tar.bz2
%else
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar.bz2
%endif
BuildConflicts: lm_utils
BuildConflicts: lm_utils-devel
BuildConflicts: liblm_sensors1
BuildConflicts: liblm_sensors1-devel
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
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
Requires: kde4-kdeprintfax
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
Requires: phonon-xine
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Meta package that requires all base kdebase 4 files

%files
%doc README

#--------------------------------------------------------------

%package -n oxygen-icon-theme
Group: Graphical desktop/KDE
Summary: Oxygen icon theme
Provides: kde4-icon-theme
Obsoletes: kdelibs4-common >= 30000000:3.80.3

%description -n oxygen-icon-theme
Oxygen KDE 4 icon theme. Complains with FreeDesktop.org naming schema

%files -n oxygen-icon-theme
%defattr(-,root,root,-)
%dir %_kde_iconsdir/oxygen
%_kde_iconsdir/*/index.theme
%_kde_iconsdir/*/*/*/*
%_kde_datadir/emoticons/*

#-----------------------------------------------------------------------------

%package runtime
Summary: KDE 4 application runtime components
Group: Graphical desktop/KDE
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Obsoletes: kdebase4-progs < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-core  < 1:3.93.0-0.714129.2
Obsoletes: kdebase4-common <= 1:3.80.3
Conflicts: kdebase4-workspace < 1:3.93.0 

%description runtime
KDE 4 application runtime components.

%files runtime
%defattr(-,root,root)
%_datadir/dbus-1/services/*
%_kde_prefix/env/nepomuk.sh
%_kde_appsdir/drkonqi
%_kde_appsdir/kcm_componentchooser
%_kde_appsdir/kcmlocale
%_kde_appsdir/kde
%_kde_appsdir/kdeprint
%_kde_appsdir/kdeprint_part
%_kde_appsdir/kinfocenter
%_kde_appsdir/kcontrol
%_kde_appsdir/kio_finger/kio_finger.css
%_kde_appsdir/kio_finger/kio_finger.pl
%_kde_appsdir/kio_info/kde-info2html
%_kde_appsdir/kio_info/kde-info2html.conf
%_kde_appsdir/kio_man/kio_man.css
%_kde_appsdir/kjobviewer
#%_kde_appsdir/konqueror/servicemenus/media_*
%_kde_bindir/kuiserver
%_kde_appsdir/kuiserver
%_kde_datadir/kde4/services/kuiserver.desktop
%_kde_libdir/libkdeinit4_kuiserver.so
%_kde_appsdir/Settingsmenu
%_kde_libdir/kde4/kstyle_*
%_kde_appsdir/kstyle
%_kde_libdir/kde4/plugins/styles
%_kde_datadir/kde4/services/kded/soliduiserver.desktop
%_kde_libdir/kde4/kded_soliduiserver.so
%_kde_datadir/apps/kdm
%_kde_datadir/kde4/services/khtml_fonts.desktop
%_kde_libdir/kde4/libexec/kioexec
%_kde_bindir/drkonqi
%_kde_bindir/ksvgtopng
%_kde_bindir/imagetops
%_kde_bindir/kcmshell4
%_kde_bindir/kde4-menu
%_kde_bindir/kdebugdialog
%_kde_bindir/kde-cp
%_kde_bindir/kdeeject
%_kde_bindir/kde-mv
%_kde_bindir/kde-open
%_kde_bindir/kdesu
%_kde_bindir/kdesud
%_kde_bindir/kfile4
%_kde_bindir/khc_docbookdig.pl
%_kde_bindir/khc_htdig.pl
%_kde_bindir/khc_htsearch.pl
%_kde_bindir/khc_indexbuilder
%_kde_bindir/khc_mansearch.pl
%_kde_bindir/khotnewstuff4
%_kde_bindir/kinfocenter
#%_kde_bindir/kinstalltheme
%_kde_bindir/kioclient
#%_kde_bindir/kio_media_mounthelper
%_kde_bindir/kjobviewer
%_kde_bindir/klocaldomainurifilterhelper
%_kde_bindir/kmimetypefinder
%_kde_bindir/knetattach
%_kde_datadir/applications/kde4/knetattach.desktop
%_kde_docdir/*/*/knetattach
%_kde_bindir/knotify4
%_kde_bindir/kprinter
%_kde_bindir/kquitapp
%_kde_bindir/kreadconfig
%_kde_bindir/kstart
%_kde_bindir/ktraderclient
%_kde_bindir/ktrash
%_kde_bindir/kwriteconfig
%_kde_configdir/xdg/menus/kde-information.menu
%_kde_configdir/xdg/menus/kde-kcontrol.menu
%_kde_configdir/xdg/menus/kde-settings.menu
%_kde_datadir/applications/kde4/Help.desktop
%_kde_datadir/applications/kde4/kjobviewer.desktop
%_kde_datadir/config/khotnewstuffrc
%_kde_datadir/config/kshorturifilterrc
%_kde_datadir/desktop-directories
%_kde_datadir/kde4/services/about.protocol
%_kde_datadir/kde4/services/applications.protocol
%_kde_datadir/kde4/services/ar.protocol
%_kde_datadir/kde4/services/bzip2.protocol
%_kde_datadir/kde4/services/bzip.protocol
%_kde_datadir/kde4/services/cgi.protocol
%_kde_datadir/kde4/services/componentchooser.desktop
%_kde_datadir/kde4/services/cursorthumbnail.desktop
%_kde_datadir/kde4/services/djvuthumbnail.desktop
%_kde_datadir/kde4/services/exrthumbnail.desktop
%_kde_datadir/kde4/services/finger.protocol
%_kde_datadir/kde4/services/fish.protocol
%_kde_datadir/kde4/services/fixhosturifilter.desktop
%_kde_datadir/kde4/services/floppy.protocol
%_kde_datadir/kde4/services/gzip.protocol
%_kde_datadir/kde4/services/htmlthumbnail.desktop
%_kde_datadir/kde4/services/icons.desktop
%_kde_datadir/kde4/services/imagethumbnail.desktop
%_kde_datadir/kde4/services/info.protocol
%_kde_datadir/kde4/services/kcmcgi.desktop
%_kde_datadir/kde4/services/kcmkded.desktop
%_kde_datadir/kde4/services/kcm_kdnssd.desktop
%_kde_datadir/kde4/services/kcmnotify.desktop
%_kde_datadir/kde4/services/kded/ktimezoned.desktop
#%_kde_datadir/kde4/services/kded/mediamanager.desktop
#%_kde_datadir/kde4/services/kded/medianotifier.desktop
%_kde_datadir/kde4/services/kded/remotedirnotify.desktop
%_kde_datadir/kde4/services/kdeprint_part.desktop
%_kde_datadir/kde4/services/kinfocenter.desktop
%_kde_datadir/kde4/services/kmanpart.desktop
%_kde_datadir/kde4/services/knotify4.desktop
%_kde_datadir/kde4/services/kshorturifilter.desktop
%_kde_datadir/kde4/services/kuriikwsfilter.desktop
%_kde_datadir/kde4/services/kurisearchfilter.desktop
%_kde_datadir/kde4/services/language.desktop
%_kde_datadir/kde4/services/localdomainurifilter.desktop
%_kde_datadir/kde4/services/man.protocol
#%_kde_datadir/kde4/services/media.desktop
#%_kde_datadir/kde4/services/media.protocol
%_kde_datadir/kde4/services/nfs.protocol
%_kde_datadir/kde4/services/printdb.protocol
%_kde_datadir/kde4/services/printers.desktop
%_kde_datadir/kde4/services/print.protocol
%_kde_datadir/kde4/services/programs.protocol
%_kde_datadir/kde4/services/remote.protocol
%_kde_datadir/kde4/services/searchproviders
%_kde_datadir/kde4/services/settings.protocol
%_kde_datadir/kde4/services/smbstatus.desktop
%_kde_datadir/kde4/services/smb.protocol
%_kde_appsdir/remoteview/smb-network.desktop
%_kde_libdir/kde4/kio_smb.so
%_kde_datadir/kde4/services/svgthumbnail.desktop
%_kde_datadir/kde4/services/tar.protocol
%_kde_datadir/kde4/services/textthumbnail.desktop
%_kde_datadir/kde4/services/thumbnail.protocol
%_kde_datadir/kde4/services/trash.protocol
%_kde_datadir/kde4/services/zip.protocol
%_kde_datadir/kde4/servicetypes/searchprovider.desktop
%_kde_datadir/kde4/servicetypes/thumbcreator.desktop
%_kde_datadir/locale/l10n/*/*
%_kde_datadir/locale/l10n/*.desktop
%_kde_datadir/locale/en_US
%_kde_datadir/sounds
%_kde_libdir/kde4/cursorthumbnail.so
%_kde_libdir/kde4/djvuthumbnail.so
%_kde_libdir/kde4/exrthumbnail.so
%_kde_libdir/kde4/htmlthumbnail.so
%_kde_libdir/kde4/imagethumbnail.so
%_kde_libdir/kde4/kcm_cgi.so
%_kde_libdir/kde4/kcm_componentchooser.so
%_kde_libdir/kde4/kcm_icons.so
%_kde_libdir/kde4/kcm_kded.so
%_kde_libdir/kde4/kcm_kdnssd.so
%_kde_libdir/kde4/kcm_knotify.so
%_kde_libdir/kde4/kcm_locale.so
#%_kde_libdir/kde4/kcm_media.so
%_kde_libdir/kde4/kcm_printmgr.so
%_kde_libdir/kde4/kcm_samba.so
%_kde_libdir/kde4/kded_kpasswdserver.so
%_kde_libdir/kde4/kded_ktimezoned.so
#%_kde_libdir/kde4/kded_mediamanager.so
#%_kde_libdir/kde4/kded_medianotifier.so
%_kde_libdir/kde4/librenaudioplugin.so
%_kde_libdir/kde4/librenimageplugin.so
%_kde_libdir/kde4/kded_remotedirnotify.so
%_kde_libdir/kde4/kio_sftp.so
%_kde_datadir/kde4/services/sftp* 
%_kde_libdir/kde4/kio_about.so
%_kde_libdir/kde4/kio_cgi.so
%_kde_libdir/kde4/kio_filter.so
%_kde_libdir/kde4/kio_finger.so
%_kde_libdir/kde4/kio_fish.so
%_kde_libdir/kde4/kio_floppy.so
%_kde_libdir/kde4/kio_info.so
%_kde_libdir/kde4/kio_man.so
#%_kde_libdir/kde4/kio_media.so
%_kde_libdir/kde4/kio_nfs.so
%_kde_libdir/kde4/kio_print.so
%_kde_libdir/kde4/kio_remote.so
%_kde_libdir/kde4/kio_settings.so
#%_kde_libdir/kde4/kio_tar.so
%_kde_libdir/kde4/kcm_ioslaveinfo.so
%_kde_libdir/kde4/kio_archive.so
%_kde_libdir/kde4/kio_thumbnail.so
%_kde_libdir/kde4/kio_trash.so
%_kde_libdir/kde4/libfixhosturifilter.so
%_kde_libdir/kde4/libkdeprint_part.so
%_kde_libdir/kde4/libkmanpart.so
%_kde_libdir/kde4/libkshorturifilter.so
%_kde_libdir/kde4/libkuriikwsfilter.so
%_kde_libdir/kde4/libkurisearchfilter.so
%_kde_libdir/kde4/liblocaldomainurifilter.so
%_kde_libdir/kde4/svgthumbnail.so
%_kde_libdir/kde4/textthumbnail.so
#%_kde_bindir/nepomukcoreservices
#%_kde_bindir/nepomukdaemon
#%_kde_datadir/kde4/services/nepomuk/nepomuk-coreservices.desktop
%_kde_datadir/kde4/services/ioslaveinfo.desktop
%_kde_datadir/kde4/services/renaudiodlg.desktop
%_kde_datadir/kde4/services/renimagedlg.desktop
%_kde_prefix/shutdown/nepomuk.sh
#%_kde_libdir/libkdeinit4_kcmshell.so
%_kde_libdir/libkdeinit4_khelpcenter.so
%_kde_datadir/kde4/services/khelpcenter.desktop
%_kde_bindir/khelpcenter
%_kde_appsdir/khelpcenter
%_kde_docdir/*/*/khelpcenter
%_kde_libdir/libkdeinit4_kinfocenter.so
%_kde_libdir/libkdeinit4_kjobviewer.so
%_kde_libdir/libkdeinit4_kprinter.so
%_kde_docdir/*/*/faq
%_kde_docdir/*/*/kcontrol
%_kde_docdir/*/*/glossary
%_kde_docdir/*/*/kdeprint
%_kde_docdir/*/*/kdesu
%_kde_docdir/*/*/kfind
%_kde_docdir/*/*/kioslave
%_kde_docdir/*/*/userguide
%_kde_docdir/*/*/visualdict
%_kde_docdir/*/*/quickstart
%_kde_docdir/*/*/kdebugdialog

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
%_kde_datadir/applications/kde4/konsolesu.desktop
%_kde_datadir/applications/kde4/quick-access-konsole.desktop
%_kde_appsdir/konqueror/servicemenus/konsolehere.desktop
%_kde_appsdir/konsole
%_kde_datadir/kde4/services/kded/kwrited.desktop
%_kde_datadir/kde4/services/konsole-script.desktop
%_kde_datadir/kde4/services/konsolepart.desktop
%_kde_datadir/kde4/servicetypes/terminalemulator.desktop
%_kde_docdir/*/*/konsole

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
%_kde_libdir/kde4/dolphinpart.so
%_kde_appsdir/dolphinpart/dolphinpart.rc
%_kde_appsdir/dolphin
%_kde_docdir/*/*/dolphin

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

#-----------------------------------------------------------------------------

%package -n kde4-kdeprintfax
Summary: kdeprintfax
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Requires: enscript
Obsoletes: kdebase4-kdeprintfax < 1:3.93.0-0.714129.2

%description -n kde4-kdeprintfax
Programm to send fax

%files -n kde4-kdeprintfax
%defattr(-,root,root)
%_kde_appsdir/kdeprintfax
%_kde_bindir/kdeprintfax
%_kde_datadir/applications/kde4/kdeprintfax.desktop

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
%_kde_libdir/kde4/kcm_nsplugins.so
%_kde_libdir/kde4/libkcminit_nsplugin.so
%_kde_appsdir/plugin/nspluginpart.rc
%_kde_datadir/kde4/services/khtml_plugins.desktop

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
%_kde_docdir/*/*/kwrite

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
%_kde_appsdir/kconf_update/kuriikwsfilter.upd
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
%_kde_datadir/kde4/services/fileappearance.desktop
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
%_kde_docdir/*/*/konqueror
%_kde_appsdir/konqueror
#%exclude %_kde_appsdir/konqueror/servicemenus/media_*
%exclude %_kde_appsdir/konqueror/servicemenus/konsolehere.desktop

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

#-----------------------------------------------------------------------------

%package -n phonon-xine
Summary: Xine backend to Phonon
Group: Sound
BuildRequires: libxine-devel
Obsoletes: kde4-phonon-xine < 1:3.93.0-0.714129.2

%description -n phonon-xine
Xine backend to Phonon.

%files -n phonon-xine
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_libdir/kde4/phonon_xine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop
%_kde_datadir/kde4/services/phononbackends/xine.desktop

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdebase 4
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libdolphinprivate = %epoch:%version
Requires: %libkonq = %epoch:%version
Requires: %libkonqsidebarplugin = %epoch:%version
Obsoletes: %{_lib}kdebase46-devel < 1:3.93.0-0.714129.2

%description  devel
This package contains header files needed if you wish to build applications based on kdebase.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*
%_kde_datadir/apps/cmake/*/*
%_kde_datadir/config.kcfg
%_datadir/dbus-1/interfaces/*
%exclude %_kde_libdir/libkdeinit*

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

# Nepomuk
install -d  -m 0755 %buildroot%_kde_prefix/env
install -d  -m 0755 %buildroot%_kde_prefix/shutdown
cat << EOF > %buildroot%_kde_prefix/env/nepomuk.sh
# start Nepomuk-KDE
%_kde_bindir/nepomukdaemon &
%_kde_bindir/nepomukcoreservices &
EOF
cat << EOF > %buildroot%_kde_prefix/shutdown/nepomuk.sh
# start Nepomuk-KDE
killall nepomukdaemon
killall nepomukcoreservices
EOF
chmod +x %buildroot%_kde_prefix/env/nepomuk.sh
chmod +x %buildroot%_kde_prefix/shutdown/nepomuk.sh

# The kmenu icon is required by kicker
pushd %buildroot%_kde_iconsdir/oxygen/
for i in 128x128 16x16 22x22 32x32 48x48 64x64; do
	ln -sf %_kde_iconsdir/oxygen/$i/actions/about-kde.png $i/apps/kmenu.png
done
ln -sf %_kde_iconsdir/oxygen/scalable/actions/about-kde.svgz scalable/apps/kmenu.svgz
popd
# kcalc.svgz crashes kicker
rm -rf %buildroot/%_kde_iconsdir/oxygen/scalable/apps/small/16x16/kcalc.svgz

%clean
rm -fr %buildroot

