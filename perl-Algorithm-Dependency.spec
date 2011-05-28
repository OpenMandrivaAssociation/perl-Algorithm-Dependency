%define upstream_name	 Algorithm-Dependency
%define upstream_version 1.110

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Algorithmic framework for implementing dependency tree
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Config::Tiny) >= 2.0
BuildRequires:	perl(Test::ClassAPI) >= 0.6
BuildRequires:  perl(Params::Util)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Algorithm::Dependency is a framework for creating simple read-only
dependency hierachies, where you have a set of items that rely on other
items in the set, and require actions on them as well.

Despite the most visible of these being software installation systems
like the CPAN installer, or debian apt-get, they are useful in others
situations. This module intentionally uses implementation-neutral words,
to avoid confusion.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
