
%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 681089

%if %unstable
%define dont_strip 1
%endif

Name: kdebase4
Summary: K Desktop Environment
Version: 3.91
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
Source1: kde4.sh
Source2: dmkde4start
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
Requires: kdebase4-runtime
Requires: kdebase4-workspace
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
Requires: kde4-kdm
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Meta package that requires all base kdebase 4 files

%files
%doc README

#-----------------------------------------------------------------------------

%package runtime
Summary: KDE 4 application runtime components
Group: Graphical desktop/KDE
Requires: kdelibs4-core
Requires: oxygen-icon-theme
Obsoletes: kdebase4-progs
Obsoletes: kdebase4-core 

%description runtime
KDE 4 application runtime components.

%files runtime
%defattr(-,root,root)
%_sysconfdir/profile.d/*
%_datadir/dbus-1/services/*
%_kde_datadir/icons/*/*/*/*
%_kde_appsdir/drkonqi
%_kde_appsdir/kcm_componentchooser
%_kde_appsdir/kcmlocale
%_kde_appsdir/kde
%_kde_appsdir/kdeprint
%_kde_appsdir/kdeprint_part
%_kde_appsdir/khelpcenter
%_kde_appsdir/kinfocenter
%_kde_appsdir/kcontrol
%_kde_appsdir/kio_finger/kio_finger.css
%_kde_appsdir/kio_finger/kio_finger.pl
%_kde_appsdir/kio_info/kde-info2html
%_kde_appsdir/kio_info/kde-info2html.conf
%_kde_appsdir/kio_man/kio_man.css
%_kde_appsdir/kjobviewer
%_kde_appsdir/konqueror/dirtree/remote/smb-network.desktop
%_kde_appsdir/konqueror/servicemenus/media_eject.desktop
%_kde_appsdir/konqueror/servicemenus/media_mount.desktop
%_kde_appsdir/konqueror/servicemenus/media_safelyremove.desktop
%_kde_appsdir/konqueror/servicemenus/media_unmount.desktop
%_kde_appsdir/kuiserver/icons/crystalsvg/16x16/apps/kio_uiserver.png
%_kde_appsdir/remoteview/smb-network.desktop
%_kde_appsdir/Settingsmenu
%_kde_appsdir/solidfakebluetoothbackend
%_kde_appsdir/solidfakenetbackend
%_kde_appsdir/systemview/documents.desktop
%_kde_appsdir/systemview/home.desktop
%_kde_appsdir/systemview/media.desktop
%_kde_appsdir/systemview/remote.desktop
%_kde_appsdir/systemview/trash.desktop
%_kde_appsdir/systemview/users.desktop
%_kde_datadir/kde4/services/nepomuk/nepomuk-coreservices.desktop
%_kde_bindir/drkonqi
%_kde_bindir/imagetops
%_kde_bindir/kcmshell
%_kde_bindir/kcontrol
%_kde_bindir/kde4-menu
%_kde_bindir/kdebugdialog
%_kde_bindir/kde-cp
%_kde_bindir/kdeeject
%_kde_bindir/kde-mv
%_kde_bindir/kde-open
%_kde_bindir/kdesu
%_kde_bindir/kdesud
%_kde_bindir/kfile
%_kde_bindir/khc_docbookdig.pl
%_kde_bindir/khc_htdig.pl
%_kde_bindir/khc_htsearch.pl
%_kde_bindir/khc_indexbuilder
%_kde_bindir/khc_mansearch.pl
%_kde_bindir/khelpcenter
%_kde_bindir/khotnewstuff
%_kde_bindir/kinfocenter
%_kde_bindir/kinstalltheme
%_kde_bindir/kioclient
%_kde_bindir/kioexec
%_kde_bindir/kio_media_mounthelper
%_kde_bindir/kio_system_documenthelper
%_kde_bindir/kjobviewer
%_kde_bindir/klocaldomainurifilterhelper
%_kde_bindir/kmimetypefinder
%_kde_bindir/knetattach
%_kde_bindir/knotify4
%_kde_bindir/kprinter
%_kde_bindir/kquitapp
%_kde_bindir/kreadconfig
%_kde_bindir/kstart
%_kde_bindir/ktraderclient
%_kde_bindir/ktrash
%_kde_bindir/kuiserver
%_kde_bindir/kwriteconfig
%_kde_bindir/solidshell
%_kde_libdir/kconf_update_bin/khotkeys_update
%_kde_libdir/kconf_update_bin/kicker-3.4-reverseLayout
%_kde_libdir/kconf_update_bin/kwin_update_default_rules
%_kde_libdir/kconf_update_bin/kwin_update_window_settings
%_kde_appsdir/kconf_update/convertShortcuts.pl
%_kde_appsdir/kconf_update/kaccel.upd
%_kde_appsdir/kconf_update/kcmdisplayrc.upd
%_kde_appsdir/kconf_update/khotkeys_32b1_update.upd
%_kde_appsdir/kconf_update/kicker-3.1-properSizeSetting.pl
%_kde_appsdir/kconf_update/kicker-3.5-kconfigXTize.pl
%_kde_appsdir/kconf_update/kicker-3.5-taskbarEnums.pl
%_kde_appsdir/kconf_update/kickerrc.upd
%_kde_appsdir/kconf_update/klipper-1-2.pl
%_kde_appsdir/kconf_update/klipper-kde31.sh
%_kde_appsdir/kconf_update/klipperrc.upd
%_kde_appsdir/kconf_update/klippershortcuts.upd
%_kde_appsdir/kconf_update/konqueror_gestures_kde321_update.upd
%_kde_appsdir/kconf_update/ksmserver.upd
%_kde_appsdir/kconf_update/kwin.upd
%_kde_appsdir/kconf_update/kwin3_plugin.pl
%_kde_appsdir/kconf_update/kwin3_plugin.upd
%_kde_appsdir/kconf_update/kwin_*
%_kde_appsdir/kconf_update/kwiniconify.upd
%_kde_appsdir/kconf_update/kwinsticky.upd
%_kde_appsdir/kconf_update/kwinupdatewindowsettings.upd
%_kde_appsdir/kconf_update/mouse_cursor_theme.upd
%_kde_appsdir/kconf_update/move_session_config.sh
%_kde_appsdir/kconf_update/pluginlibFix.pl
%_kde_configdir/xdg/menus/kde-information.menu
%_kde_configdir/xdg/menus/kde-kcontrol.menu
%_kde_configdir/xdg/menus/kde-settings.menu
%_kde_datadir/applications/kde4/Help.desktop
%_kde_datadir/applications/kde4/kjobviewer.desktop
%_kde_datadir/applications/kde4/knetattach.desktop
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
%_kde_datadir/kde4/services/home.protocol
%_kde_datadir/kde4/services/htmlthumbnail.desktop
%_kde_datadir/kde4/services/icons.desktop
%_kde_datadir/kde4/services/imagethumbnail.desktop
%_kde_datadir/kde4/services/info.protocol
%_kde_datadir/kde4/services/kcmcgi.desktop
%_kde_datadir/kde4/services/kcmkded.desktop
%_kde_datadir/kde4/services/kcm_kdnssd.desktop
%_kde_datadir/kde4/services/kcmnotify.desktop
%_kde_datadir/kde4/services/kcm_solid.desktop
%_kde_datadir/kde4/services/KControl.desktop
%_kde_datadir/kde4/services/kded/homedirnotify.desktop
%_kde_datadir/kde4/services/kded/ktimezoned.desktop
%_kde_datadir/kde4/services/kded/mediamanager.desktop
%_kde_datadir/kde4/services/kded/medianotifier.desktop
%_kde_datadir/kde4/services/kded/remotedirnotify.desktop
%_kde_datadir/kde4/services/kded/systemdirnotify.desktop
%_kde_datadir/kde4/services/kdeprint_part.desktop
%_kde_datadir/kde4/services/khelpcenter.desktop
%_kde_datadir/kde4/services/kinfocenter.desktop
%_kde_datadir/kde4/services/kmanpart.desktop
%_kde_datadir/kde4/services/knotify4.desktop
%_kde_datadir/kde4/services/kshorturifilter.desktop
%_kde_datadir/kde4/services/kuiserver.desktop
%_kde_datadir/kde4/services/kuriikwsfilter.desktop
%_kde_datadir/kde4/services/kurisearchfilter.desktop
%_kde_datadir/kde4/services/language.desktop
%_kde_datadir/kde4/services/ldap.protocol
%_kde_datadir/kde4/services/ldaps.protocol
%_kde_datadir/kde4/services/localdomainurifilter.desktop
%_kde_datadir/kde4/services/man.protocol
%_kde_datadir/kde4/services/media.desktop
%_kde_datadir/kde4/services/media.protocol
%_kde_datadir/kde4/services/nfs.protocol
%_kde_datadir/kde4/services/nntp.protocol
%_kde_datadir/kde4/services/nntps.protocol
%_kde_datadir/kde4/services/pop3.protocol
%_kde_datadir/kde4/services/pop3s.protocol
%_kde_datadir/kde4/services/printdb.protocol
%_kde_datadir/kde4/services/printers.desktop
%_kde_datadir/kde4/services/print.protocol
%_kde_datadir/kde4/services/programs.protocol
%_kde_datadir/kde4/services/remote.protocol
%_kde_datadir/kde4/services/searchproviders
%_kde_datadir/kde4/services/settings.protocol
%_kde_datadir/kde4/services/sftp.protocol
%_kde_datadir/kde4/services/smb.protocol
%_kde_datadir/kde4/services/smbstatus.desktop
%_kde_datadir/kde4/services/smtp.protocol
%_kde_datadir/kde4/services/smtps.protocol
%_kde_datadir/kde4/services/solidbackends
%_kde_datadir/kde4/services/svgthumbnail.desktop
%_kde_datadir/kde4/services/system.protocol
%_kde_datadir/kde4/services/tar.protocol
%_kde_datadir/kde4/services/textthumbnail.desktop
%_kde_datadir/kde4/services/thumbnail.protocol
%_kde_datadir/kde4/services/trash.protocol
%_kde_datadir/kde4/services/zip.protocol
%_kde_datadir/kde4/services/kded/networkstatus.desktop
%_kde_datadir/kde4/servicetypes/searchprovider.desktop
%_kde_datadir/kde4/servicetypes/solidbluetoothmanager.desktop
%_kde_datadir/kde4/servicetypes/solidnetworkmanager.desktop
%_kde_datadir/kde4/servicetypes/solidpowermanager.desktop
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
%_kde_libdir/kde4/kcm_media.so
%_kde_libdir/kde4/kcm_printmgr.so
%_kde_libdir/kde4/kcm_samba.so
%_kde_libdir/kde4/kcm_solid.so
%_kde_libdir/kde4/kded_homedirnotify.so
%_kde_libdir/kde4/kded_kpasswdserver.so
%_kde_libdir/kde4/kded_networkstatus.so
%_kde_libdir/kde4/kded_ktimezoned.so
%_kde_libdir/kde4/kded_mediamanager.so
%_kde_libdir/kde4/kded_medianotifier.so
%_kde_libdir/kde4/kded_remotedirnotify.so
%_kde_libdir/kde4/kded_systemdirnotify.so
%_kde_libdir/kde4/kio_about.so
%_kde_libdir/kde4/kio_cgi.so
%_kde_libdir/kde4/kio_filter.so
%_kde_libdir/kde4/kio_finger.so
%_kde_libdir/kde4/kio_fish.so
%_kde_libdir/kde4/kio_floppy.so
%_kde_libdir/kde4/kio_home.so
%_kde_libdir/kde4/kio_info.so
%_kde_libdir/kde4/kio_ldap.so
%_kde_libdir/kde4/kio_man.so
%_kde_libdir/kde4/kio_media.so
%_kde_libdir/kde4/kio_nfs.so
%_kde_libdir/kde4/kio_nntp.so
%_kde_libdir/kde4/kio_pop3.so
%_kde_libdir/kde4/kio_print.so
%_kde_libdir/kde4/kio_remote.so
%_kde_libdir/kde4/kio_settings.so
%_kde_libdir/kde4/kio_sftp.so
%_kde_libdir/kde4/kio_smb.so
%_kde_libdir/kde4/kio_smtp.so
%_kde_libdir/kde4/kio_system.so
%_kde_libdir/kde4/kio_tar.so
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
%_kde_libdir/kde4/solid_*
%_kde_bindir/nepomukcoreservices
%_kde_bindir/nepomukdaemon
%_kde_libdir/libkdeinit4_kcmshell.so
%_kde_libdir/libkdeinit4_kcontrol.so
%_kde_libdir/libkdeinit4_khelpcenter.so
%_kde_libdir/libkdeinit4_kinfocenter.so
%_kde_libdir/libkdeinit4_kjobviewer.so
%_kde_libdir/libkdeinit4_kprinter.so
%_kde_libdir/libkdeinit4_kuiserver.so
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

#------------------------------------------------	

%define libsolidcontrolifaces %mklibname solidcontrolifaces 5

%package -n %libsolidcontrolifaces
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libsolidcontrolifaces
KDE 4 core library.

%post -n %libsolidcontrolifaces -p /sbin/ldconfig
%postun -n %libsolidcontrolifaces -p /sbin/ldconfig

%files -n %libsolidcontrolifaces
%defattr(-,root,root)
%_kde_libdir/libsolidcontrolifaces.so.*

#------------------------------------------------	

%define libsolidcontrol %mklibname solidcontrol 5

%package -n %libsolidcontrol
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libsolidcontrol
KDE 4 core library.

%post -n %libsolidcontrol -p /sbin/ldconfig
%postun -n %libsolidcontrol -p /sbin/ldconfig

%files -n %libsolidcontrol
%defattr(-,root,root)
%_kde_libdir/libsolidcontrol.so.*

#------------------------------------------------

%define libkdecorations %mklibname kdecorations 5

%package -n %libkdecorations
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkdecorations
KDE 4 core library.

%post -n %libkdecorations -p /sbin/ldconfig
%postun -n %libkdecorations -p /sbin/ldconfig

%files -n %libkdecorations
%defattr(-,root,root)
%_kde_libdir/libkdecorations.so.*

#------------------------------------------------

%define libkfontinst %mklibname kfontinst 5

%package -n %libkfontinst
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkfontinst
KDE 4 core library.

%post -n %libkfontinst -p /sbin/ldconfig
%postun -n %libkfontinst -p /sbin/ldconfig

%files -n %libkfontinst
%defattr(-,root,root)
%_kde_libdir/libkfontinst.so.*

#------------------------------------------------

%define libkfontinstui %mklibname kfontinstui 5

%package -n %libkfontinstui
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkfontinstui
KDE 4 core library.

%post -n %libkfontinstui -p /sbin/ldconfig
%postun -n %libkfontinstui -p /sbin/ldconfig

%files -n %libkfontinstui
%defattr(-,root,root)
%_kde_libdir/libkfontinstui.so.*

#------------------------------------------------

%define libkickermain %mklibname kickermain 2

%package -n %libkickermain
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkickermain
KDE 4 core library.

%post -n %libkickermain -p /sbin/ldconfig
%postun -n %libkickermain -p /sbin/ldconfig

%files -n %libkickermain
%defattr(-,root,root)
%_kde_libdir/libkickermain.so.*

#------------------------------------------------

%define libkscreensaver %mklibname kscreensaver 5

%package -n %libkscreensaver
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkscreensaver
KDE 4 core library.

%post -n %libkscreensaver -p /sbin/ldconfig
%postun -n %libkscreensaver -p /sbin/ldconfig

%files -n %libkscreensaver
%defattr(-,root,root)
%_kde_libdir/libkscreensaver.so.*

#------------------------------------------------

%define libksgrd %mklibname ksgrd 4

%package -n %libksgrd
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libksgrd
KDE 4 core library.

%post -n %libksgrd -p /sbin/ldconfig
%postun -n %libksgrd -p /sbin/ldconfig

%files -n %libksgrd
%defattr(-,root,root)
%_kde_libdir/libksgrd.so.*

#------------------------------------------------

%define libkwineffects %mklibname kwineffects 1

%package -n %libkwineffects
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkwineffects
KDE 4 core library.

%post -n %libkwineffects -p /sbin/ldconfig
%postun -n %libkwineffects -p /sbin/ldconfig

%files -n %libkwineffects
%defattr(-,root,root)
%_kde_libdir/libkwineffects.so.*

#------------------------------------------------

%define libkworkspace %mklibname kworkspace 1

%package -n %libkworkspace
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkworkspace
KDE 4 core library.

%post -n %libkworkspace -p /sbin/ldconfig
%postun -n %libkworkspace -p /sbin/ldconfig

%files -n %libkworkspace
%defattr(-,root,root)
%_kde_libdir/libkworkspace.so.*

#------------------------------------------------

%define libplasma %mklibname plasma 1

%package -n %libplasma
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libplasma
KDE 4 core library.

%post -n %libplasma -p /sbin/ldconfig
%postun -n %libplasma -p /sbin/ldconfig

%files -n %libplasma
%defattr(-,root,root)
%_kde_libdir/libplasma.so.*

#------------------------------------------------

%define libprocesscore %mklibname processcore 5

%package -n %libprocesscore
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libprocesscore
KDE 4 core library.

%post -n %libprocesscore -p /sbin/ldconfig
%postun -n %libprocesscore -p /sbin/ldconfig

%files -n %libprocesscore
%defattr(-,root,root)
%_kde_libdir/libprocesscore.so.*

#------------------------------------------------

%define libprocessui %mklibname processui 5

%package -n %libprocessui
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libprocessui
KDE 4 core library.

%post -n %libprocessui -p /sbin/ldconfig
%postun -n %libprocessui -p /sbin/ldconfig

%files -n %libprocessui
%defattr(-,root,root)
%_kde_libdir/libprocessui.so.*

#------------------------------------------------

%define libtaskbar %mklibname taskbar 5

%package -n %libtaskbar
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libtaskbar
KDE 4 core library.

%post -n %libtaskbar -p /sbin/ldconfig
%postun -n %libtaskbar -p /sbin/ldconfig

%files -n %libtaskbar
%defattr(-,root,root)
%_kde_libdir/libtaskbar.so.*

#------------------------------------------------

%define libtaskmanager %mklibname taskmanager 5

%package -n %libtaskmanager
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libtaskmanager
KDE 4 core library.

%post -n %libtaskmanager -p /sbin/ldconfig
%postun -n %libtaskmanager -p /sbin/ldconfig

%files -n %libtaskmanager
%defattr(-,root,root)
%_kde_libdir/libtaskmanager.so.*


#-----------------------------------------------------------------------------

%package workspace
Summary: KDE 4 application runtime components
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Requires: strigi
Requires: desktop-common-data
Obsoletes: kdebase4-progs

%description workspace
KDE 4 application workspace components.

%post workspace
%make_session

%postun workspace
%make_session

%files workspace
%defattr(-,root,root)
%_sysconfdir/X11/wmsession.d/10KDE4
%_kde_bindir/dmkde4start
%_kde_bindir/appletproxy
%_kde_bindir/kaccess
%_kde_bindir/kapplymousetheme
%_kde_bindir/kblankscrn.kss
%_kde_bindir/kcheckpass
%_kde_bindir/kcheckrunning
%_kde_bindir/kcminit
%_kde_bindir/kcminit_startup
%_kde_bindir/kcontroledit
%_kde_bindir/kdeinstallktheme
%_kde_bindir/kdesktop
%_kde_bindir/kdostartupconfig
%_kde_bindir/kfontinst
%_kde_bindir/kfontprint
%_kde_bindir/kfontview
%_kde_bindir/khotkeys
%_kde_bindir/kicker
%_kde_bindir/klipper
%_kde_bindir/kmenuedit
%_kde_bindir/kpager
%_kde_bindir/krandom.kss
%_kde_bindir/krandrtray
%_kde_bindir/krdb
%_kde_bindir/krootimage
%_kde_bindir/krunner
%_kde_bindir/krunner_lock
%_kde_bindir/ksmserver
%_kde_bindir/ksplashsimple
%_kde_bindir/ksplashx
%_kde_bindir/ksplashx_scale
%_kde_bindir/kstartupconfig
%_kde_bindir/ksysguard
%_kde_bindir/ksysguardd
%_kde_bindir/ksystraycmd
%_kde_bindir/ktip
%_kde_bindir/kwebdesktop
%_kde_bindir/kwin
%_kde_bindir/kwin_killer_helper
%_kde_bindir/kwin_rules_dialog
%_kde_bindir/kxkb
%_kde_bindir/plasma
%_kde_bindir/plasmaengineexplorer
%_kde_bindir/startkde
%_kde_bindir/systemsettings
%_kde_configdir/systemsettingsrc
%_kde_prefix/env
%_kde_prefix/shutdown
%_kde_configdir/ksysguarddrc
%_kde_libdir/kde4/dockbar_panelextension.so
%_kde_libdir/kde4/fontthumbnail.so
%_kde_libdir/kde4/kcm_access.so
%_kde_libdir/kde4/kcm_accessibility.so
%_kde_libdir/kde4/kcm_background.so
%_kde_libdir/kde4/kcm_bell.so
%_kde_libdir/kde4/kcm_clock.so
%_kde_libdir/kde4/kcm_colors.so
%_kde_libdir/kde4/kcm_display.so
%_kde_libdir/kde4/kcm_energy.so
%_kde_libdir/kde4/kcm_fontinst.so
%_kde_libdir/kde4/kcm_fonts.so
%_kde_libdir/kde4/kcm_info.so
%_kde_libdir/kde4/kcm_input.so
%_kde_libdir/kde4/kcm_joystick.so
%_kde_libdir/kde4/kcm_keyboard.so
%_kde_libdir/kde4/kcm_keys.so
%_kde_libdir/kde4/kcm_khotkeys.so
%_kde_libdir/kde4/kcm_ksplashthemes.so
%_kde_libdir/kde4/kcm_kthememanager.so
%_kde_libdir/kde4/kcm_kwin4_effect_builtins.so
%_kde_libdir/kde4/kcm_kwindecoration.so
%_kde_libdir/kde4/kcm_kwineffects.so
%_kde_libdir/kde4/kcm_kwinoptions.so
%_kde_libdir/kde4/kcm_kwinrules.so
%_kde_libdir/kde4/kcm_launch.so
%_kde_libdir/kde4/kcm_nic.so
%_kde_libdir/kde4/kcm_randr.so
%_kde_libdir/kde4/kcm_screensaver.so
%_kde_libdir/kde4/kcm_smserver.so
%_kde_libdir/kde4/kcm_style.so
%_kde_libdir/kde4/kcm_usb.so
%_kde_libdir/kde4/kcm_view1394.so
%_kde_libdir/kde4/kcm_xinerama.so
%_kde_libdir/kde4/kded_khotkeys.so
%_kde_libdir/kde4/kgreet_classic.so
%_kde_libdir/kde4/kgreet_winbind.so
%_kde_libdir/kde4/kickermenu_*
%_kde_libdir/kde4/kio_fonts.so
%_kde_libdir/kde4/krunner_calculatorrunner.so
%_kde_libdir/kde4/krunner_searchrunner.so
%_kde_libdir/kde4/kstyle_keramik_config.so
%_kde_libdir/kde4/kwin3_*
%_kde_libdir/kde4/kwin4_*
%_kde_libdir/kde4/kwin_*
%_kde_libdir/kde4/launcher_panelapplet.so
%_kde_libdir/kde4/libexec/test_kcm_xinerama
%_kde_libdir/kde4/libkfontviewpart.so
%_kde_libdir/kde4/lockout_panelapplet.so
%_kde_libdir/kde4/media_panelapplet.so
%_kde_libdir/kde4/menu_panelapplet.so
%_kde_libdir/kde4/naughty_panelapplet.so
%_kde_libdir/kde4/plasma_*
%_kde_libdir/kde4/run_panelapplet.so
%_kde_libdir/kde4/sidebar_panelextension.so
%_kde_libdir/kde4/systemtray_panelapplet.so
%_kde_libdir/kde4/taskbar_panelapplet.so
%_kde_libdir/kde4/trash_panelapplet.so
%_kde_libdir/libkdeinit4_appletproxy.so
%_kde_libdir/libkdeinit4_kaccess.so
%_kde_libdir/libkdeinit4_kcminit.so
%_kde_libdir/libkdeinit4_kcminit_startup.so
%_kde_libdir/libkdeinit4_kcontroledit.so
%_kde_libdir/libkdeinit4_kdesktop.so
%_kde_libdir/libkdeinit4_khotkeys.so
%_kde_libdir/libkdeinit4_kicker.so
%_kde_libdir/libkdeinit4_klipper.so
%_kde_libdir/libkdeinit4_kmenuedit.so
%_kde_libdir/libkdeinit4_ksmserver.so
%_kde_libdir/libkdeinit4_ksysguard.so
%_kde_libdir/libkdeinit4_kwin.so
%_kde_libdir/libkdeinit4_kwin_rules_dialog.so
%_kde_libdir/libkdeinit4_kxkb.so
%_kde_libdir/strigi/strigita_font.so
%_kde_datadir/applications/kde4/kfontview.desktop
%_kde_datadir/applications/kde4/klipper.desktop
%_kde_datadir/applications/kde4/kmenuedit.desktop
%_kde_datadir/applications/kde4/kpager.desktop
%_kde_datadir/applications/kde4/krandrtray.desktop
%_kde_datadir/applications/kde4/ksysguard.desktop
%_kde_datadir/applications/kde4/ktip.desktop
%_kde_datadir/applications/kde4/kxkb.desktop
%_kde_appsdir/desktoptheme/default/dialogs/background.svg
%_kde_appsdir/desktoptheme/default/dialogs/shutdowndlg.svg
%_kde_appsdir/desktoptheme/default/dialogs/shutdowndlgbuttonglow.svg
%_kde_appsdir/desktoptheme/default/widgets/clock.svg
%_kde_appsdir/desktoptheme/default/widgets/iconbutton.svg
%_kde_appsdir/desktoptheme/default/widgets/plot-background.svg
%_kde_appsdir/desktoptheme/default/widgets/toolbox-button.svg
%_kde_appsdir/desktoptheme/desktoptheme-default.desktop
%_kde_appsdir/kcontroledit
%_kde_appsdir/kaccess/kaccess.notifyrc
%_kde_appsdir/kcminput/cursor_large_black.pcf.gz
%_kde_appsdir/kcminput/cursor_large_white.pcf.gz
%_kde_appsdir/kcminput/cursor_small_white.pcf.gz
%_kde_appsdir/kcminput/pics/mouse_lh.png
%_kde_appsdir/kcminput/pics/mouse_rh.png
%_kde_appsdir/kcmkeys/kde3.kksrc
%_kde_appsdir/kcmkeys/kde4.kksrc
%_kde_appsdir/kcmkeys/mac4.kksrc
%_kde_appsdir/kcmkeys/unix3.kksrc
%_kde_appsdir/kcmkeys/win3.kksrc
%_kde_appsdir/kcmkeys/win4.kksrc
%_kde_appsdir/kcmkeys/wm3.kksrc
%_kde_appsdir/kcmusb/usb.ids
%_kde_appsdir/kcmview1394/oui.db
%_kde_appsdir/kdesktop
%_kde_appsdir/kdewizard/pics/wizard_small.png
%_kde_appsdir/kdewizard/tips
%_kde_appsdir/kdisplay
%_kde_appsdir/kfontinst/bin/kio_fonts_helper
%_kde_appsdir/kfontinst/icons/crystalsvg/16x16/actions/disablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/16x16/actions/enablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/16x16/actions/newfont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/22x22/actions/disablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/22x22/actions/enablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/22x22/actions/newfont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/32x32/actions/disablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/32x32/actions/enablefont.png
%_kde_appsdir/kfontinst/icons/crystalsvg/32x32/actions/newfont.png
%_kde_appsdir/kfontinst/icons/oxygen/scalable/actions/disablefont.svgz
%_kde_appsdir/kfontinst/icons/oxygen/scalable/actions/enablefont.svgz
%_kde_appsdir/kfontinst/kfontviewpart.rc
%_kde_appsdir/kfontview/kfontviewui.rc
%_kde_appsdir/khotkeys/kde32b1.khotkeys
%_kde_appsdir/khotkeys/konqueror_gestures_kde321.khotkeys
%_kde_appsdir/kicker
%_kde_appsdir/kmenuedit/icons/crystalsvg/22x22/actions/menu_new.png
%_kde_appsdir/kmenuedit/icons/crystalsvg/22x22/actions/menu_new_sep.png
%_kde_appsdir/kmenuedit/icons/crystalsvg/32x32/actions/menu_new.png
%_kde_appsdir/kmenuedit/icons/crystalsvg/32x32/actions/menu_new_sep.png
%_kde_appsdir/kmenuedit/icons/locolor/16x16/actions/menu_new.png
%_kde_appsdir/kmenuedit/kmenueditui.rc
%_kde_appsdir/konqsidebartng/virtual_folders/services/fonts.desktop
%_kde_appsdir/konqueror/servicemenus/installfont.desktop
%_kde_appsdir/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%_kde_appsdir/ksmserver/pics/shutdownkonq.png
%_kde_appsdir/ksplash
%_kde_appsdir/ksysguard/KSysGuardApplet.xml
%_kde_appsdir/ksysguard/ProcessTable.sgrd
%_kde_appsdir/ksysguard/SystemLoad.sgrd
%_kde_appsdir/ksysguard/default_theme.svg
%_kde_appsdir/ksysguard/ksysguard.notifyrc
%_kde_appsdir/ksysguard/ksysguardui.rc
%_kde_appsdir/kthememanager
%_kde_appsdir/kwin
%_kde_appsdir/naughtyapplet/pics/naughty-happy.png
%_kde_appsdir/naughtyapplet/pics/naughty-sad.png
%_kde_datadir/autostart/khotkeys.desktop
%_kde_datadir/autostart/klipper.desktop
%_kde_datadir/autostart/krunner.desktop
%_kde_datadir/autostart/ktip.desktop
%_kde_datadir/autostart/panel.desktop
%_kde_datadir/autostart/plasma.desktop
%_kde_datadir/config/background.knsrc
%_kde_datadir/config/kdesktop_custom_menu1
%_kde_datadir/config/kdesktop_custom_menu2
%_kde_datadir/applications/kde4/systemsettings.desktop
%_kde_datadir/apps/desktoptheme/default/widgets/background.svg
%_kde_datadir/apps/systemsettings/systemsettingsui.rc
%_kde_datadir/kde4/services/settings-about-me.desktop
%_kde_datadir/kde4/services/settings-accessibility.desktop
%_kde_datadir/kde4/services/settings-advanced-user-settings.desktop
%_kde_datadir/kde4/services/settings-advanced.desktop
%_kde_datadir/kde4/services/settings-appearance.desktop
%_kde_datadir/kde4/services/settings-bluetooth.desktop
%_kde_datadir/kde4/services/settings-computer-administration.desktop
%_kde_datadir/kde4/services/settings-desktop.desktop
%_kde_datadir/kde4/services/settings-general.desktop
%_kde_datadir/kde4/services/settings-keyboard-and-mouse.desktop
%_kde_datadir/kde4/services/settings-look-and-feel.desktop
%_kde_datadir/kde4/services/settings-network-and-connectivity.desktop
%_kde_datadir/kde4/services/settings-network-settings.desktop
%_kde_datadir/kde4/services/settings-notifications.desktop
%_kde_datadir/kde4/services/settings-personal.desktop
%_kde_datadir/kde4/services/settings-regional-and-language.desktop
%_kde_datadir/kde4/services/settings-sharing.desktop
%_kde_datadir/kde4/services/settings-system.desktop
%_kde_datadir/kde4/services/settings-window-behaviour.desktop
%_kde_datadir/kde4/servicetypes/systemsettingscategory.desktop
%_kde_datadir/kde4/services/ScreenSavers/kblank.desktop
%_kde_datadir/kde4/services/ScreenSavers/krandom.desktop
%_kde_datadir/kde4/services/accessibility.desktop
%_kde_datadir/kde4/services/background.desktop
%_kde_datadir/kde4/services/bell.desktop
%_kde_datadir/kde4/services/clock.desktop
%_kde_datadir/kde4/services/colors.desktop
%_kde_datadir/kde4/services/devices.desktop
%_kde_datadir/kde4/services/display.desktop
%_kde_datadir/kde4/services/dma.desktop
%_kde_datadir/kde4/services/energy.desktop
%_kde_datadir/kde4/services/fontinst.desktop
%_kde_datadir/kde4/services/fonts.desktop
%_kde_datadir/kde4/services/fonts.protocol
%_kde_datadir/kde4/services/fontthumbnail.desktop
%_kde_datadir/kde4/services/installktheme.desktop
%_kde_datadir/kde4/services/interrupts.desktop
%_kde_datadir/kde4/services/ioports.desktop
%_kde_datadir/kde4/services/joystick.desktop
%_kde_datadir/kde4/services/kaccess.desktop
%_kde_datadir/kde4/services/kcmaccess.desktop
%_kde_datadir/kde4/services/kcmkicker.desktop
%_kde_datadir/kde4/services/kcmlaunch.desktop
%_kde_datadir/kde4/services/kcmsmserver.desktop
%_kde_datadir/kde4/services/kcmusb.desktop
%_kde_datadir/kde4/services/kcmview1394.desktop
%_kde_datadir/kde4/services/kded/khotkeys.desktop
%_kde_datadir/kde4/services/keyboard.desktop
%_kde_datadir/kde4/services/keyboard_layout.desktop
%_kde_datadir/kde4/services/keys.desktop
%_kde_datadir/kde4/services/kfontviewpart.desktop
%_kde_datadir/kde4/services/khotkeys.desktop
%_kde_datadir/kde4/services/krunner_calculatorrunner.desktop
%_kde_datadir/kde4/services/krunner_searchrunner.desktop
%_kde_datadir/kde4/services/ksplashthememgr.desktop
%_kde_datadir/kde4/services/kthememanager.desktop
%_kde_datadir/kde4/services/kwin/blur.desktop
%_kde_datadir/kde4/services/kwin/boxswitch.desktop
%_kde_datadir/kde4/services/kwin/demo_liquid.desktop
%_kde_datadir/kde4/services/kwin/demo_shiftworkspaceup.desktop
%_kde_datadir/kde4/services/kwin/demo_showpicture.desktop
%_kde_datadir/kde4/services/kwin/demo_taskbarthumbnail.desktop
%_kde_datadir/kde4/services/kwin/desktopgrid.desktop
%_kde_datadir/kde4/services/kwin/dialogparent.desktop
%_kde_datadir/kde4/services/kwin/diminactive.desktop
%_kde_datadir/kde4/services/kwin/drunken.desktop
%_kde_datadir/kde4/services/kwin/explosion.desktop
%_kde_datadir/kde4/services/kwin/fade.desktop
%_kde_datadir/kde4/services/kwin/fallapart.desktop
%_kde_datadir/kde4/services/kwin/flame.desktop
%_kde_datadir/kde4/services/kwin/howto.desktop
%_kde_datadir/kde4/services/kwin/magnifier.desktop
%_kde_datadir/kde4/services/kwin/maketransparent.desktop
%_kde_datadir/kde4/services/kwin/minimizeanimation.desktop
%_kde_datadir/kde4/services/kwin/mousemark.desktop
%_kde_datadir/kde4/services/kwin/presentwindows.desktop
%_kde_datadir/kde4/services/kwin/presentwindows_config.desktop
%_kde_datadir/kde4/services/kwin/scalein.desktop
%_kde_datadir/kde4/services/kwin/shadow.desktop
%_kde_datadir/kde4/services/kwin/shadow_config.desktop
%_kde_datadir/kde4/services/kwin/shakymove.desktop
%_kde_datadir/kde4/services/kwin/showfps.desktop
%_kde_datadir/kde4/services/kwin/test_fbo.desktop
%_kde_datadir/kde4/services/kwin/test_input.desktop
%_kde_datadir/kde4/services/kwin/test_thumbnail.desktop
%_kde_datadir/kde4/services/kwin/thumbnailaside.desktop
%_kde_datadir/kde4/services/kwin/trackmouse.desktop
%_kde_datadir/kde4/services/kwin/wavywindows.desktop
%_kde_datadir/kde4/services/kwin/zoom.desktop
%_kde_datadir/kde4/services/kwinactions.desktop
%_kde_datadir/kde4/services/kwinadvanced.desktop
%_kde_datadir/kde4/services/kwindecoration.desktop
%_kde_datadir/kde4/services/kwineffects.desktop
%_kde_datadir/kde4/services/kwinfocus.desktop
%_kde_datadir/kde4/services/kwinmoving.desktop
%_kde_datadir/kde4/services/kwinoptions.desktop
%_kde_datadir/kde4/services/kwinrules.desktop
%_kde_datadir/kde4/services/kwintranslucency.desktop
%_kde_datadir/kde4/services/memory.desktop
%_kde_datadir/kde4/services/mouse.desktop
%_kde_datadir/kde4/services/nic.desktop
%_kde_datadir/kde4/services/opengl.desktop
%_kde_datadir/kde4/services/partitions.desktop
%_kde_datadir/kde4/services/pci.desktop
%_kde_datadir/kde4/services/plasma-*
%_kde_datadir/kde4/services/processor.desktop
%_kde_datadir/kde4/services/randr.desktop
%_kde_datadir/kde4/services/screensaver.desktop
%_kde_datadir/kde4/services/scsi.desktop
%_kde_datadir/kde4/services/sound.desktop
%_kde_datadir/kde4/services/style.desktop
%_kde_datadir/kde4/services/xinerama.desktop
%_kde_datadir/kde4/services/xserver.desktop
%_kde_datadir/kde4/servicetypes/krunnerrunner.desktop
%_kde_datadir/kde4/servicetypes/kwineffect.desktop
%_kde_datadir/kde4/servicetypes/plasma_*
%_kde_datadir/kde4/servicetypes/screensaver.desktop
%_kde_datadir/sounds/pop.wav
%_kde_datadir/templates
%_kde_datadir/wallpapers
%_kde_appsdir/desktoptheme/default/widgets/wallpaper.svg
%_kde_docdir/*/*/khelpcenter
%_kde_docdir/*/*/kinfocenter
%_kde_docdir/*/*/kicker
%_kde_docdir/*/*/kmenuedit
%_kde_docdir/*/*/klipper
%_kde_docdir/*/*/knetattach
%_kde_docdir/*/*/kompmgr
%_kde_docdir/*/*/kpager
%_kde_docdir/*/*/kxkb
%_kde_docdir/*/*/ksysguard

