%define upstream_name    CGI-Auth
%define upstream_version 3.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 6

Summary:	Simple session-based password authentication for CGI applications
License:	BSD-like
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/C/CC/CCWALLACE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#%%check
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README extra
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*
