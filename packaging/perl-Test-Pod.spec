#specfile originally created for Fedora, modified for Moblin Linux
Name:           perl-Test-Pod
Version:        1.42
Release:        1
Summary:        Perl module for checking for POD errors in files

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Pod/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Pod-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Module::Build) >= 0.30
BuildRequires:  perl(Pod::Simple) >= 3.07
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More) >= 0.70
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
%{summary}.

%prep
%setup -q -n Test-Pod-%{version}

%build
%{__perl} Build.PL  --installdirs vendor
./Build

%check
LC_ALL=C ./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/Test/*
%doc %{_mandir}/man3/*.3pm*


