#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	Multimethods
Summary:	Class::Multimethods - support multimethods and function overloading in Perl
Summary(pl.UTF-8):	Class::Multimethods - obsługa wielometod i przeciążania funkcji w Perlu
Name:		perl-Class-Multimethods
Version:	1.70
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fdc79daa81b102b956b1a61531fd6a7
URL:		http://search.cpan.org/dist/Class-Multimethods/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Class::Multimethod module exports a subroutine (&multimethod) that
can be used to declare other subroutines that are dispatched using a
algorithm different from the normal Perl subroutine or method dispatch
mechanism.

%description -l pl.UTF-8
Moduł Class::Multimethod eksportuje funkcję (&multimethod), która może
być użyta do deklarowania innych funkcji, które mogą być wysyłane przy
użyciu innego algorytmu niż normalnie używany przez Perla dla funkcji
lub metod.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
