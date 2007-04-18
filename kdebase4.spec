%define _requires_exceptions devel\(linux-gate\)\\|perl\(open\)

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig libkdebase6
%define lib_major 6
%define lib_name %mklibname kdebase4 %lib_major
%define epoch_kdelibs 30000000

Name: 		kdebase4
Summary:	K Desktop Environment - Core files
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.6
Epoch: 		1
Group: 		Graphical desktop/KDE
License:	GPL
URL: 		http://www.kde.org
Packager: 	Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version-%branch_date.tar.bz2
%else
Source: 	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebase-%version.tar.bz2
%endif
Source1: 	mandriva-profile-chooser-1.0.tar.bz2
Source2: 	kdm-migrate.pl
Source10:	kdebase-3.0-kde.pam
Source11:   kdebase-3.5-kde.pam
# Root desktop
Source155:	kdebase-3.5.4-root-interface.tar.bz2
# Old Menu 
Source200:      kdebase-3.0-menu-method
Source201:      kdebase-3.0-removekdesysmenu.pl
Source202:      kdebase-3.0-restorekdemimetypes.pl
Source203:      kdebase-3.0-savekdemimetypes.pl
Source204:      kdebase-3.0-menu-with-mimetypesupport
Source205:      kdebase-3.0-basedir
# David - 3.0-0.beta1.8mdk - Source206: allow users to use preferences (right
#                            click on K menu -> Preferences).
Source206:      kdebase-3.0-kmenu-preferences-switch-without-simpified-menu-support
# David - 3.0-0.beta1.8mdk - Menu method for Mandriva Linux 8.0
Source210:	kdebase-3.0-menu-method-mdk-8.0
# David - 2.2.2-53mdk - menu-method for MDK 8.1
Source211:  kdebase-3.0-menu-method-mdk-8.1
# David 2.2.2-53mdk - menu-method for MDK 8.2
Source212:  kdebase-3.0-menu-method-mdk-8.2
# David - 2.2.2-54mdk - To create 'What to do?' menu
Source213:  kdebase-3.1-9.1-create-what-to-do-menu
Source214:	kdebase-3.2-kde3-test-screensaver.sh
## David - 3.0-0.beta1.8mdk - Simplified menu
Source250:	kdebase-3.0-menu-method-simplified-menu
Source251:      kdebase-3.0-simplified-menu-removekdesysmenu.pl
Source252:      kdebase-3.0-simplified-menu-kdebasedir
# David - 3.0-0.beta1.8mdk - Source253: allow users to use preferences (right
#                                       click on K menu -> Preferences).
Source253:	kdebase-3.0-kmenu-preferences-switch-with-simpified-menu-support
# David - 2.2.2-53mdk - menu-method for simplied menu in MDK 8.2
Source254:  kdebase-3.0-menu-simplified
### David - 3.0-0.beta1.8mdk - Scripts used to configure desktop. 300 -> 399
## David - 3.0-0.beta1.8mdk - User's desktop
Source300:	kdebase-3.0-kdesktop-links
Source301:	kdebase-3.0-ArrangeIcons
Source302:	kdebase-3.0-test-windows-key
Source303:	kdebase-3.0-kdenetwork
# David - 2.2.2-60mdk - For MDK 8.2 only
Source304:  kdebase-3.0-8.2-kdesktop-links
# David - 3.1.3-70mdk - To open K menu
Source305:	kdebase-3.1.3-openkmenu
Source306:	kdebase-3.1.3-openkmenu.desktop
## David - 2.2.2-17mdk - PPC .desktop
# David - 2.2.2-17mdk - To fix undefined symbol... in Kcontrol -> Information
### David - 3.0-0.beta1.8mdk - Default icons on Desktop. 400 -> 499
# David - 3.0-0.beta1.8mdk - Source400 is used (with Source300) to line up icons on
#                      Desktop
Source400:	kdebase-3.0-kdesktop-ArangeIcons.desktop
Source401:	kdebase-3.0-kdesktop-CD-ROM.desktop
Source402:	kdebase-3.0-kdesktop-CD-ROM2.desktop
Source403:	kdebase-3.5.2-kdesktop-Control-Center.desktop
Source404:	kdebase-3.5.2-kdesktop-Documentation-de.desktop
Source405:	kdebase-3.5.2-kdesktop-Documentation-es.desktop
Source406:	kdebase-3.5.2-kdesktop-Documentation-fr.desktop
Source407:	kdebase-3.5.2-kdesktop-Documentation-it.desktop
Source408:	kdebase-3.5.2-kdesktop-Documentation.desktop
Source409:	kdebase-3.0-kdesktop-Floppy.desktop
Source410:	kdebase-3.0-kdesktop-Floppy2.desktop
Source412:	kdebase-3.5-kdesktop-Mandriva_Expert.desktop	
Source413:	kdebase-3.5-kdesktop-Mandriva_News.desktop	
Source414:	kdebase-3.5-kdesktop-Mandriva_Store.desktop	
Source415:	kdebase-3.0-kdesktop-Printer-kprinter.desktop
Source416:	kdebase-3.0-kdesktop-Printer-kups.desktop
Source417:	kdebase-3.0-kdesktop-Printer-lpr.desktop
Source418:	kdebase-3.0-kdesktop-Printer-qtcups.desktop
Source419:	kdebase-3.0-kdesktop-Printer-xpp.desktop
Source420:	kdebase-3.0-kdesktop-XKill.desktop
Source421:	kdebase-3.0-kdesktop-Zip.desktop
Source422:	kdebase-3.0-kdesktop-Zip2.desktop
Source423:	kdebase-3.0-kdesktop-directory-desktop
# David - 3.0-0.beta1.8mdk - Source424 is only used on PPC
Source424:	kdebase-3.0-kdesktop-Floppy3.desktop
Source425:	kdebase-3.0-connect-to-internet.desktop
Source426:	kdebase-3.0-connect-to-internet2.desktop
Source427:	kdebase-3.5-kdesktop-Mandriva_Club.desktop
Source428:	kdebase-3.0.3-removable_media.directory
# David - 3.0-0.beta1.8mdk - Replace image used in Kandalf by a safe one (from a law
#                      point of view)
Source510:	kdebase-3.0-wizard_small.png
#Source1000:	kdebase-3.0-kde3
Source1001:	kdebase-3.2-kde3-np
Source1002: kdebase-3.5-kde3-np
Source2000:	kdebase-2.2.2-8.2-kups
# David - 3.0.3-67mkd - Make FB happy - Icon for Mandriva documentation in kicker
Source3100: kdebase-3.0.3-mdkdoc-kicker
# Laurent default color scheme
Source5000:	kdebase-3.1-galaxy.kcsrc
Source5100:	kdebase-3.1.1-Galaxy.ktheme
Source7000:	kdebase-3.1.3-trash-profile
Source20001:	kdebase-3.2-konsole-migrate.pl
Source20002:	kdebase-3.2-kicker-migrate.pl
Source20003:	kdebase-3.4.2-www-browser-convert.pl

#Source30000:    kdebase-3.80.3-mdvsplashscreen.tar.bz2	

Source50000:	kdebase-3.2.3-migratemenu.pl
Source50001:    kdebase-3.2.3-translatemenu.upd
Source50002:    kdebase-3.2.3-migratemenu.sh
Source70000:    kdebase-3.2.3-alignment-icone
Source70001:    kdebase-3.2.3-alignment-icons.desktop
Source100000:	kdebase-3.4.1-devices.desktop
Source100001:	kdebase-3.4.1-devices.protocol
Source200000:	kdebase-3.4.2-lycoris.kcsrc
Source200001:	kdebase-3.4.2-Mandriva.preview.png
Source200002:	kdebase-3.4.2-Mandriva.xml
Source200020:	kdebase-3.4.2-devices-profiles
Source200022:	kdebase-hdd_win_mounted.desktop 
Source200023:	kdebase-hdd_win_unmounted.desktop
Source300000:	kdebase-3.5.4-IaOraBlue.kcsrc
Source300001:	kdebase-3.5.4-IaOraFree.kcsrc
Source300002:	kdebase-3.5.4-IaOraGray.kcsrc
Source300003:	kdebase-3.5.4-IaOraOrange.kcsrc


###             ###
### Patch party ###
###             ###

# Please keep it this section organised
# Please put name of patch in %%changelog

# Menudrake for distros before 2007
Patch0: kdebase-3.1-launch-menudrake-and-not-kmenuedit-in-K-menu.patch
# Right kcontrol path for Mandriva in Menu structure (Configuration/KDE)
Patch1: kdebase-3.2-fix-kcontrol-global.patch
Patch2: kdebase-3.5.2-move-xdg_menu_dir.patch
Patch3: kdebase-3.5.4-ksplashscreen-mdk.patch
# startkde without kpersonalizer
Patch7: kdebase-3.4.92-startkde
# Default Mandriva startpage
Patch14:	kdebase-3.0.3-fix-index-html.patch
# Fix paste local url in konsole : file:/mtc... 
Patch16:	kdebase-3.2-fix-paste-action-in-konsole.patch
# Fix panel default app in simplified menu
Patch22:	kdebase-3.1-fix-load-default-panel-appl-in-simplified-menu.patch
Patch23:	kdebase-kscreensaver-pamd-2006.patch
Patch24:	kdebase-3.3-remove-help-entry-into-kdesktop.patch
Patch25: kdebase-kscreensaver-pamd.patch
Patch26: kdebase-3.5.4-increase-default-kicker-size.patch
Patch32:	kdebase-3.2-kde-info2html.patch
Patch37:	kdebase-3.4.92-kicker-add-mdk-icon.patch
Patch39:	kdebase-3.3.2-fix-miniclip-icon.patch
Patch40:	kdebase-3.5.3-fix-media-fuser.patch
Patch42:	kdebase-3.4.0-konqueror-about.patch
Patch43:	kdebase-3.2-add-multimedia-key.patch
Patch48:	kdebase-3.4.0-fix-mdk-merge-dir.patch
Patch49:	kdebase-3.4.0-fix-scrnsaver.patch
Patch50:	kdebase-3.4.0-fix-arts-mdk-bugs-11671.patch
Patch51:	kdebase-3.4.0-fix-kfileivi.patch
Patch53:	kdebase-3.4.92-fix-convert-mdk-10.1-10.2.patch
Patch55:	kdebase-3.4.92-fix-launch-kicker-config.patch
Patch56:	kdebase-3.4.0-fix-kdesktop-launch-kcmshell.patch
Patch57:	kdebase-3.4.0-fix-konqueror-launch-kcmshell.patch
Patch58:	kdebase-3.4.0-fix-kwin-config-launcher.patch
Patch59:	kdebase-3.4.0-fix-kfmclient-launch.patch
Patch60:	kdebase-3.4.2-fix-kiosettings.patch
Patch61:	kdebase-3.4.2-fix-kicker-prefmenu.patch
Patch62:	kdebase-3.4.0-fix-vibrate-dialog.patch
Patch63:	kdebase-3.4.0-fix-kthememanager-mdk-bug-15567.patch
Patch65:	kdebase-3.4.0-fix-kde-bug-15327.patch
Patch66:	kdebase-3.4.0-fix-mdk-bug-16007.patch
Patch70:	kdebase-3.4.2-fix-launch-clock.patch
Patch71:	kdebase-3.4.2-fix-default-kthememanager-name.patch
# Verify posterior changes
Patch73:	kdebase-3.5.3-add-mdv-device.patch
Patch75:	kdebase-3.4.2-kwin-theme.patch
Patch76:	kdebase-3.4.2-mdkft.patch
Patch79:	kdebase-3.5.3-launch-drakeclock.patch
Patch80:	kdebase-3.4.2-fix-wrap-crash.patch
Patch82:	kdebase-3.4.2-startkde-align-icones.patch
Patch83:	kdebase-3.4.92-fix-detect-ntfs-partition.patch
Patch85:	kdebase-3.5.3-xinerama.patch
Patch86:	kdebase-3.4.92-kicker-launch-menudrake.patch
Patch87:	kdebase-3.5.0-fix-launch-printer-modules.patch
Patch89:	kdebase-3.5.3-install-script-kde.patch
Patch90: kdebase-3.5.2-dont-autostart-klipper.patch
Patch92:	kdebase-3.5.2-startkde-move-menu-directory.patch
Patch93: kdebase-3.2.3-fix-makefile-crypto.patch
# Post 3.5.4 release
Patch96: kdebase-3.5.3-fix-kthememanager-enable-button.patch
Patch101: kdebase-3.5.3-show-specific-kde-desktop-file-only-kde.patch
Patch125: kdebase-3.5.1-rubberband.patch
Patch126: kdebase-3.5.4-rubberband-kcmstyle.patch
Patch145: kdebase-3.3.2-fix-kdm-theme-mdk.patch
Patch147: kdebase-3.4.2-fix-kdm-server-args.patch
Patch148: kdebase-3.5.3-logout-without-confirmation.patch
Patch149: kdebase-3.5.4-be-sure-that-we-use-aa.patch
Patch150: kdebase-3.5.4-kdeeject-hal.patch 
Patch151: kdebase-3.5.4-international-bookmarks.patch
Patch152: kdebase-3.5.4-fix-old-icon-pos.patch
Patch154: kdebase-3.5.4-media-mnt.patch
Patch155: kdebase-3.5.4-fix-gtk-style.patch
#Patch156: kdebase-3.5.4-fix-kdeeject-multi-umount-error.patch
Patch158:	kdebase-3.5.4-fix-screensaver-onlyshowin-kde.patch

