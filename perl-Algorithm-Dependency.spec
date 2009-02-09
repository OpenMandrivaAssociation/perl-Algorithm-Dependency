%define module	Algorithm-Dependency
%define name	perl-%{module}
%define version 1.107
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Algorithmic framework for implementing dependency tree
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Algorithm/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Config::Tiny) >= 2.0
BuildRequires:	perl(Test::ClassAPI) >= 0.6
BuildRequires:  perl(Params::Util)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Algorithm::Dependency is a framework for creating simple read-only
dependency hierachies, where you have a set of items that rely on other
items in the set, and require actions on them as well.

Despite the most visible of these being software installation systems
like the CPAN installer, or debian apt-get, they are usefu
situations. This module intentionally uses implementation-neutral words,
to avoid confusion.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*