#-----------------------------------------------------------------------------

%package -n kde4-konsole
Summary: Konsole
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: konsole4
Obsoletes: kdebase4-konsole

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
%_kde_appsdir/kconf_update/konsole.upd
%_kde_appsdir/kconf_update/schemaStrip.pl
%_kde_appsdir/konqueror/servicemenus/konsolehere.desktop
%_kde_appsdir/konsole
%_kde_datadir/kde4/services/kded/kwrited.desktop
%_kde_datadir/kde4/services/konsole-script.desktop
%_kde_datadir/kde4/services/konsolepart.desktop
%_kde_datadir/kde4/servicetypes/terminalemulator.desktop
%_kde_docdir/*/*/konsole

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

#------------------------------------------------	

%define libdolphinprivate %mklibname dolphinprivate 5

%package -n %libdolphinprivate
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libdolphinprivate
KDE 4 core library.

%post -n %libdolphinprivate -p /sbin/ldconfig
%postun -n %libdolphinprivate -p /sbin/ldconfig

%files -n %libdolphinprivate
%defattr(-,root,root)
%_kde_libdir/libdolphinprivate.so.*
%_kde_docdir/*/*/dolphin

#-----------------------------------------------------------------------------

%package -n kde4-dolphin
Summary: dolphin
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Provides: dolphin4

