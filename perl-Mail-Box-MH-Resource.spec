#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Box-MH-Resource
Summary:	Mail::Box::MH::Resource - Manage an MH resource file such as the MH profile
Summary(pl):	Mail::Box::MH::Resource - zarz±dzanie plikami zasobów MH takimi jak profile MH
Name:		perl-Mail-Box-MH-Resource
Version:	0.05
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	422dc5db21ed7e323dccb7dff174b115
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-Mail-Box
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Read and write MH format resource files such as profile, context,
and sequence.

%description -l pl
Ten modu³ czyta i zapisuje pliki zasobów w formacie MH, takie jak
profile, context i sequence.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{perl_vendorlib}/Mail/Box/MH
%{perl_vendorlib}/Mail/Box/MH/*.pm
%{_mandir}/man3/*