Patch159:	kdebase-3.4.2-npapi-64bit-fixes.patch
Patch160:	kdebase-3.5.5-fix-kthememanager-kicker-config.patch
Patch161:	kdebase-3.5.5-fix-nsplugins-default-value.patch

Patch163:	kdebase-3.5.5-fix-dbus-mediamanager.patch

#####################################kde4
Patch1000:	kdebase-4.0-startkde.patch
#Patch1001:	kdebase-3.80.3-add-mdv-splashscreen.patch

#Laurent Necessary ?
BuildConflicts: lm_utils
BuildConflicts: lm_utils-devel
BuildConflicts: liblm_sensors1
BuildConflicts: liblm_sensors1-devel
BuildRequires: cmake
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: fontconfig-devel >= 2.1-9mdk
BuildRequires: pam-devel
BuildRequires: freetype2-devel
BuildRequires:	libsasl-devel
BuildRequires:	openldap-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-client-devel
BuildRequires:	libsmbclient-devel > 3.0
BuildRequires:	libieee1284-devel
BuildRequires: OpenEXR-devel
BuildRequires: mandrakelinux-create-kde-mdk-menu >= 2007-2mdk
BuildRequires:	hal-devel 
BuildRequires: libusb-devel
BuildRequires: libxml2-utils
BuildRequires:  X11-devel
BuildRequires:	mesaglut-devel
BuildRequires: bdftopcf
BuildRequires:	imake
BuildRequires:	libraw1394-devel
BuildRequires:	libxklavier-devel
BuildRequires:	kdepimlibs4-devel >= %version-%mini_release
BuildRequires: lua-devel
BuildRequires: resmgr-devel
BuildRequires:	strigi-devel
#For next snapshot
BuildRequires:	libnetworkmanager-util-devel
BuildRequires:	networkmanager-devel

Requires:	%name-progs = %epoch:%version-%release
Requires:	%name-konsole = %epoch:%version-%release
Requires:	%name-kdeprintfax = %epoch:%version-%release
Requires:	%name-kmenuedit = %epoch:%version-%release
BuildRoot:	%_tmppath/%name-%version-%release-root

%description
Core applications for the K Desktop Environment.
Here is an overview of the directories:

	- drkonqi: if ever an app crashes (heaven forbid!) then Dr.Konqi will be so
          kind and make a stack trace. This is a great help for the
          developers to fix the bug.
	- kappfinder: searches your hard disk for non-KDE applications, e.g. Acrobat
             Reader (tm) and installs those apps under the K start button
	- kcheckpass: small program to enter and check passwords, only to be used by
             other programs
	- kcontrol: the KDE Control Center allows you to tweak the KDE settings
	- kdebugdialog: allows you to specify which debug messages you want to see
	- kdeprint: the KDE printing system
	- kdesktop: you guessed it: the desktop above the panel
	- kdesu: a graphical front end to "su"
	- kdm: replacement for XDM, for those people that like graphical logins
	- kfind: find files
	- khelpcenter: the app to read all great documentation about KDE
	- khotkeys: intercepts keys and can call applications
	- kicker: the panel at the botton with the K start button and the 
				taskbar etc
	- kioslave: infrastructure that helps make every application internet 
				enabled e.g. to directly save a 
				file to ftp://place.org/dir/file.txt
	- klipper: enhances and extenses the X clipboard
	- kmenuedit: edit for the menu below the K start button
	- konqueror: the file manager and web browser you get easily used to
	- kpager: applet to show the contents of the virtual desktops
	- kpersonalizer: the customization wizard you get when you first start KDE
	- kreadconfig: a tool for shell scripts to get info from KDE's config files
	- kscreensaver: the KDE screensaver environment and lot's of savers
	- ksmserver: the KDE session manager (saves program status on login, 
				restarts those program at the next login)
	- ksplash: the screen displayed while KDE starts
	- kstart: to launch applications with special window properties
         such as iconified etc
	- ksysguard: task manager and system monitor, even for remote systems
	- ksystraycmd: allows to run any application in the system tray
	- ktip: gives you tips how to use KDE
	- kwin: the KDE window manager
	- kxkb: a keyboard map tool
	- legacyimport: odd name for a cute program to load GTK themes
	- libkonq: some libraries needed by Konqueror
	- nsplugins: together with OSF/Motif or Lesstif allows you to use Netscape
			(tm) plugins in Konqueror

%files
%doc README


#-----------------------------------------------------------------------------

%package progs
Summary:	K Desktop Environment - Core files
Group:		Development/KDE and Qt
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
# For kio-fish MDK bug#16934
Requires: openssh-clients
Requires: xinit
Requires: iceauth
Requires: xkbcomp
Requires: xsetroot
Requires: xset
Requires: xrandr
Requires: setxkbmap
Requires: xmessage
Requires: xprop
Requires: mdk-menu-messages
Requires: %lib_name = %epoch:%version-%release
#TODO: Laurent port to kde4
#Requires: ia_ora-kde-kwin 
#Requires: kde-config-file >= 10.2-2mdk
Requires: initscripts 
Requires: mandrake_desk
Requires: indexhtml 
Requires: libsmbclient
Requires: kdelibs4-common 
Requires: sasl-plug-plain

%description progs
Core applications for the K Desktop Environment.
Here is an overview of the directories:

	- drkonqi: if ever an app crashes (heaven forbid!) then Dr.Konqi will be so
          kind and make a stack trace. This is a great help for the
          developers to fix the bug.
	- kappfinder: searches your hard disk for non-KDE applications, e.g. Acrobat
             Reader (tm) and installs those apps under the K start button
	- kcheckpass: small program to enter and check passwords, only to be used by
             other programs
	- kcontrol: the KDE Control Center allows you to tweak the KDE settings
	- kdebugdialog: allows you to specify which debug messages you want to see
	- kdeprint: the KDE printing system
	- kdesktop: you guessed it: the desktop above the panel
	- kdesu: a graphical front end to "su"
	- kdm: replacement for XDM, for those people that like graphical logins
	- kfind: find files
	- khelpcenter: the app to read all great documentation about KDE
	- khotkeys: intercepts keys and can call applications
	- kicker: the panel at the botton with the K start button and the 
				taskbar etc
	- kioslave: infrastructure that helps make every application internet 
				enabled e.g. to directly save a 
				file to ftp://place.org/dir/file.txt
	- klipper: enhances and extenses the X clipboard
	- kmenuedit: edit for the menu below the K start button
	- konqueror: the file manager and web browser you get easily used to
	- kpager: applet to show the contents of the virtual desktops
	- kpersonalizer: the customization wizard you get when you first start KDE
	- kreadconfig: a tool for shell scripts to get info from KDE's config files
	- kscreensaver: the KDE screensaver environment and lot's of savers
	- ksmserver: the KDE session manager (saves program status on login, 
				restarts those program at the next login)
	- ksplash: the screen displayed while KDE starts
	- kstart: to launch applications with special window properties
         such as iconified etc
	- ksysguard: task manager and system monitor, even for remote systems
	- ksystraycmd: allows to run any application in the system tray
	- ktip: gives you tips how to use KDE
	- kwin: the KDE window manager
	- kxkb: a keyboard map tool
	- legacyimport: odd name for a cute program to load GTK themes
	- libkonq: some libraries needed by Konqueror
	- nsplugins: together with OSF/Motif or Lesstif allows you to use Netscape
			(tm) plugins in Konqueror

%post progs
/sbin/ldconfig
%make_session
#Laurent 3.80.3 reactivate it ?
#kicker-migrate.pl /usr/share/config/kickerrc
%{update_desktop_database}
%update_icon_cache crystalsvg

#%preun progs


%postun progs
/sbin/ldconfig
%make_session
%{clean_desktop_database}
%clean_icon_cache crystalsvg

%files progs
%defattr(-,root,root)
%_bindir/khotnewstuff
%_bindir/kfontinst
%_bindir/khc_indexbuilder
%_bindir/krandrtray
%_bindir/kwin_killer_helper
%_bindir/kwriteconfig
%_bindir/mdkdoc-kicker
%_bindir/klocaldomainurifilterhelper
%_bindir/ArrangeIcons
%_bindir/appletproxy
%_bindir/drkonqi
%_bindir/kdialog
%_bindir/kdm-migrate.pl
%_bindir/kaccess
%_bindir/kappfinder
%attr(4755,root,root) %_bindir/kcheckpass
%_bindir/kcminit
%_bindir/kcontrol
%_bindir/kcontroledit
%_bindir/kdeinstallktheme
%_bindir/kdepasswd
%_datadir/apps/kicker/builtins/bookmarks.desktop
%_datadir/apps/kicker/builtins/browser.desktop
%_datadir/apps/kicker/builtins/desktop.desktop
%_datadir/apps/kicker/builtins/exec.desktop
%_datadir/apps/kicker/builtins/kmenu.desktop
%_datadir/apps/kicker/builtins/windowlist.desktop
%dir %_datadir/apps/remoteview/
%_datadir/apps/remoteview/smb-network.desktop
%_bindir/kicker-migrate.pl
%_bindir/www-browser-convert.pl
%_bindir/kdebugdialog
%_bindir/kdeeject
%_bindir/kdesktop
%_bindir/kdesktop-links
%_bindir/kfind
%_bindir/ksystraycmd
%_bindir/kdesktop-network
%_bindir/kdesu
%attr(2755,root,nogroup) %_bindir/kdesud
%_bindir/keditbookmarks
%_bindir/keditfiletype
%_bindir/kfmclient
%_bindir/khelpcenter
%_bindir/kinfocenter
%_bindir/khotkeys
%_bindir/kicker
%_bindir/kjobviewer
%_bindir/klipper
%_bindir/kmenu-preferences-switch
%_bindir/konqueror
%_bindir/kpager
%_bindir/kprinter 
%_bindir/krdb
%_bindir/kreadconfig
%_bindir/ksmserver
%_bindir/kstart
%_bindir/ksysguard
%_bindir/ksysguardd
%_bindir/ktip
%_bindir/kwebdesktop
%_bindir/kwin
%_bindir/kwrite
%_bindir/kxkb
%_bindir/openkmenu
%_bindir/startkde*
%_bindir/test-windows-key
%_bindir/alignment-icons
%_bindir/kcmshell
%_bindir/kinstalltheme
%_bindir/krunner
%_bindir/kfile
%_bindir/kfontview
%_bindir/kioexec
%_bindir/kmimetypefinder
%_bindir/knotify
%_bindir/ksplashsimple
%_bindir/ksplashx
%_bindir/ksplashx_scale

