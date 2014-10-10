%define upstream_name	 Algorithm-Dependency
%define upstream_version 1.110

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Algorithmic framework for implementing dependency tree
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Config::Tiny) >= 2.0
BuildRequires:	perl(Test::ClassAPI) >= 0.6
BuildRequires:	perl(Params::Util)

BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.110.0-3mdv2011.0
+ Revision: 680445
- mass rebuild

* Wed Feb 10 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.110.0-2mdv2011.0
+ Revision: 503911
- rebuild using %%perl_convert_version

* Fri Dec 25 2009 Michael Scherer <misc@mandriva.org> 1.110-2mdv2010.1
+ Revision: 482286
- fix License
- fix description

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.110-1mdv2010.0
+ Revision: 370007
- update to new version 1.110

* Thu Feb 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.108-1mdv2009.1
+ Revision: 339735
- update to new version 1.108

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.107-1mdv2009.1
+ Revision: 338706
- update to new version 1.107

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.106-3mdv2009.0
+ Revision: 255262
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.106-1mdv2008.1
+ Revision: 152822
- update to new version 1.106

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.104-1mdv2008.1
+ Revision: 109469
- update to new version 1.104

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.103-1mdv2008.0
+ Revision: 46962
- update to new version 1.103


* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.102-2mdv2007.0
- better source URL

* Mon Apr 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.102-1mdk
- New release 1.102
- better source URL
- better buildrequires syntax

* Wed Oct 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.101-1mdk
- New release 1.101

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.04-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdk
- New release 1.04
- spec cleanup
- fix directory ownership
- fix spelling errors in description

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.03-1mdk
- initial Mandriva package

