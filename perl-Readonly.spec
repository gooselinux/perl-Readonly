Name:           perl-Readonly
Version:        1.03
Release:        11%{?dist}
Summary:        Facility for creating read-only scalars, arrays, hashes

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Readonly/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Readonly-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# perl-Readonly-XS builds for all current fedora architectures, so let's
# require it.
Requires:       perl(Readonly::XS)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Readonly.pm provides a facility for creating non-modifiable scalars,
arrays, and hashes.

Readonly.pm
* Creates scalars, arrays (not lists), and hashes.
* Creates variables that look and work like native perl variables.
* Creates global or lexical variables.
* Works at runtime or compile time.
* Works with deep or shallow data structures.
* Prevents reassignment of Readonly variables.

%prep
%setup -q -n Readonly-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

# make sure this goes where it should to be...
mv %{buildroot}%{perl_vendorlib}/benchmark.pl .


%check
make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes README benchmark.pl
%{perl_vendorlib}/Readonly.pm
%{_mandir}/man3/*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.03-11
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03-8
- Rebuild for perl 5.10 (again)

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-7
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-6.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.03-6.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Wed Oct 04 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.03-6
- add explict requires on perl(Readonly::XS).  perl(Readonly::XS) is available
  for all architectures fedora supports, so there's no good reason to not
  require it.
- spec file rework

* Tue Sep 19 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.03-5
- bump for mass rebuild

* Thu Dec 08 2005 Michael A. Peters <mpeters@mac.com> - 1.03-3
- Remove requires on perl-Readonly-XS

* Thu Dec 08 2005 Michael A. Peters <mpeters@mac.com> - 1.03-3
- Fix license and BuildRequires, use %%{?_smp_mflags} with make,

* Sat Nov 12 2005 Michael A. Peters <mpeters@mac.com> - 1.03-2
- separate out perl-Readonly-XS into its own package
- package benchmark.pl as a doc

* Mon Nov 7 2005 Michael A. Peters <mpeters@mac.com> - 1.03-1
- Initial spec file