%_bindir/kde-cp
%_bindir/kde-mv
%_bindir/kde-open
%_bindir/kioclient
%_bindir/kquitapp
%_bindir/kwin_rules_dialog
%_bindir/solidshell

%_bindir/lpr-kprinter
%_bindir/qtcups
%_bindir/kups
%_bindir/krunner_lock
%_bindir/kuiserver
%_bindir/plasma-qgv


%_datadir/apps/desktoptheme/default/background/shutdowndlg.svg
%_datadir/apps/kfontinst/bin/kio_fonts_helper
%_datadir/config/khotnewstuffrc

#
#
#
# David - 3.0-0.beta1.8mdk - Screensavers
#                            Please not included those which can have legal
#                            issue (kmatrix is a good example)
%_bindir/kblankscrn.kss
%_bindir/krandom.kss
%_bindir/kapplymousetheme
%_bindir/kio_system_documenthelper
%_bindir/kcminit_startup

%_bindir/dolphin
%_datadir/apps/dolphin/dolphinui.rc
%_datadir/apps/dolphin/icons/hicolor/128x128/actions/preview.png
%_datadir/apps/dolphin/icons/hicolor/16x16/actions/editurl.png
%_datadir/apps/dolphin/icons/hicolor/16x16/actions/preview.png
%_datadir/apps/dolphin/icons/hicolor/22x22/actions/preview.png
%_datadir/apps/dolphin/icons/hicolor/32x32/actions/preview.png
%_datadir/apps/dolphin/icons/hicolor/48x48/actions/preview.png
%_datadir/apps/dolphin/icons/hicolor/64x64/actions/preview.png
%_datadir/apps/dolphin/servicemenus/*.desktop

%dir %_docdir/HTML/en/quickstart/
%doc %_docdir/HTML/en/quickstart/*.bz2
%doc %_docdir/HTML/en/quickstart/*.docbook
%dir %_docdir/HTML/en/userguide/
%doc %_docdir/HTML/en/userguide/*.png
%doc %_docdir/HTML/en/userguide/*.bz2
%doc %_docdir/HTML/en/userguide/*.docbook
%dir %_docdir/HTML/en/visualdict/
%doc %_docdir/HTML/en/visualdict/*.bz2
%doc %_docdir/HTML/en/visualdict/*.docbook
%doc %_docdir/HTML/en/visualdict/*.png

%dir %_docdir/HTML/en/konqueror/
%doc %_docdir/HTML/en/konqueror/*.png
%doc %_docdir/HTML/en/konqueror/*.bz2
%doc %_docdir/HTML/en/konqueror/*.docbook

%dir %_docdir/HTML/en/kpager/
%doc %_docdir/HTML/en/kpager/*.bz2
%doc %_docdir/HTML/en/kpager/*.docbook
%doc %_docdir/HTML/en/kpager/*.png

%doc %_docdir/HTML/en/ksysguard/*.bz2
%doc %_docdir/HTML/en/ksysguard/*.docbook

%dir %_docdir/HTML/en/kwrite/
%doc %_docdir/HTML/en/kwrite/*.bz2
%doc %_docdir/HTML/en/kwrite/*.docbook

%dir %_docdir/HTML/en/kxkb/
%doc %_docdir/HTML/en/kxkb/*.bz2
%doc %_docdir/HTML/en/kxkb/*.docbook

%dir %_docdir/HTML/en/kioslave/
%doc %_docdir/HTML/en/kioslave/*.docbook
%dir %_docdir/HTML/en/klipper/
%doc %_docdir/HTML/en/klipper/*.bz2
%doc %_docdir/HTML/en/klipper/*.docbook
%doc %_docdir/HTML/en/klipper/*.png
%dir %_docdir/HTML/en/knetattach/
%doc %_docdir/HTML/en/knetattach/*.bz2
%doc %_docdir/HTML/en/knetattach/*.docbook
%doc %_docdir/HTML/en/knetattach/*.png
%dir %_docdir/HTML/en/kompmgr/
%doc %_docdir/HTML/en/kompmgr/*.bz2
%doc %_docdir/HTML/en/kompmgr/*.docbook

%dir %_docdir/HTML/en/kinfocenter/dma/
%doc %_docdir/HTML/en/kinfocenter/dma/*.docbook
%dir %_docdir/HTML/en/kinfocenter/
%doc %_docdir/HTML/en/kinfocenter/*.bz2
%doc %_docdir/HTML/en/kinfocenter/*.docbook
%dir %_docdir/HTML/en/kinfocenter/interrupts/
%doc %_docdir/HTML/en/kinfocenter/interrupts/*.bz2
%doc %_docdir/HTML/en/kinfocenter/interrupts/*.docbook
%dir %_docdir/HTML/en/kinfocenter/ioports/
%doc %_docdir/HTML/en/kinfocenter/ioports/*.bz2
%doc %_docdir/HTML/en/kinfocenter/ioports/*.docbook
%dir %_docdir/HTML/en/kinfocenter/memory/
%doc %_docdir/HTML/en/kinfocenter/memory/*.bz2
%doc %_docdir/HTML/en/kinfocenter/memory/*.docbook
%dir %_docdir/HTML/en/kinfocenter/nics/
%doc %_docdir/HTML/en/kinfocenter/nics/*.bz2
%doc %_docdir/HTML/en/kinfocenter/nics/*.docbook
%dir %_docdir/HTML/en/kinfocenter/opengl/
%doc %_docdir/HTML/en/kinfocenter/opengl/*.bz2
%doc %_docdir/HTML/en/kinfocenter/opengl/*.docbook
%dir %_docdir/HTML/en/kinfocenter/partitions/
%doc %_docdir/HTML/en/kinfocenter/partitions/*.bz2
%doc %_docdir/HTML/en/kinfocenter/partitions/*.docbook
%dir %_docdir/HTML/en/kinfocenter/pci/
%doc %_docdir/HTML/en/kinfocenter/pci/*.bz2
%doc %_docdir/HTML/en/kinfocenter/pci/*.docbook
%dir %_docdir/HTML/en/kinfocenter/pcmcia/
%doc %_docdir/HTML/en/kinfocenter/pcmcia/*.bz2
%doc %_docdir/HTML/en/kinfocenter/pcmcia/*.docbook
%dir %_docdir/HTML/en/kinfocenter/processor/
%doc %_docdir/HTML/en/kinfocenter/processor/*.bz2
%doc %_docdir/HTML/en/kinfocenter/processor/*.docbook
%dir %_docdir/HTML/en/kinfocenter/protocols/
%doc %_docdir/HTML/en/kinfocenter/protocols/*.bz2
%doc %_docdir/HTML/en/kinfocenter/protocols/*.docbook
%dir %_docdir/HTML/en/kinfocenter/samba/
%doc %_docdir/HTML/en/kinfocenter/samba/*.bz2
%doc %_docdir/HTML/en/kinfocenter/samba/*.docbook
%dir %_docdir/HTML/en/kinfocenter/scsi/
%doc %_docdir/HTML/en/kinfocenter/scsi/*.bz2
%doc %_docdir/HTML/en/kinfocenter/scsi/*.docbook
%dir %_docdir/HTML/en/kinfocenter/sound/
%doc %_docdir/HTML/en/kinfocenter/sound/*.bz2
%doc %_docdir/HTML/en/kinfocenter/sound/*.docbook
%dir %_docdir/HTML/en/kinfocenter/usb/
%doc %_docdir/HTML/en/kinfocenter/usb/*.bz2
%doc %_docdir/HTML/en/kinfocenter/usb/*.docbook
%dir %_docdir/HTML/en/kinfocenter/xserver/
%doc %_docdir/HTML/en/kinfocenter/xserver/*.bz2
%doc %_docdir/HTML/en/kinfocenter/xserver/*.docbook
%dir %_docdir/HTML/en/kioslave/
%doc %_docdir/HTML/en/kioslave/*.bz2
%dir %_docdir/HTML/en/kinfocenter/devices/
%doc %_docdir/HTML/en/kinfocenter/devices/*.docbook
%dir %_docdir/HTML/en/kinfocenter/dma/
%doc %_docdir/HTML/en/kinfocenter/dma/*.bz2

%dir %_docdir/HTML/en/kfind/
%doc %_docdir/HTML/en/kfind/*.bz2
%doc %_docdir/HTML/en/kfind/*.docbook
%dir %_docdir/HTML/en/khelpcenter/
%doc %_docdir/HTML/en/khelpcenter/*.bz2
%doc %_docdir/HTML/en/khelpcenter/*.docbook
%doc %_docdir/HTML/en/khelpcenter/*.png
%dir %_docdir/HTML/en/kicker/
%doc %_docdir/HTML/en/kicker/*.png
%doc %_docdir/HTML/en/kicker/*.bz2
%doc %_docdir/HTML/en/kicker/*.docbook
%dir %_docdir/HTML/en/kinfocenter/devices/
%doc %_docdir/HTML/en/kinfocenter/devices/*.bz2
%doc %_docdir/HTML/en/kinfocenter/devices/*.docbook
%dir %_docdir/HTML/en/kinfocenter/dma/
%doc %_docdir/HTML/en/kinfocenter/dma/*.bz2
%dir %_docdir/HTML/en/kdeprint/
%doc %_docdir/HTML/en/kdeprint/*.png
%doc %_docdir/HTML/en/kdeprint/*.bz2
%doc %_docdir/HTML/en/kdeprint/*.docbook
%dir %_docdir/HTML/en/kdesu/
%doc %_docdir/HTML/en/kdesu/*.bz2
%doc %_docdir/HTML/en/kdesu/*.docbook
%dir %_docdir/HTML/en/kdm/
%doc %_docdir/HTML/en/kdm/*.bz2
%doc %_docdir/HTML/en/kdm/*.docbook
%dir %_docdir/HTML/en/kcontrol/keyboard/
%doc %_docdir/HTML/en/kcontrol/keyboard/*.docbook
%dir %_docdir/HTML/en/kcontrol/keys/
%doc %_docdir/HTML/en/kcontrol/keys/*.bz2
%doc %_docdir/HTML/en/kcontrol/keys/*.docbook
%dir %_docdir/HTML/en/kcontrol/khtml/
%doc %_docdir/HTML/en/kcontrol/khtml/*.bz2
%doc %_docdir/HTML/en/kcontrol/khtml/*.docbook
%dir %_docdir/HTML/en/kcontrol/kwindecoration/
%doc %_docdir/HTML/en/kcontrol/kwindecoration/*.bz2
%doc %_docdir/HTML/en/kcontrol/kwindecoration/*.docbook
%dir %_docdir/HTML/en/kcontrol/language/
%doc %_docdir/HTML/en/kcontrol/language/*.bz2
%doc %_docdir/HTML/en/kcontrol/language/*.docbook
%dir %_docdir/HTML/en/kcontrol/mouse/
%doc %_docdir/HTML/en/kcontrol/mouse/*.bz2
%doc %_docdir/HTML/en/kcontrol/mouse/*.docbook
%dir %_docdir/HTML/en/kcontrol/netpref/
%doc %_docdir/HTML/en/kcontrol/netpref/*.bz2
%doc %_docdir/HTML/en/kcontrol/netpref/*.docbook
%dir %_docdir/HTML/en/kcontrol/panel/
%doc %_docdir/HTML/en/kcontrol/panel/*.bz2
%doc %_docdir/HTML/en/kcontrol/panel/*.docbook
%dir %_docdir/HTML/en/kcontrol/panelappearance/
%doc %_docdir/HTML/en/kcontrol/panelappearance/*.bz2
%doc %_docdir/HTML/en/kcontrol/panelappearance/*.docbook
%dir %_docdir/HTML/en/kcontrol/passwords/
%doc %_docdir/HTML/en/kcontrol/passwords/*.bz2
%doc %_docdir/HTML/en/kcontrol/passwords/*.docbook
%dir %_docdir/HTML/en/kcontrol/performance/
%doc %_docdir/HTML/en/kcontrol/performance/*.bz2
%doc %_docdir/HTML/en/kcontrol/performance/*.docbook
%dir %_docdir/HTML/en/kcontrol/proxy/
%doc %_docdir/HTML/en/kcontrol/proxy/*.bz2
%doc %_docdir/HTML/en/kcontrol/proxy/*.docbook
%dir %_docdir/HTML/en/kcontrol/screensaver/
%doc %_docdir/HTML/en/kcontrol/screensaver/*.bz2
%doc %_docdir/HTML/en/kcontrol/screensaver/*.docbook
%doc %_docdir/HTML/en/kcontrol/*.png
%dir %_docdir/HTML/en/kcontrol/smb/
%doc %_docdir/HTML/en/kcontrol/smb/*.bz2
%doc %_docdir/HTML/en/kcontrol/smb/*.docbook
%dir %_docdir/HTML/en/kcontrol/useragent/
%doc %_docdir/HTML/en/kcontrol/useragent/*.bz2
%doc %_docdir/HTML/en/kcontrol/useragent/*.docbook
%dir %_docdir/HTML/en/kcontrol/windowmanagement/
%doc %_docdir/HTML/en/kcontrol/windowmanagement/*.bz2
%doc %_docdir/HTML/en/kcontrol/windowmanagement/*.docbook
%dir %_docdir/HTML/en/kdebugdialog/
%doc %_docdir/HTML/en/kdebugdialog/*.bz2
%doc %_docdir/HTML/en/kdebugdialog/*.docbook
%dir %_docdir/HTML/en/kcontrol/email/
%doc %_docdir/HTML/en/kcontrol/email/*.docbook
%dir %_docdir/HTML/en/kcontrol/energy/
%doc %_docdir/HTML/en/kcontrol/energy/*.bz2
%doc %_docdir/HTML/en/kcontrol/energy/*.docbook
%dir %_docdir/HTML/en/kcontrol/filemanager/
%doc %_docdir/HTML/en/kcontrol/filemanager/*.bz2
%doc %_docdir/HTML/en/kcontrol/filemanager/*.docbook
%doc %_docdir/HTML/en/kcontrol/filemanager/*.png
%dir %_docdir/HTML/en/kcontrol/filetypes/
%doc %_docdir/HTML/en/kcontrol/filetypes/*.bz2
%doc %_docdir/HTML/en/kcontrol/filetypes/*.docbook
%dir %_docdir/HTML/en/kcontrol/fonts/
%doc %_docdir/HTML/en/kcontrol/fonts/*.bz2
%doc %_docdir/HTML/en/kcontrol/fonts/*.docbook
%dir %_docdir/HTML/en/kcontrol/helpindex/
%doc %_docdir/HTML/en/kcontrol/helpindex/*.bz2
%doc %_docdir/HTML/en/kcontrol/helpindex/*.docbook
%dir %_docdir/HTML/en/kcontrol/icons/
%doc %_docdir/HTML/en/kcontrol/icons/*.bz2
%doc %_docdir/HTML/en/kcontrol/icons/*.docbook
%dir %_docdir/HTML/en/kcontrol/
%doc %_docdir/HTML/en/kcontrol/*.bz2
%doc %_docdir/HTML/en/kcontrol/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmaccess/
%doc %_docdir/HTML/en/kcontrol/kcmaccess/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmaccess/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmcss/
%doc %_docdir/HTML/en/kcontrol/kcmcss/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmcss/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmkonsole/
%doc %_docdir/HTML/en/kcontrol/kcmkonsole/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmkonsole/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmlaunch/
%doc %_docdir/HTML/en/kcontrol/kcmlaunch/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmlaunch/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmnotify/
%doc %_docdir/HTML/en/kcontrol/kcmnotify/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmnotify/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmsmserver/
%doc %_docdir/HTML/en/kcontrol/kcmsmserver/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmsmserver/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmstyle/
%doc %_docdir/HTML/en/kcontrol/kcmstyle/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmstyle/*.docbook
%dir %_docdir/HTML/en/kcontrol/kcmtaskbar/
%doc %_docdir/HTML/en/kcontrol/kcmtaskbar/*.bz2
%doc %_docdir/HTML/en/kcontrol/kcmtaskbar/*.docbook
%dir %_docdir/HTML/en/kcontrol/kdm/
%doc %_docdir/HTML/en/kcontrol/kdm/*.bz2
%doc %_docdir/HTML/en/kcontrol/kdm/*.docbook
%dir %_docdir/HTML/en/kcontrol/keyboard/
%doc %_docdir/HTML/en/kcontrol/keyboard/*.bz2
%dir %_docdir/HTML/en/kcontrol/background/
%doc %_docdir/HTML/en/kcontrol/background/*.bz2
%doc %_docdir/HTML/en/kcontrol/background/*.docbook
%dir %_docdir/HTML/en/kcontrol/bell/
%doc %_docdir/HTML/en/kcontrol/bell/*.bz2
%doc %_docdir/HTML/en/kcontrol/bell/*.docbook
%dir %_docdir/HTML/en/kcontrol/cache/
%doc %_docdir/HTML/en/kcontrol/cache/*.bz2
%doc %_docdir/HTML/en/kcontrol/cache/*.docbook
%dir %_docdir/HTML/en/kcontrol/clock/
%doc %_docdir/HTML/en/kcontrol/clock/*.bz2
%doc %_docdir/HTML/en/kcontrol/clock/*.docbook
%dir %_docdir/HTML/en/kcontrol/colors/
%doc %_docdir/HTML/en/kcontrol/colors/*.bz2
%doc %_docdir/HTML/en/kcontrol/colors/*.docbook
%dir %_docdir/HTML/en/kcontrol/cookies/
%doc %_docdir/HTML/en/kcontrol/cookies/*.bz2
%doc %_docdir/HTML/en/kcontrol/cookies/*.docbook
%dir %_docdir/HTML/en/kcontrol/crypto/
%doc %_docdir/HTML/en/kcontrol/crypto/*.bz2
%doc %_docdir/HTML/en/kcontrol/crypto/*.docbook
%dir %_docdir/HTML/en/kcontrol/desktop/
%doc %_docdir/HTML/en/kcontrol/desktop/*.bz2
%doc %_docdir/HTML/en/kcontrol/desktop/*.docbook
%dir %_docdir/HTML/en/kcontrol/desktopbehavior/
%doc %_docdir/HTML/en/kcontrol/desktopbehavior/*.bz2
%doc %_docdir/HTML/en/kcontrol/desktopbehavior/*.docbook
%dir %_docdir/HTML/en/kcontrol/ebrowsing/
%doc %_docdir/HTML/en/kcontrol/ebrowsing/*.bz2
%doc %_docdir/HTML/en/kcontrol/ebrowsing/*.docbook
%dir %_docdir/HTML/en/kcontrol/email/
%doc %_docdir/HTML/en/kcontrol/email/*.bz2
%dir %_docdir/HTML/en/faq/
%doc %_docdir/HTML/en/faq/*.bz2
%doc %_docdir/HTML/en/faq/*.docbook
%dir %_docdir/HTML/en/glossary/
%doc %_docdir/HTML/en/glossary/*.bz2
%doc %_docdir/HTML/en/glossary/*.docbook

#-----------------------------------------------------------------------------

%package konsole
Summary:	Konsole
Group:		Graphical desktop/KDE
Requires:	%name-common = %epoch:%version-%release
Requires:	%lib_name-konsole = %epoch:%version-%release
Provides:	konsole4
Requires: 	%name-progs = %epoch:%version-%release

%description konsole
A shell program similar to xterm for KDE

%post konsole
/sbin/ldconfig
# Laurent 3.80.3 reactivate it when it will official
#/usr/sbin/update-alternatives --install /usr/bin/xvt xvt /usr/bin/konsole 35

%postun konsole
/sbin/ldconfig
# Laurent 3.80.3 reactivate it when it will official
#if [ "$1" = "0" ]; then
#   /usr/sbin/update-alternatives --remove xvt /usr/bin/konsole
#fi

%files konsole
%defattr(-,root,root)
%_bindir/konsole
%dir %_datadir/apps/konsole/
%_datadir/apps/konsole/*
%_libdir/kde4/kcm_konsole.*
%_libdir/kde4/kickermenu_konsole.*
%_bindir/konsole-migrate.pl
%_libdir/kde4/libkonsolepart.*
%dir %_docdir/HTML/en/konsole/
%doc %_docdir/HTML/en/konsole/*.bz2
%doc %_docdir/HTML/en/konsole/*.docbook
%doc %_docdir/HTML/en/konsole/*.png


#-----------------------------------------------------------------------------

%package -n %lib_name-konsole
Summary:	Libraries for Konsole
Group:		Graphical desktop/KDE

%description -n %lib_name-konsole
Libraries for konsole program

%post -n %lib_name-konsole -p /sbin/ldconfig
%postun -n %lib_name-konsole -p /sbin/ldconfig

%files -n %lib_name-konsole
%defattr(-,root,root)
%_libdir/libkdeinit_konsole.*

#-----------------------------------------------------------------------------

%package kdeprintfax
Summary:	Kdeprintfax
Group:		Graphical desktop/KDE
Requires:	%name-progs = %epoch:%version-%release
Requires:	%name-common = %epoch:%version-%release
Provides:	kdeprintfax4
Requires:	enscript

%description kdeprintfax
Programm to send fax

%files kdeprintfax
%defattr(-,root,root)
%dir %_datadir/apps/kdeprintfax
%_datadir/apps/kdeprintfax/*
%_bindir/kdeprintfax
%_datadir/applications/kde4/kdeprintfax.desktop

#-----------------------------------------------------------------------------


%package -n %lib_name
Group:      Graphical desktop/KDE
Summary:    Libraries for kdebase
Requires:   kdelibs4-common 
Provides:   %lib_name_orig = %epoch:%version-%release
Requires:   %name-session-plugins

%description -n %lib_name
Libraries for the K Desktop Environment.

%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%files -n %lib_name
%defattr(-,root,root)
%_libdir/kde4/kded_kpasswdserver.so
%_libdir/kde4/solid_bluez.so
%_libdir/kde4/solid_networkmanager.so
%_libdir/libdolphinprivate.so.*
%_libdir/libkdeinit_knotify.so
%_libdir/libprocesscore.so.*
%_libdir/strigi/strigita_font.so

%_libdir/libprocessui.so.*
%_libdir/kde4/krunner_calculatorrunner.so
%_libdir/kde4/libfixhosturifilter.so
%_libdir/libkfontinstui.so.*
%_libdir/libkdeinit_kuiserver.so
%_libdir/libplasma.so.*
%_libdir/libkscreensaver.so.*
%_libdir/libkworkspace.so.*
%_libdir/kde4/konq_part.so
%_libdir/kde4/libexec/test_kcm_xinerama
%_libdir/kde4/libkcminit_nsplugin.so
%_libdir/kde4/libkfindpart.so
%_libdir/kde4/solid_hal_discovery.so
%_libdir/kde4/solid_hal_power.so
%_libdir/kde4/svgthumbnail.so
%_libdir/kde4/taskbar_panelapplet.so
%_libdir/libkdeinit_ksysguard.so
%_libdir/libkdeinit_kwin_rules_dialog.so
%_libdir/kde4/kio_*
%_libdir/libkdeinit_kprinter.so
%_libdir/libkickermain.so.*
%_libdir/libkonqsidebarplugin.so.*
%_libdir/libkonq.so.*
%_libdir/libksgrd.so.*
%_libdir/libtaskbar.so.*
%_libdir/libtaskmanager.so.*
%_libdir/libkdeinit_khelpcenter.so
%_libdir/libkdeinit_kinfocenter.so
%_libdir/libkdeinit_appletproxy.so
%_libdir/libkdeinit_kdesktop.so
%_libdir/libkdeinit_keditbookmarks.so
%_libdir/libkdeinit_kfmclient.so
%_libdir/libkdeinit_khotkeys.so
%_libdir/libkdeinit_kicker.so
%_libdir/libkdeinit_kjobviewer.so
%_libdir/libkdeinit_klipper.so
%_libdir/libkdeinit_konqueror.so
%_libdir/libkdeinit_ksmserver.so
%_libdir/libkdeinit_kwin.so
%_libdir/libkdeinit_kwrite.so
%_libdir/libkdeinit_kxkb.so
%_libdir/libkdeinit_kcontrol.so
%_libdir/libkdeinit_kcminit.so
%_libdir/libkdeinit_kaccess.so
%_libdir/libkdecorations.so.*
%_libdir/libkdeinit_kcontroledit.so
%_libdir/libkfontinst.so.*
%_libdir/libkdeinit_kcminit_startup.so
%_libdir/libkdeinit_kcmshell.so
%_libdir/kde4/krunner_searchrunner.so
%_libdir/kde4/kxkb_panelapplet.so
%_libdir/kde4/kded_homedirnotify.so
%_libdir/kde4/kded_medianotifier.so
%_libdir/kde4/exrthumbnail.so
%_libdir/kde4/kded_khotkeys.so
%_libdir/kde4/kded_mediamanager.so
%_libdir/kde4/kded_remotedirnotify.so
%_libdir/kde4/kded_systemdirnotify.so
%_libdir/kde4/kickermenu_remotemenu.so
%_libdir/kde4/kickermenu_systemmenu.so
%_libdir/kde4/kwin3_plastik.so
%_libdir/kde4/kwin_plastik_config.so
%_libdir/kde4/libkhtmlkttsdplugin.so
%_libdir/kde4/media_panelapplet.so
%_libdir/kde4/trash_panelapplet.so
%_libdir/kde4/libkfontviewpart.so
%_libdir/kde4/sidebar_panelextension.so

%dir %_libdir/kconf_update_bin/
%_libdir/kconf_update_bin/khotkeys_update
%_libdir/kconf_update_bin/kwin_update_window_settings
%_libdir/kconf_update_bin/kicker-3.4-reverseLayout
%_libdir/kconf_update_bin/kwin_update_default_rules


%_libdir/kde4/cursorthumbnail.so
%_libdir/kde4/djvuthumbnail.so
%_libdir/kde4/kded_konqy_preloader.so
%_libdir/kde4/kickermenu_find.so
%_libdir/kde4/konqsidebar_web.so
%_libdir/kde4/kwin3_default.so
%_libdir/kde4/kwin3_keramik.so
%_libdir/kde4/kwin3_laptop.so
%_libdir/kde4/kwin3_modernsys.so
%_libdir/kde4/kwin3_redmond.so
%_libdir/kde4/kwin3_b2.so
%_libdir/kde4/kwin3_quartz.so
%_libdir/kde4/kwin3_web.so
%_libdir/kde4/kwin_b2_config.so
%_libdir/kde4/kwin_quartz_config.so
%_libdir/kde4/kwin_default_config.so
%_libdir/kde4/kwin_keramik_config.so
%_libdir/kde4/kwin_modernsys_config.so
%_libdir/kde4/menu_panelapplet.so
%_libdir/kde4/kstyle_keramik_config.so
%_libdir/kde4/kcm_*
%exclude %_libdir/kde4/kcm_konsole.*
%exclude %_libdir/kde4/kcm_nsplugins.*
%_libdir/kde4/kded_kwrited.so
%_libdir/kde4/kickermenu_konqueror.so
%_libdir/kde4/konq_remoteencoding.so
%_libdir/kde4/liblocaldomainurifilter.so
%_libdir/kde4/dockbar_panelextension.so*
%_libdir/kde4/htmlthumbnail.so
%_libdir/kde4/imagethumbnail.so
%_libdir/kde4/kickermenu_kdeprint.so
%_libdir/kde4/klipper_panelapplet.so
%_libdir/kde4/konq_aboutpage.so
%_libdir/kde4/konq_shellcmdplugin.so
%_libdir/kde4/konq_sidebar.so
%_libdir/kde4/konq_sidebartree_bookmarks.so
%_libdir/kde4/konq_sidebartree_dirtree.so
%_libdir/kde4/konq_sidebartree_history.so
%_libdir/kde4/konqsidebar_tree.so
%_libdir/kde4/konq_sound.so
%_libdir/kde4/launcher_panelapplet.so*
%_libdir/kde4/libkdeprint_part.so
%_libdir/kde4/libkshorturifilter.so
%_libdir/kde4/libkuriikwsfilter.so
%_libdir/kde4/libkurisearchfilter.so
%_libdir/kde4/lockout_panelapplet.so*
%_libdir/kde4/naughty_panelapplet.so*
%_libdir/kde4/run_panelapplet.so*
%_libdir/kde4/sysguard_panelapplet.so*
%_libdir/kde4/systemtray_panelapplet.so*
%_libdir/kde4/textthumbnail.so
%_libdir/kde4/kded_favicons.so
%_libdir/kde4/fontthumbnail.so
%_libdir/kde4/kickermenu_prefmenu.so
%_libdir/kde4/kickermenu_recentdocs.so
%_libdir/kde4/libkmanpart.so

#-----------------------------------------------------------------------------

%package    common
Group:      Graphical desktop/KDE
Summary:    Config file and icons file for %name.
PreReq:     %lib_name = %epoch:%version-%release
# Laurent 3.80.3 reactivate it
Provides:	webclient4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description common
This packages contains all icons, config file etc...

%post common

# Laurent readd it after moving
#(
#cd %_datadir/fonts/
#/usr/bin/fc-cache -f . 
#)
%{update_desktop_database}
%update_icon_cache crystalsvg

%postun common
%{clean_desktop_database}
%clean_icon_cache crystalsvg

%files common
%defattr(-,root,root)
#/etc/profile.d/kde3.sh
#%dir %_sysconfdir/X11/wmsession.d/
#%_sysconfdir/X11/wmsession.d/*KDE
%config(noreplace) %_sysconfdir/ksysguarddrc 
#

%_datadir/apps/desktoptheme/default/background/dialog.svg


/etc/X11/wmsession.d/10KDE4

%_sysconfdir/xdg/menus/*.menu


%if %mdkversion > 200600
#%dir %_sysconfdir/xdg/kde
#%_sysconfdir/xdg/kde/menus/*.menu
#%dir %_sysconfdir/xdg/kde/menus/applications-merged/
#%_sysconfdir/xdg/kde/menus/applications-merged/*.menu
%endif

%config(noreplace) /etc/pam.d/kde4
%config(noreplace) /etc/pam.d/kscreensaver4
%config(noreplace) /etc/pam.d/kde4-np
#
#
%config(noreplace) %_datadir/config/kdesktop_custom_menu1
%config(noreplace) %_datadir/config/kdesktop_custom_menu2
%config(noreplace) %_datadir/config/konqsidebartng.rc
%config(noreplace) %_datadir/config/kshorturifilterrc

#

%_bindir/kbookmarkmerger
%_bindir/kcheckrunning
%_bindir/khc_docbookdig.pl
%_bindir/khc_htdig.pl
%_bindir/khc_htsearch.pl
%_bindir/khc_mansearch.pl
%_bindir/kio_media_mounthelper
%_bindir/knetattach
%_bindir/ktrash

%_datadir/apps/khtml/kpartplugins/*.desktop
%_datadir/apps/khtml/kpartplugins/*.rc

%_datadir/apps/desktoptheme/default/background/shutdowndlgbuttonglow.svg
%_datadir/apps/kde/kde.notifyrc
%_datadir/apps/kfontinst/bin/kfontprint
%_datadir/apps/kfontinst/icons/oxygen/scalable/actions/disablefont.svgz
%_datadir/apps/kfontinst/icons/oxygen/scalable/actions/enablefont.svgz
%_iconsdir/oxygen/scalable/mimetypes/fonts-folder.svgz
%_iconsdir/oxygen/scalable/mimetypes/fonts-package.svgz
%_iconsdir/oxygen/scalable/mimetypes/fonts-system-folder.svgz

%_datadir/apps/kfontview/kfontviewui.rc
%_datadir/apps/ksplash/Themes/Default/1600x1200/*
%_datadir/apps/ksplash/Themes/Default/Preview.png
%_datadir/apps/ksplash/Themes/Default/Theme.rc
%_datadir/apps/ksplash/Themes/None/Theme.rc
%_datadir/apps/ksplash/Themes/Simple/Preview.png
%_datadir/apps/ksplash/Themes/Simple/Theme.rc
%_datadir/config/background.knsrc

#

%dir %_datadir/desktop-directories/
%_datadir/desktop-directories/*.directory


%dir %_datadir/apps/kinfocenter/
%_datadir/apps/kinfocenter/kinfocenterui.rc

%_datadir/apps/kuiserver/icons/crystalsvg/16x16/apps/kio_uiserver.png


%_datadir/apps/kfontinst/icons/crystalsvg/*
%_datadir/apps/kfontinst/kfontviewpart.rc

%_datadir/apps/konqpart/konq_iconview.rc
%_datadir/apps/konqpart/konq_listview.rc

%_datadir/apps/Settingsmenu/printmgr.desktop
#
%dir %_datadir/config.kcfg/
%_datadir/config.kcfg/*.kcfg
%dir %_datadir/apps/
%dir %_datadir/apps/kthememanager/themes/
%_datadir/apps/kthememanager/themes/*
%dir %_datadir/apps/kcontroledit/
%_datadir/apps/kcontroledit/*
%dir %_datadir/apps/drkonqi/
%_datadir/apps/drkonqi/*
%dir %_datadir/apps/kappfinder/
%_datadir/apps/kappfinder/*
%exclude %_datadir/apps/kappfinder/apps/Games/Roguelikes/*.desktop
%exclude %_datadir/apps/kappfinder/apps/Games/Arcade/*.desktop
%dir %_datadir/apps/kbookmark/
%_datadir/apps/kbookmark/*
%dir %_datadir/apps/kcmcss/
%_datadir/apps/kcmcss/*
%dir %_datadir/apps/kcminput/
%_datadir/apps/kcminput/*
%dir %_datadir/apps/kcmkeys
%_datadir/apps/kcmkeys/*
%dir %_datadir/apps/kcmlocale/
%_datadir/apps/kcmlocale/*
%dir %_datadir/apps/khotkeys/
%_datadir/apps/khotkeys/*
%dir %_datadir/apps/kcontrol/
%_datadir/apps/kcontrol/*
%dir %_datadir/apps/kconf_update/
%_datadir/apps/kconf_update/*.upd
%_datadir/apps/kconf_update/*.pl
%_datadir/apps/kconf_update/*.sh
%dir %_datadir/apps/kcm_componentchooser
%_datadir/apps/kcm_componentchooser/*
%dir %_datadir/apps/kdeprint_part
%_datadir/apps/kdeprint_part/*
%dir %_datadir/apps/kdeprint
%_datadir/apps/kdeprint/*
%dir %_datadir/apps/kdesktop
%_datadir/apps/kdesktop/*
%dir %_datadir/apps/kdewizard
%_datadir/apps/kdewizard/*
%dir %_datadir/apps/kdisplay
%_datadir/apps/kdisplay/*
%dir %_datadir/apps/keditbookmarks/
%_datadir/apps/keditbookmarks/*
%dir %_datadir/apps/khelpcenter/
%_datadir/apps/khelpcenter/*
%dir %_datadir/apps/kicker
%_datadir/apps/kicker/*
%dir %_datadir/apps/kio_finger/
%_datadir/apps/kio_finger/*
%dir %_datadir/apps/kio_info/
%_datadir/apps/kio_info/*
%dir %_datadir/apps/kjobviewer/
%_datadir/apps/kjobviewer/*
%dir %_datadir/apps/konqiconview/
%_datadir/apps/konqiconview/*
%dir %_datadir/apps/konqlistview/
%_datadir/apps/konqlistview/*
%dir %_datadir/apps/konqsidebartng/
%_datadir/apps/konqsidebartng/*
%dir %_datadir/apps/konqueror/
%_datadir/apps/konqueror/*
%dir %_datadir/apps/ksysguard/
%_datadir/apps/ksysguard/*
%dir %_datadir/apps/kthememgr/
%_datadir/apps/kthememgr/*
%dir %_datadir/apps/kwin/
%_datadir/apps/kwin/*
%dir %_datadir/apps/kwrite/
%_datadir/apps/kwrite/*
%dir %_datadir/apps/kaccess
%_datadir/apps/kaccess/*
%_datadir/apps/kio_man/kio_man.css
%dir %_datadir/apps/ksmserver
%_datadir/apps/ksmserver/*
%dir %_datadir/apps/naughtyapplet/
%_datadir/apps/naughtyapplet/*
%dir %_datadir/autostart/
%_datadir/autostart/*
%_iconsdir/*/*/actions/*
%_iconsdir/*/*/apps/*
%_iconsdir/*/*/devices/*
%_datadir/locale/en_US
%_datadir/locale/l10n/*
%dir %_datadir/mdk/
%dir %_datadir/mdk/kde
%_datadir/mdk/kde/*desktop
%_datadir/mdk/kde/*.directory
%dir %_datadir/mdk/kde/root-interface/
%_datadir/mdk/kde/root-interface/*
%dir %_datadir/mdk/kde/scripts/
%dir %_datadir/mdk/kde/scripts/env
%dir %_datadir/mdk/kde/scripts/shutdown/
%_datadir/applications/kde4/*
%exclude %_datadir/applications/kde4/kdeprintfax.desktop
%dir %_datadir/apps/kcmusb
%_datadir/apps/kcmusb/*
%dir %_datadir/apps/systemview
%_datadir/apps/systemview/*
%dir %_datadir/mimelnk/
%dir %_datadir/mimelnk/application
%_datadir/mimelnk/application/*
%dir %_datadir/mimelnk/media
%_datadir/mimelnk/media/*
%dir %_datadir/mimelnk/print/
%_datadir/mimelnk/print/*
%dir %_datadir/mimelnk/inode/
%_datadir/mimelnk/inode/system_directory.desktop
%dir %_datadir/kde4/services
%_datadir/kde4/services/*
%dir %_datadir/kde4/servicetypes/
%_datadir/kde4/servicetypes/*
%dir %_datadir/sounds/
%_datadir/sounds/*
%dir %_datadir/templates/
%_datadir/templates/*
%_datadir/templates/.source
%dir %_datadir/wallpapers/
%_datadir/wallpapers/*
%dir %_datadir/apps/kcmview1394/
%_datadir/apps/kcmview1394/oui.db

# Don't autostart ktip
%exclude %_datadir/autostart/ktip.desktop
# Not on desktop
%exclude %_datadir/apps/kdesktop/DesktopLinks/System.desktop

#-----------------------------------------------------------------------------

%package  -n %lib_name-devel
Summary:	Devel stuff for kdebase
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%lib_name = %epoch:%version-%release 
Provides:	%name-devel = %epoch:%version-%release

%description  -n %lib_name-devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files -n %lib_name-devel
%defattr(-,root,root)
%_libdir/libplasma.so
%_libdir/libkfontinstui.so
%dir %_includedir/Plasma/
%_includedir/Plasma/*
%_includedir/*.h
%dir %_includedir/ksysguard/
%_includedir/ksysguard/*.h
%dir %_includedir/ksgrd
%_includedir/ksgrd/*.h
%_libdir/libkickermain.so
%_libdir/libkonqsidebarplugin.so
%_libdir/libkonq.so
%_libdir/libksgrd.so
%_libdir/libtaskbar.so
%_libdir/libtaskmanager.so
%_libdir/libkdecorations.so
%_libdir/libkfontinst.so

%_libdir/libdolphinprivate.so
%_libdir/libprocesscore.so
%_libdir/libprocessui.so
%_libdir/kde4/plugins/designer/ksysguardwidgets.so

%_libdir/libkscreensaver.so
%_libdir/libkworkspace.so


%_datadir/apps/cmake/modules/*.cmake
%dir %_includedir/libworkspace/
%_includedir/libworkspace/*.h
%dir %_includedir/plasma/
%_includedir/plasma/*.h

%_datadir/dbus-1/interfaces/*.xml

#-----------------------------------------------------------------------------

%package nsplugins
Summary:	Netscape Plugins for kdebase
Group:		Graphical desktop/KDE
Requires:	%name-progs = %epoch:%version-%release

%description nsplugins
This package contains the Netscape plugins for konqueror files.

%files nsplugins
%defattr(-,root,root)
%_bindir/nspluginscan
%_bindir/nspluginviewer
%_datadir/apps/plugin/nspluginpart.rc
%_libdir/kde4/kcm_nsplugins.*


#-----------------------------------------------------------------------------

%package session-plugins
Summary:    Session plugins for kdesktop/kdm
Group:      Graphical desktop/KDE

%description session-plugins
This package contains sessions plugins for kdesktop kdm.
It allows to login into with kdm and lock/unlock kdesktop screensaver.


%files session-plugins
%defattr(-,root,root)
%_libdir/kde4/kgreet_winbind.so
%_libdir/kde4/kgreet_classic.so


%package kdm
Summary:    kdm for kdebase
Group:      Graphical desktop/KDE
Requires:	kdm-config-file
Provides:	kdm4
Requires:	xinitrc
Requires:	%name-session-plugins

%description kdm
This package contains kdm.

%post kdm
%make_session

%files kdm
%defattr(-,root,root)
%_bindir/kdm
%_bindir/kdmctl
%_bindir/kdm_config
%_bindir/kdm_greet
%_bindir/krootimage
%_bindir/genkdmconf
%_datadir/apps/doc/kdm/README
%dir %_datadir/apps/kdm
%_datadir/apps/kdm/*

#-----------------------------------------------------------------------------

%package kmenuedit
Summary:    kmenuedit 
Group:      Graphical desktop/KDE
Provides:	kmenuedit4
Requires:   %lib_name-kmenuedit = %epoch:%version-%release

%description kmenuedit
Kmenuedit for kdebase

%files kmenuedit
%defattr(-,root,root)
%_bindir/kmenuedit
%dir %_datadir/apps/kmenuedit/
%_datadir/apps/kmenuedit/*

%_datadir/apps/kmenuedit/icons/crystalsvg/22x22/actions/menu_new.png
%_datadir/apps/kmenuedit/icons/crystalsvg/22x22/actions/menu_new_sep.png
%_datadir/apps/kmenuedit/icons/crystalsvg/32x32/actions/menu_new.png
%_datadir/apps/kmenuedit/icons/crystalsvg/32x32/actions/menu_new_sep.png
%_datadir/apps/kmenuedit/icons/locolor/16x16/actions/menu_new.png
%_datadir/apps/kmenuedit/kmenueditui.rc

%dir %_docdir/HTML/en/kmenuedit/
%doc %_docdir/HTML/en/kmenuedit/*.bz2
%doc %_docdir/HTML/en/kmenuedit/*.docbook
%doc %_docdir/HTML/en/kmenuedit/*.png

#-----------------------------------------------------------------------------

%package -n %lib_name-kmenuedit
Summary:    Library for KMenuedit for kdebase
Group:      Graphical desktop/KDE

%description -n %lib_name-kmenuedit
Library for Kmenuedit for kdebase

%post -n %lib_name-kmenuedit -p /sbin/ldconfig
%postun -n %lib_name-kmenuedit -p /sbin/ldconfig

%files -n %lib_name-kmenuedit
%defattr(-,root,root)
%_libdir/libkdeinit_kmenuedit.*

#-----------------------------------------------------------------------------

%prep
%setup -q -nkdebase-%version-%branch_date 
#(
#cd workspace/ksplashml/
#tar -xvf %SOURCE30000
#)

%patch1000 -p1 -b .startkde
#%patch1001 -p1 -b .add_mdv_splashscreen

# Mandriva menu support
#%patch2 -p1 -b .xdg
#%patch3 -p1 -b .splash
#%patch7 -p1 -b .startkde_mdk
#%patch14 -p1 -b .konqueror_default_profile_webbrowsing
#%patch16 -p1 -b .fix_konsole_paste_action
#%patch24 -p1 -b .remove_help_entry_kdesktop
#%patch25 -p1 -b .increase_kicker_size
#%patch32 -p1 -b .dont_use_strict_info2html
#%patch37 -p1 -b .desktop_button_icon_mdk
#%patch39 -p1 -b .krun_icon
#%patch40 -p1 -b .fix_media_fuser_path
#%patch42 -p0 -b .fix_about_mandrake
#%patch43 -p1 -b .add_multimedia_keyboard_to_konqueror
#%patch48 -p0 -b .merge_mdk_dir
#%patch49 -p1 -b .fix_screensaver
#%patch50 -p1 -b .fix_arts_mdk_bug_11671
#%patch51 -p1 -b .fix_kfileivi_crash
#%patch62 -p0 -b .fix_vibrate_dialog
#%patch65 -p1 -b .fix_kde_bug_15327
#%patch66 -p1 -b .fix_mdk_bug_16007
#%patch71 -p1 -b .fix_kthememanager_name
#%patch73 -p1 -b .add_mdv_device
#%patch75 -p1 -b .kwintheme
#%patch76 -p1 -b .fix_mdkfirsttime
#%patch80 -p1 -b .fix_kdesktop_wrap_crash
#%patch82 -p1 -b .startkde_align_icons
#%patch83 -p1 -b .fix_detect_nfts_partition
#%patch85 -p1 -b .xinerama
#%patch92 -p1 -b .startkde_move_menu_dir
#%patch89 -p1 -b .install_kde_script
#%patch90 -p1 -b .dont_autostart_klipper
#%patch93 -p1 -b .crypto
#%patch96 -p1 -b .fix_kthemenamager_disable_button
#%patch101 -p1 -b .only_show_desktop_under_kde
#%patch125 -p1 -b .rubberband
#%patch126 -p1 -b .rubberbandkcm
#%patch145 -p1 -b .fix_kdm_theme
#%patch147 -p1 -b .fix_kdm_server_args
#%patch148 -p1 -b .fix_logout_without_confirmation
#%patch149 -p1 -b .by_default_aa
#%patch150 -p0 -b .kdeeject
#%patch151 -p0 -b .bookmarks
#%patch152 -p1 -b .fix_old_icons_pos
#%patch154 -p1 -b .fix_mnt_mount_point
#%patch155 -p1 -b .fix_gtk_style
#%patch156 -p1 -b .fix_kdeeject
#%patch158 -p1 -b .fix_kscreensaver_only_show_in_kde
#%patch159 -p1 -b .fix_nsplugins_x86_64
#%patch160 -p1 -b .fix_kicker_kthememanager
#%patch161 -p1 -b .fix_nsplugins_reset_to_default_path
#%patch163 -p1 -b .fix_dbus_kmediamanager

%build
cd $RPM_BUILD_DIR/kdebase-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdebase-%version-%branch_date
cd build

make DESTDIR=%buildroot install


# Install kde pam configuration file
# David - 3.0-0.beta1.8mdk - We don't use the _sysconfdir macro as long as we
#                            install KDE 3 in /opt/kde3/
install -d -m 0755 %buildroot/etc/pam.d/
install -m 0644 %SOURCE11 %buildroot/etc/pam.d/kde4
install -m 0644 %SOURCE1002 %buildroot/etc/pam.d/kde4-np

# Install kscreensaver pam configuration file
install -m 0644 $RPM_BUILD_DIR/kdebase-%version-%branch_date/workspace/kscreensaver.pamd %buildroot/etc/pam.d/kscreensaver4

# LMDK config files
install -d -m 0775 %buildroot/%_datadir/config/
#install -m 0644 %SOURCE100000 %buildroot/%_datadir/apps/kdesktop/DesktopLinks/device.desktop
#install -m 0644 %SOURCE100001 %buildroot/%_datadir/services/devices.protocol

install -d -m 0775 %buildroot/%_datadir/apps/kthememgr/Themes/
install -m 0644 %SOURCE5100 %buildroot/%_datadir/apps/kthememgr/Themes/Galaxy.ktheme


# Root's desktop configuration
# David - 2.2-61mdk - Root interface
install -d -m 0755 %buildroot/%_datadir/mdk/kde/
cd %buildroot/%_datadir/mdk/kde/
tar jxf %SOURCE155

install -d -m 0755 %buildroot/%_datadir/mdk/kde/scripts/
install -d -m 0755 %buildroot/%_datadir/mdk/kde/scripts/env/
install -d -m 0755 %buildroot/%_datadir/mdk/kde/scripts/shutdown/


# Scripts for Desktop configuration
# David - 2.1.1-4mdk - To be able to use "Preferences" in K menu (right click
#                      on K menu -> Preferences)
install -m 0755 %SOURCE253 %buildroot/%_bindir/kmenu-preferences-switch

install -m 0755 %SOURCE300 %buildroot/%_bindir/kdesktop-links
install -m 0755 %SOURCE301 %buildroot/%_bindir/ArrangeIcons

install -m 0755 %SOURCE302 %buildroot/%_bindir/test-windows-key

install -m 0755 %SOURCE303 %buildroot/%_bindir/kdesktop-network

install -m 0755 %SOURCE305 %buildroot/%_bindir/openkmenu
install -m 0644 %SOURCE306 %buildroot/%_datadir/mdk/kde/openkmenu.desktop


# Default icons for Desktop
install -d %buildroot/%_datadir/mdk/kde/
install -m 0644 %SOURCE400 %buildroot/%_datadir/mdk/kde/ArangeIcons.desktop
install -m 0644 %SOURCE401 %buildroot/%_datadir/mdk//kde/CD-ROM.desktop
install -m 0644 %SOURCE402 %buildroot/%_datadir/mdk/kde/CD-ROM2.desktop
install -m 0644 %SOURCE403 %buildroot/%_datadir/mdk/kde/Mandriva\ Control\ Center.desktop
install -m 0644 %SOURCE404 %buildroot/%_datadir/mdk/kde/Documentation-de.desktop
install -m 0644 %SOURCE405 %buildroot/%_datadir/mdk/kde/Documentation-es.desktop
install -m 0644 %SOURCE406 %buildroot/%_datadir/mdk/kde/Documentation-fr.desktop
install -m 0644 %SOURCE407 %buildroot/%_datadir/mdk/kde/Documentation-it.desktop
install -m 0644 %SOURCE408 %buildroot/%_datadir/mdk/kde/Documentation.desktop
install -m 0644 %SOURCE409 %buildroot/%_datadir/mdk/kde/Floppy.desktop
%ifnarch ppc
install -m 0644 %SOURCE410 %buildroot/%_datadir/mdk/kde/Floppy2.desktop
%else
install -m 0644 %SOURCE424 %buildroot/%_datadir/mdk/kde/Floppy2.desktop
%endif
install -m 0644 %SOURCE412 %buildroot/%_datadir/mdk/kde/Mandriva\ Expert.desktop
install -m 0644 %SOURCE413 %buildroot/%_datadir/mdk/kde/Mandriva\ News.desktop
install -m 0644 %SOURCE414 %buildroot/%_datadir/mdk/kde/Mandriva\ Store.desktop
install -m 0644 %SOURCE415 %buildroot/%_datadir/mdk/kde/Printer-kprinter.desktop
install -m 0644 %SOURCE416 %buildroot/%_datadir/mdk/kde/Printer-kups.desktop
install -m 0644 %SOURCE417 %buildroot/%_datadir/mdk/kde/Printer-lpr.desktop
install -m 0644 %SOURCE418 %buildroot/%_datadir/mdk/kde/Printer-qtcups.desktop
install -m 0644 %SOURCE419 %buildroot/%_datadir/mdk/kde/Printer-xpp.desktop
install -m 0644 %SOURCE420 %buildroot/%_datadir/mdk/kde/XKill.desktop
install -m 0644 %SOURCE421 %buildroot/%_datadir/mdk/kde/Zip.desktop
install -m 0644 %SOURCE422 %buildroot/%_datadir/mdk/kde/Zip2.desktop
install -m 0644 %SOURCE423 %buildroot/%_datadir/mdk/kde/directory-desktop
install -m 0644 %SOURCE425 %buildroot/%_datadir/mdk/kde/Connection-to-Internet.desktop
install -m 0644 %SOURCE426 %buildroot/%_datadir/mdk/kde/Connection-to-Internet2.desktop
install -m 0644 %SOURCE427 %buildroot/%_datadir/mdk/kde/MandrivaClub.desktop
install -m 0644 %SOURCE428 %buildroot/%_datadir/mdk/kde/removable_media.directory


install -d -m 0755 %buildroot/%_datadir/mimelnk/
install -d -m 0755 %buildroot/%_datadir/mimelnk/media/
install -m 0644 %SOURCE200022 %buildroot/%_datadir/mimelnk/media/hdd_win_mounted.desktop
install -m 0644 %SOURCE200023 %buildroot/%_datadir/mimelnk/media/hdd_win_unmounted.desktop


# David - 3.0.3-67mdk - Make FB happy - Icon for MDK documentation in kicker
install -m 0755 %SOURCE3100 %buildroot/%_bindir/mdkdoc-kicker

install -m 0644 %SOURCE2 %buildroot/%_bindir/


# Add chksession support
# David - 3.0-0.beta1.8mdk - We don't use the _sysconfdir macro here because
#                            this file need to be installed in /etc/ and not
#                            in /opt/kde3/etc/ (or KDE 3 will not be displayed
#                            in KDM/GDM.
#                            We will also need to rename 11KDE in 01KDE when
#                            KDE 3 will be used as default KDE.
install -d -m 0775 %buildroot/etc/X11/wmsession.d/
cat << EOF > %buildroot/etc/X11/wmsession.d/10KDE4
NAME=KDE4
ICON=kde-wmsession.xpm
DESC=The K Desktop Environment
EXEC=%_bindir/startkde
SCRIPT:
exec %_bindir/startkde
EOF


# David - 2.1-0.20010210.1mdk - Change kdesud owners and permission (per request
#                               of binary)
# David - 2.1-1mdk - It seems that Coolo made some modifications in Makefile to
#                    set that automatically in KDE post 2.1. To check in next
#                    CVS code update
#TODO
#chmod 2755 %buildroot/%_bindir/kdesud
#chmod 4755 %buildroot/%_bindir/kcheckpass 

# Laurent - 2.2.1-2mdk - Add an icon to adressbook
#perl -pi -e "s|Icon=kadressbook|Icon=addressbook_section.png|" %buildroot/%_datadir/applnk/Utilities/kaddressbook.desktop

# David - 2.2.2-17mdk - Provide icon for socks menu entry
#perl -pi -e "s|Icon=socks|Icon=network|" %buildroot/%_datadir/applnk/Settings/Network/socks.desktop


#=============================================# 
#             Mandriva menu support           #
#=============================================#

## Mandriva menu support
# Laurent - 3.0-0.beta1.7mdk - Don't install menu-method into /opt/kde3/etc
#                              To remove when KDE 3 will be installed in /usr
#install -d -m 0755 %buildroot/etc/menu-methods/
##install -m 0755 %SOURCE200 %buildroot/etc/menu-methods/kde3

install -m 0775 %SOURCE20001 %buildroot/%_bindir/konsole-migrate.pl
install -m 0775 %SOURCE20002 %buildroot/%_bindir/kicker-migrate.pl
install -m 0775 %SOURCE20003 %buildroot/%_bindir/www-browser-convert.pl

install -m 0755 %SOURCE70000 %buildroot/%_bindir/alignment-icons
install -m 0644 %SOURCE70001 %buildroot/%_datadir/mdk/kde/alignment-icons.desktop






mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/Help.desktop "More Applications/Documentation" kde

perl -pi -e 's|Icon=.*|Icon=home-mdk|' %buildroot/%_datadir/applications/kde/Home.desktop
####FIXME 
mandriva-add-xdg-categories.pl  %buildroot/%_datadir/applications/kde/Home.desktop .hidden kde
#mandriva-add-xdg-categories.pl  Configuration %buildroot/%_datadir/applications/kde/KControl.desktop %buildroot/%_menudir/kdebase-kcontrol kde
# David - 3.1-49mdk - To display Kcontrol by default
#
#perl -pi -e 's|Icon=.*|Icon=find-files-mdk|' %buildroot/%_datadir/applications/kde/Kfind.desktop
#mandriva-add-xdg-categories.pl  "System/File Tools" %buildroot/%_datadir/applications/kde/Kfind.desktop %buildroot/%_menudir/kdebase-kfind kde





# %%_datadir/applnk/Editors/
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/kwrite.desktop "More Applications/Editors" 


# %%_datadir/applnk/Internet
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/konqbrowser.desktop  "Internet/Web Browsers" 


# %%_datadir/applnk/Settings/Accessibility/
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Accessibility %buildroot/%_datadir/applications/kde/kcmaccess.desktop %buildroot/%_menudir/kdebase-kcmaccess kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Accessibility %buildroot/%_datadir/applications/kde/keys.desktop %buildroot/%_menudir/kdebase-keys kde
# David - 3.1-45mdk - Don't creat child entry in Kcontrol
#perl -pi -e "s|/| - |g;s|DocPath=.*|DocPath=kcontrol/language/index.html|" %buildroot/%_datadir/applications/kde/language.desktop
#
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Accessibility %buildroot/%_datadir/applications/kde/language.desktop %buildroot/%_menudir/kdebase-language kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Accessibility %buildroot/%_datadir/applications/kde/keyboard_layout.desktop %buildroot/%_menudir/kdebase-keyboard-layout kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/componentchooser.desktop %buildroot/%_menudir/kdebase-componentchooser kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/filebrowser.desktop %buildroot/%_menudir/kdebase-filebrowser kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/filetypes.desktop %buildroot/%_menudir/kdebase-filetypes kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/kcmkded.desktop %buildroot/%_menudir/kdebase-kcmkded kde
#perl -pi -e "s|kded.png|misc.png|" %buildroot/%_menudir/kdebase-kcmkded
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/kcmsmserver.desktop %buildroot/%_menudir/kdebase-kcmsmserver kde
#perl -pi -e "s|smserver.png|misc.png|" %buildroot/%_menudir/kdebase-kcmsmserver

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Components %buildroot/%_datadir/applications/kde/spellchecking.desktop %buildroot/%_menudir/kdebase-spellchecking kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/desktopbehavior.desktop %buildroot/%_menudir/kdebase-desktopbehavior kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/desktop.desktop %buildroot/%_menudir/kdebase-desktop kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/kcmtaskbar.desktop %buildroot/%_menudir/kdebase-kcmtaskbar kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/kwinoptions.desktop %buildroot/%_menudir/kdebase-kwinoptions kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/panel.desktop %buildroot/%_menudir/kdebase-panel kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/devices.desktop %buildroot/%_menudir/kdebase-devices kde


#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/opengl.desktop %buildroot/%_menudir/kdebase-opengl kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/dma.desktop %buildroot/%_menudir/kdebase-dma kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/interrupts.desktop %buildroot/%_menudir/kdebase-interrupts kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/ioports.desktop %buildroot/%_menudir/kdebase-ioports kde
# David - 2.2-0.beta1.1mdk - To fix
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/ioslaveinfo.desktop %buildroot/%_menudir/kdebase-ioslaveinfo kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/kcmusb.desktop %buildroot/%_menudir/kdebase-kcmusb kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/memory.desktop %buildroot/%_menudir/kdebase-memory kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/nic.desktop %buildroot/%_menudir/kdebase-nic kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/partitions.desktop %buildroot/%_menudir/kdebase-partitions kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/pci.desktop %buildroot/%_menudir/kdebase-pci kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/processor.desktop %buildroot/%_menudir/kdebase-processor kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/scsi.desktop %buildroot/%_menudir/kdebase-scsi kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/smbstatus.desktop %buildroot/%_menudir/kdebase-smbstatus kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/sound.desktop %buildroot/%_menudir/kdebase-sound kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Information %buildroot/%_datadir/applications/kde/xserver.desktop %buildroot/%_menudir/kdebase-xserver kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/background.desktop %buildroot/%_menudir/kdebase-background kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/colors.desktop %buildroot/%_menudir/kdebase-colors kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/fonts.desktop %buildroot/%_menudir/kdebase-fonts kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/icons.desktop %buildroot/%_menudir/kdebase-icons kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/kcmlaunch.desktop %buildroot/%_menudir/kdebase-kcmlaunch kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/kwindecoration.desktop %buildroot/%_menudir/kdebase-kwindecoration kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/screensaver.desktop %buildroot/%_menudir/kdebase-screensaver kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/style.desktop %buildroot/%_menudir/kdebase-style kde
################""FIXME
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Network %buildroot/%_datadir/applications/kde/netpref.desktop %buildroot/%_menudir/kdebase-netpref kde
#perl -pi -e "s|socket.png|network.png|" %buildroot/%_menudir/kdebase-netpref
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Network %buildroot/%_datadir/applications/kde/proxy.desktop %buildroot/%_menudir/kdebase-proxy kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Network %buildroot/%_datadir/applications/kde/lanbrowser.desktop %buildroot/%_menudir/kdebase-lanbrowser kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/kcmcgi.desktop %buildroot/%_menudir/kdebase-kcmcgi kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/cache.desktop %buildroot/%_menudir/kdebase-cache kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/cookies.desktop %buildroot/%_menudir/kdebase-cookies kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/ebrowsing.desktop %buildroot/%_menudir/kdebase-ebrowsing kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/kcmcss.desktop %buildroot/%_menudir/kdebase-kcmcss kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/kcmhistory.desktop %buildroot/%_menudir/kdebase-kcmhistory kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_behavior.desktop %buildroot/%_menudir/kdebase-khtml-behavior kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_fonts.desktop %buildroot/%_menudir/kdebase-khtml-fonts kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_java_js.desktop %buildroot/%_menudir/kdebase-khtml-java-js kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_java_js.desktop %buildroot/%_menudir/kdebase-khtml-java-js kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_plugins.desktop %buildroot/%_menudir/kdebase-khtml-plugins kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/khtml_filter.desktop %buildroot/%_menudir/kdebase-khtml-filter kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/WebBrowsing %buildroot/%_datadir/applications/kde/useragent.desktop %buildroot/%_menudir/kdebase-useragent kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/keyboard.desktop %buildroot/%_menudir/kdebase-keyboard kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/mouse.desktop %buildroot/%_menudir/kdebase-mouse kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/printers.desktop %buildroot/%_menudir/kdebase-printers kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Security %buildroot/%_datadir/applications/kde/crypto.desktop %buildroot/%_menudir/kdebase-crypto kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Sound %buildroot/%_datadir/applications/kde/arts.desktop %buildroot/%_menudir/kdebase-arts kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Sound %buildroot/%_datadir/applications/kde/bell.desktop %buildroot/%_menudir/kdebase-bell kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/kcmnotify.desktop %buildroot/%_menudir/kdebase-kcmnotify kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/clock.desktop %buildroot/%_menudir/kdebase-clock kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/desktoppath.desktop %buildroot/%_menudir/kdebase-desktoppath kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kcmfontinst.desktop %buildroot/%_menudir/kdebase-kcmfontinst kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kdm.desktop %buildroot/%_menudir/kdebase-kdm kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/display.desktop %buildroot/%_menudir/kdebase-display kde
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kcmperformance.desktop %buildroot/%_menudir/kdebase-kcmperformance kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/kcmview1394.desktop %buildroot/%_menudir/kdebase-kcmview1394 kde
#perl -pi -e "s|ieee1394.png|input_devices_settings.png|" %buildroot/%_menudir/kdebase-kcmview1394

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/khotkeys.desktop %buildroot/%_menudir/kdebase-khotkeys kde

########FIXME kde 3.4
#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/knetattach.desktop %buildroot/%_menudir/kdebase-knetattach kde


#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kfontview.desktop %buildroot/%_menudir/kdebase-kfontview kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kthememanager.desktop %buildroot/%_menudir/kdebase-kthememanager kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/installktheme.desktop %buildroot/%_menudir/kdebase-installktheme kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/joystick.desktop %buildroot/%_menudir/kdebase-joystick kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kcm_useraccount.desktop %buildroot/%_menudir/kdebase-useraccount kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kdepasswd.desktop %buildroot/%_menudir/kdebase-kdepasswd kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kwinoptions.desktop %buildroot/%_menudir/kdebase-kwinoptions kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kwinrules.desktop %buildroot/%_menudir/kdebase-kwinrules kde

 #mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kcm_kdnssd.desktop %buildroot/%_menudir/kdebase-kcm_kdnssd kde

#mandriva-add-xdg-categories.pl  System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/media.desktop %buildroot/%_menudir/kdebase-media kde

#mandriva-add-xdg-categories.pl kdebase-kmenuedit Configuration %buildroot/%_datadir/applications/kde/kmenuedit.desktop %buildroot/%_menudir/kdebase-kmenuedit

#mandriva-add-xdg-categories.pl  .hidden %buildroot/%_datadir/applications/kde/kfmclient.desktop %buildroot/%_menudir/kdebase-kfmclient kde
#mandriva-add-xdg-categories.pl  .hidden %buildroot/%_datadir/applications/kde/kfmclient_dir.desktop %buildroot/%_menudir/kdebase-kfmclient_dir kde
#mandriva-add-xdg-categories.pl  Configuration %buildroot/%_datadir/applications/kde/kfmclient_html.desktop %buildroot/%_menudir/kdebase-kfmclient_html kde
mandriva-add-xdg-categories.pl  %buildroot/%_datadir/applications/kde/kfmclient_war.desktop Networking kde 

#mandriva-add-xdg-categories.pl  System/Configuration %buildroot/%_datadir/applications/kde/kinfocenter.desktop %buildroot/%_menudir/kdebase-kinfocenter kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/konsole.desktop System/Terminals kde

#mandriva-add-xdg-categories.pl  System/Configuration/Hardware %buildroot/%_datadir/applications/kde/krandrtray.desktop %buildroot/%_menudir/kdebase-krandrtray kde
#mandriva-add-xdg-categories.pl   System/Configuration/KDE/LookNFeel %buildroot/%_datadir/applications/kde/ksplashthememgr.desktop %buildroot/%_menudir/kdebase-ksplashthememgr kde
#mandriva-add-xdg-categories.pl   System/Configuration/KDE/Security %buildroot/%_datadir/applications/kde/privacy.desktop %buildroot/%_menudir/kdebase-privacy kde



mandriva-add-xdg-categories.pl  buildroot/%_datadir/applications/kde/ksysguard.desktop System/Monitoring 


# %%_datadir/applnk/System/Utilities/
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/kdeprintfax.desktop "Office/Communications/Fax" kde
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde/kjobviewer.desktop System/Monitoring kde




# Link KDM images directory to faces directory
rm -fr %buildroot/%_datadir/apps/kdm/pics/users/
(
cd %buildroot/%_datadir/apps/kdm/pics
ln -s ../../../faces/ ./users
)

# Remove KDE hat...
rm -f %buildroot/%_datadir/apps/kdewizard/pics/wizard_small.png
# ...and install a safe image
install -m 0644 %SOURCE510 %buildroot/%_datadir/apps/kdewizard/pics/wizard_small.png

# David - 2.2.0.beta1.3mdk - Remove a potential problem with Apple
rm -f %buildroot/%_datadir/wallpapers/default_blue.jpg

install -d %buildroot/%_datadir/apps/kdesktop/Desktop

# David - 2.2.2-77mdk - The QtCUPS and KUPS packages are taken from the distro,
#                       because QtCUPS got integrated into KDE and is "kprinter"
#                       now and KUPS is the KDE Printing Manager now (KDE
#                       Control Center, "System"/"Printing Manager". The tools
#                       are generalized to aso work with LPD or LPRng. To help
#                       the old-fashioned users who always type "kups" and
#                       "qtcups" at the command prompt
(
cd %buildroot/%_bindir
ln -s kprinter qtcups
ln -s kprinter lpr-kprinter
)

cd %buildroot/%_datadir/wallpapers/
ln -s %_datadir/mdk/backgrounds mandriva

# David - 2.2.2-77mdk - Create a fake /usr/bin/kups
install -m 0755 %SOURCE2000 %buildroot/%_bindir/kups

# David - 3.0-0.beta1.8mdk - Allow users to launch KDE 3 easilily. To remove when
#                            KDE 3 will be installed in /usr/
#install -d -m 0755 %buildroot/etc/profile.d/
#install -m 0755 %SOURCE1000 %buildroot/etc/profile.d/kde3.sh

install -m 0644 %SOURCE5000 %buildroot/%_datadir/apps/kdisplay/color-schemes/Galaxy.kcsrc

install -m 0644 %SOURCE200000 %buildroot/%_datadir/apps/kdisplay/color-schemes/lycoris.kcsrc

install -m 0644 %SOURCE300000 "%buildroot/%_datadir/apps/kdisplay/color-schemes/Ia Ora Blue.kcsrc"
install -m 0644 %SOURCE300001 "%buildroot/%_datadir/apps/kdisplay/color-schemes/Ia Ora Free.kcsrc"
install -m 0644 %SOURCE300002 "%buildroot/%_datadir/apps/kdisplay/color-schemes/Ia Ora Gray.kcsrc"
install -m 0644 %SOURCE300003 "%buildroot/%_datadir/apps/kdisplay/color-schemes/Ia Ora Orange.kcsrc"


install -d -m 0755 %buildroot/%_datadir/apps/kthememanager/themes/Mandriva/
install -m 0644 %SOURCE200001 %buildroot/%_datadir/apps/kthememanager/themes/Mandriva/Mandriva.preview.png
install -m 0644 %SOURCE200002 %buildroot/%_datadir/apps/kthememanager/themes/Mandriva/Mandriva.xml

install -m 0644 %SOURCE7000 %buildroot/%_datadir/apps/konqueror/profiles/trash
install -m 0644 %SOURCE200020 %buildroot/%_datadir/apps/konqueror/profiles/devices


install -m 0755 %SOURCE50000 %buildroot/%_datadir/apps/kconf_update/migratemenu.pl
install -m 0755 %SOURCE50001 %buildroot/%_datadir/apps/kconf_update/translatemenu.upd

install -m 0755 %SOURCE50002 %buildroot/%_datadir/apps/kconf_update/migratemenu.sh

perl -pi -e 's|Icon=.*|Icon=find-mdk|' %buildroot/%_datadir/apps/kicker/menuext/find.desktop
perl -pi -e 's|Icon=.*|Icon=find-files-mdk|' %buildroot/%_datadir/apps/kicker/menuext/find/kfind.desktop
perl -pi -e 's|Icon=.*|Icon=recent-mdk|' %buildroot/%_datadir/apps/kicker/menuext/recentdocs.desktop

perl -pi -e 's|Icon=.*|Icon=home-mdk|' %buildroot/%_datadir/apps/kdesktop/DesktopLinks/Home.desktop

rm -f %buildroot/%_datadir/applications/kde/konsolesu.desktop
rm -f %buildroot/%_datadir/applications/kde/konquerorsu.desktop

%clean
rm -fr %buildroot


