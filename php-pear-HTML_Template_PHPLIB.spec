%define		_status		stable
%define		_pearname	HTML_Template_PHPLIB
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - preg_* based template system
Summary(pl.UTF-8):	%{_pearname} - system szablonĂłw bazowany na preg_*
Name:		php-pear-%{_pearname}
Version:	1.5.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b98d718a3b4185583458c583b7d13e5d
URL:		http://pear.php.net/package/HTML_Template_PHPLIB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-HTML_Template_PHPLIB-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The popular Template system from PHPLIB ported to PEAR. It has some
features that can't be found currently in the original version like
fallback paths. It has minor improvements and cleanup in the code as
well as some speed improvements.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Popularny system szablonĂłw dla PHPLIB, sportowane do PEAR-a. Posiada
kilka dodatkowych cech w stosunku do oryginalnego wersji takie jak
domyślne ścieżki. Dokonano także drobnych poprawek w kodzie
dotyczących czyszczenia kodu jak i wydajności.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/Template/*
