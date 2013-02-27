Name:           perl-Test-Pod
Version:        1.45
Release:        3%{?dist}
Summary:        Test POD files for correctness
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Pod/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Test-Pod-%{version}.tar.gz
Source1001:     packaging/perl-Test-Pod.manifest
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build) >= 0.3000
BuildRequires:  perl(Pod::Simple) >= 3.05
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More) >= 0.62
Requires:       perl
Requires:       perl(Pod::Simple) >= 3.05
Requires:       perl(Test::Builder::Tester) >= 1.02
Requires:       perl(Test::More) >= 0.62

%description
Check POD files for errors or warnings in a test file, using Pod::Simple to do
the heavy lifting.

%prep
%setup -q -n Test-Pod-%{version}

%build
cp %{SOURCE1001} .
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} \; 2>/dev/null
%{_fixperms} $RPM_BUILD_ROOT

%check
#LC_ALL=C ./Build test


%files
%defattr(-,root,root,-)
%manifest perl-Test-Pod.manifest
%doc Changes README
%{perl_vendorlib}/Test/*
%doc %{_mandir}/man3/Test::Pod.3pm*