%description -n kde4-dolphin
A shell program similar to xterm for KDE

%files -n kde4-dolphin
%defattr(-,root,root)
%_kde_bindir/dolphin
%_kde_datadir/applications/kde4/dolphin.desktop
%_kde_appsdir/dolphin

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
Obsoletes: kdebase4-kdeprintfax

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
Obsoletes: kdebase4-kdepasswd

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
Obsoletes: kdebase4-nsplugins

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
Obsoletes: kdebase4-kwrite

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
%_kde_appsdir/konqueror/pics/arrow_bottomleft.png
%_kde_appsdir/konqueror/pics/arrow_bottomright.png
%_kde_appsdir/konqueror/pics/arrow_topleft.png
%_kde_appsdir/konqueror/pics/arrow_topright.png
%_kde_appsdir/konqueror/pics/thumbnailfont_7x4.png
%_kde_datadir/kde4/services/kded/favicons.desktop
%_kde_datadir/kde4/servicetypes/konqpopupmenuplugin.desktop

#------------------------------------------------	

%define libkonqsidebarplugin %mklibname konqsidebarplugin 5

%package -n %libkonqsidebarplugin
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkonqsidebarplugin
KDE 4 core library.

%post -n %libkonqsidebarplugin -p /sbin/ldconfig
%postun -n %libkonqsidebarplugin -p /sbin/ldconfig

