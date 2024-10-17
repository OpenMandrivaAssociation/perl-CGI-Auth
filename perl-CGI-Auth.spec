%define upstream_name    CGI-Auth
%define upstream_version 3.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	Simple session-based password authentication for CGI applications
License:	BSD-like
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CC/CCWALLACE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
"CGI::Auth" provides password authentication for web-based applications. It
uses server-based session files which are referred to by a parameter in all
links and forms inside the scripts guarded by "CGI::Auth".

At the beginning of each script, a "CGI::Auth" object should be created and its
"check" method called. When this happens, "check" checks for a 'session_file'
CGI parameter. If that parameter exists and has a matching session file in the
session directory, "check" returns, and the rest of the script can execute.

If the session file parameter or the file itself doesn't exist, "check"
presents the user with a login form and exits the script. The login form will
then be submitted to the same script (specified in "-formaction"). When "check"
is called this time, it verifies the user's login information in the userfile,
creates a session file and provides the session file parameter to the rest of
the script.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#make test

%install
%makeinstall_std

%files
%doc Changes README extra
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 3.0.0-6mdv2011.0
+ Revision: 680684
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-5mdv2011.0
+ Revision: 504598
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.00-4mdv2010.0
+ Revision: 430302
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.00-3mdv2009.0
+ Revision: 241164
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3.00-1mdv2008.0
+ Revision: 26732
- disable the tests for now because of unknown iurt problems
- fix deps
- Import perl-CGI-Auth



* Mon May 14 2007 Oden Eriksson <oeriksson@mandriva.com> 3.00-1mdv2007.1
- initial Mandriva package 
