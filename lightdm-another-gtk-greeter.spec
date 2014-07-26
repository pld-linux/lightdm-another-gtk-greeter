%define		pver	1.0.6.3
%define		prel	4
#
Summary:	Yet another GTK+ greeter for LightDM
Name:		lightdm-another-gtk-greeter
Version:	%{pver}.%{prel}
Release:	1
License:	GPL v3
Group:		Themes
Source0:	http://github.com/kalgasnik/lightdm-another-gtk-greeter/archive/%{pver}-%{prel}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	7e4255fccd5725be98a5b40a61953130
URL:		http://github.com/kalgasnik/lightdm-another-gtk-greeter/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxklavier-devel
BuildRequires:	lightdm-libs-gobject-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Provides:	lightdm-greeter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another GTK+ greeter for LightDM.

%prep
%setup -q -n %{name}-%{pver}-%{prel}

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS INSTALL ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lightdm/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/xgreeters/%{name}.desktop