%files -n %libkonqsidebarplugin
%defattr(-,root,root)
%_kde_libdir/libkonqsidebarplugin.so.*

#-----------------------------------------------------------------------------

%package -n kde4-konqueror
Summary: konqueror
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-konqueror

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
%_kde_libdir/kde4/konq_part.so
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
%_kde_appsdir/konqpart/konq_iconview.rc
%_kde_appsdir/konqpart/konq_listview.rc
%_kde_appsdir/konqsidebartng
%_kde_appsdir/konqueror/about
%_kde_appsdir/konqueror/icons
%_kde_appsdir/konqueror/konq-simplebrowser.rc
%_kde_appsdir/konqueror/konqueror.rc
%_kde_appsdir/konqueror/pics
%_kde_appsdir/konqueror/profiles
%_kde_appsdir/konqueror/servicemenus/text-ada-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-c++-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-c++h-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-ch-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-css-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-diff-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-html-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-java-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-log-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-makefile-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-pas-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-perl-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-python-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-tcl-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-tex-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-xml-print.desktop
%_kde_appsdir/konqueror/servicemenus/text-xslt-print.desktop
%_kde_appsdir/konqueror/tiles
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
%_kde_datadir/kde4/services/khtml_fonts.desktop
%_kde_datadir/kde4/services/khtml_general.desktop
%_kde_datadir/kde4/services/khtml_java_js.desktop
%_kde_datadir/kde4/services/konq_aboutpage.desktop
%_kde_datadir/kde4/services/konq_iconview4.desktop
%_kde_datadir/kde4/services/konq_listview.desktop
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

