# THIS PACKAGE IS HOSTED AT MANDRIVA SVN
# PLEASE DO NOT UPLOAD DIRECTLY BEFORE COMMIT

%define name         verbiste
%define version      0.1.19
%define release      %mkrel 2
%define __libtoolize /bin/true
%define __cputoolize /bin/true

%define major   1
%define libname %mklibname %name %major

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   To use well french verbs
License:   GPL
URL:       http://www3.sympatico.ca/sarrazip/dev/%name.html
Group:     Toys
Source:    http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.bz2
BuildRequires: libxml2-devel
BuildRequires: libgnomeui2-devel gnome-panel-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Verbiste is a French conjugation system. It contains a C++ library, two 
programs that can be run from the command line or from another program, 
and a GNOME applet. This applet shows a text field in the GNOME Panel 
where the user can enter a conjugated verb and obtain its complete 
conjugation. The knowledge base is represented in XML and contains over 
6800 verbs.

%files -f %{name}.lang
%defattr(-,root,root) 
%doc AUTHORS COPYING HACKING INSTALL LISEZMOI NEWS  README TODO
%_bindir/french-*conjugator
%_datadir/%name-0.1
%_mandir/fr/man?/*
%_mandir/man?/*


#--------------------------------------------------------------------

%package -n     %name-gtk
Summary:        Gtk+ interface for %name
Group:          Development/Other

%description  -n %name-gtk
Gtk+ interface for %name.

%files -n %name-gtk
%defattr(-,root,root)
%_bindir/verbiste
%_bindir/verbiste-gtk
%_libdir/bonobo/servers/verbiste.server
%_libdir/verbiste-applet
%_datadir/applications/verbiste.desktop
%_datadir/pixmaps/verbiste.png


#--------------------------------------------------------------------

%package -n     %{libname}
Summary:        Shared Librairies for %name
Group:          Development/Other

%description  -n %{libname}
Shared Librairies for cluster

%postun -n %{libname} 
/sbin/ldconfig

%post -n %{libname} 
/sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%_libdir/lib%name-0.1.la
%_libdir/lib%name-0.1.so.0
%_libdir/lib%name-0.1.so.0.0.0

#--------------------------------------------------------------------

%package -n %{libname}-devel
Summary:        %name header files and static libraries
Group:          Development/Other
Requires:       %{name} = %{version}
Requires:       %{libname} = %{version}
Provides:       %name-devel = %{version}

%description -n %{libname}-devel
This package contains header files and static libraries.

%files -n %{libname}-devel
%defattr(-,root,root)
%_includedir/%name-0.1/%name/FrenchVerbDictionary.h
%_includedir/%name-0.1/%name/HashMap.h
%_includedir/%name-0.1/%name/Trie.cpp
%_includedir/%name-0.1/%name/Trie.h
%_includedir/%name-0.1/%name/c-api.h
%_includedir/%name-0.1/%name/misc-types.h
%_libdir/lib%name-0.1.so
%_libdir/pkgconfig/%name-0.1.pc

#--------------------------------------------------------------------
%prep

%setup -q -n %{name}-%{version}

%configure --with-gtk-app --with-gnome-app --with-gnome-applet

%install
rm -rf %buildroot
%{makeinstall_std}

%find_lang %{name}
%clean
rm -rf %{buildroot}


