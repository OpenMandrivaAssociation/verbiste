%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		verbiste
Version:	0.1.34
Release:	1
Summary:	To use well french verbs
License:	GPLv2+
Group:		Toys
URL:		http://http://perso.b2b2c.ca/sarrazip/dev/verbiste.html
Source0:	http://perso.b2b2c.ca/sarrazip/dev/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
Verbiste is a French conjugation system. It contains a C++ library, two
programs that can be run from the command line or from another program,
and a GNOME applet. This applet shows a text field in the GNOME Panel
where the user can enter a conjugated verb and obtain its complete
conjugation. The knowledge base is represented in XML and contains over
6800 verbs.

%package -n     %{name}-gtk
Summary:        Gtk+ interface for %{name}
Group:          Development/Other
Requires:       %{name} 

%description  -n %{name}-gtk
Gtk+ interface for %{name}.

%package -n     %{libname}
Summary:        Shared Librairies for %{name}
Group:          Development/Other

%description  -n %{libname}
Shared Librairies for cluster

%package -n %{devname}
Summary:        %{name} header files and static libraries
Group:          Development/Other
Requires:       %{name} = %{version}
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:	%{_lib}%{name}1-devel

%description -n %{devname}
This package contains header files and static libraries.

%prep
%setup -q

%build
%configure2_5x \
	--with-gtk-app \
	--with-gnome-app \
	--with-gnome-applet

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_docdir}/%{name}-%{version}/*
%{_bindir}/french-*conjugator
%{_datadir}/%{name}-0.1
%{_mandir}/fr/man?/*
%{_mandir}/man?/*

%files -n %{name}-gtk
%{_bindir}/verbiste
%{_bindir}/verbiste-gtk
%{_libdir}/bonobo/servers/verbiste.server
%{_libdir}/verbiste-applet
%{_datadir}/applications/verbiste.desktop
%{_datadir}/pixmaps/verbiste.png
%{_datadir}/texmf/tex/latex/verbiste/verbiste.cfg
%{_datadir}/texmf/tex/latex/verbiste/verbiste.cls

%files -n %{libname}
%{_libdir}/lib%{name}-0.1.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}-0.1
%{_libdir}/lib%{name}-0.1.so
%{_libdir}/pkgconfig/%{name}-0.1.pc