#-----------------------------------------------------------------------------

%package -n kde4-keditbookmarks
Summary: Bookmark editor
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-keditbookmarks

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
Obsoletes: kdebase4-kfind

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
Obsoletes: kdebase4-kdialog

%description -n kde4-kdialog
Dialog KDE base widgets

%files -n kde4-kdialog
%defattr(-,root,root)
%_kde_bindir/kdialog

#-----------------------------------------------------------------------------

%package -n kde4-kdm
Summary: KDE Desktop Login Manager
Group: Graphical desktop/KDE
Requires: kdebase4-runtime
Obsoletes: kdebase4-kdm

%description -n kde4-kdm
KDE Desktop Login Manager.

%files -n kde4-kdm
%defattr(-,root,root)
%_kde_bindir/kdm
%_kde_bindir/kdm_config
%_kde_bindir/kdm_greet
%_kde_bindir/kdmctl
%_kde_bindir/genkdmconf
%_kde_libdir/kde4/kcm_kdm.so
%_kde_appsdir/doc/kdm/README
%_kde_appsdir/kdm
%_kde_datadir/config/kdm.knsrc
%_kde_datadir/kde4/services/kdm.desktop
%_kde_docdir/*/*/kdm

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdebase 4
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libsolidcontrolifaces = %epoch:%version
Requires: %libsolidcontrol = %epoch:%version
Requires: %libkdecorations = %epoch:%version
Requires: %libkfontinst = %epoch:%version
Requires: %libkfontinstui = %epoch:%version
Requires: %libkickermain = %epoch:%version
Requires: %libkscreensaver = %epoch:%version
Requires: %libksgrd = %epoch:%version
Requires: %libkwineffects = %epoch:%version
Requires: %libkworkspace = %epoch:%version
Requires: %libplasma = %epoch:%version
Requires: %libprocesscore = %epoch:%version
Requires: %libprocessui = %epoch:%version
Requires: %libtaskbar = %epoch:%version
Requires: %libtaskmanager = %epoch:%version
Requires: %libdolphinprivate = %epoch:%version
Requires: %libkonquerorprivate = %epoch:%version
Requires: %libkonq = %epoch:%version
Requires: %libkonqsidebarplugin = %epoch:%version
Obsoletes: %{_lib}kdebase4-devel

