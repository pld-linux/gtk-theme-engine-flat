Summary:	This theme engine gives GTK+ a flattened appearance
Summary(pl.UTF-8):   Motyw dający GTK+ spłaszczony wygląd
Name:		gtk-theme-engine-flat
Version:	0.1
Release:	2
License:	LGPL
Group:		Themes/GTK+
Source0:	http://download.freshmeat.net/themes/flat/flat-1.2.x.tar.gz
# Source0-md5:	5b9e6c974c2417b5793b5c930be29f5d
Patch0:		%{name}-gtkrc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This theme engine gives GTK+ a flattened appearance with elements
taken from the MacOS and Metal uis. Modified from the default and
metal theme engines; the colors and background pixmaps are fully
customizable.

%description -l pl.UTF-8
Ten motyw daje GTK+ spłaszczony wygląd z elementami wziętymi z
interfejsów użytkownika MacOS i Metal. Jest zmodyfikowany w stosunku
do motywów default i metal; kolory i obrazy tła są w pełni
konfigurowalne.

%prep
%setup  -q -n gtk-flat-theme-%{version}
%patch0 -p1

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%dir %{_datadir}/themes/*
%dir %{_datadir}/themes/*/gtk
%{_datadir}/themes/*/gtk/*
