#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Multimethods
Summary:	Class::Multimethods - Support multimethods and function overloading in Perl
Summary(pl):	Class::Multimethods - obs³uga wielometod i przeci±¿ania funkcji w Perlu
Name:		perl-Class-Multimethods
Version:	1.70
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Class::Multimethod module exports a subroutine (&multimethod) that
can be used to declare other subroutines that are dispatched using a
algorithm different from the normal Perl subroutine or method dispatch
mechanism.

%description -l pl
Modu³ Class::Multimethod eksportuje funkcjê (&multimethod), która mo¿e
byæ u¿yta do deklarowania innych funkcji, które mog± byæ wysy³ane przy
u¿yciu innego algorytmu ni¿ normalnie u¿ywany przez Perla dla funkcji
lub metod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
perl -ni -e 'BEGIN{undef $/}print "#!/usr/bin/perl\n$_"' demo/*.pl
cp -a demo/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* *.html
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