%description  devel
This package contains header files needed if you wish to build applications based on kdebase.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*
%_kde_libdir/kde4/plugins/designer/*
%_kde_datadir/apps/cmake/*/*
%_kde_datadir/config.kcfg
%_datadir/dbus-1/interfaces/*
%exclude %_kde_libdir/libkdeinit*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdebase-%version

%build
%cmake_kde4 \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debug
%endif

%make 


%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# Env entry for kde4 
install -d -m 0755 %buildroot/etc/profile.d
install -m 0755 %SOURCE1 %buildroot/etc/profile.d

# Startup script ( no more patch startkde )
install -m 0755 %SOURCE2 %buildroot/%_kde_bindir/dmkde4start

install -d -m 0775 %buildroot/etc/X11/wmsession.d/
cat << EOF > %buildroot/etc/X11/wmsession.d/10KDE4
NAME=KDE4
ICON=kde-wmsession.xpm
DESC=The K Desktop Environment
EXEC=%_kde_bindir/dmkde4start
SCRIPT:
exec %_kde_bindir/dmkde4start
EOF

# KDM PAM Login
#install -d -m 0755 %buildroot/etc/pam.d/
#install -m 0644 %SOURCE3 %buildroot/etc/pam.d/kde4
#install -m 0644 %SOURCE4 %buildroot/etc/pam.d/kde4-np

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

%clean
rm -fr %buildroot

