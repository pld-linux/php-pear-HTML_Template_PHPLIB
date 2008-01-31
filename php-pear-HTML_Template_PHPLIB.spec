%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_PHPLIB
Summary:	%{_pearname} - preg_* based template system
Summary(pl.UTF-8):	%{_pearname} - system szablonĂłw bazowany na preg_*
Name:		php-pear-%{_pearname}
Version:	1.3.3
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9e415db896569c5542c7d15b5926551d
URL:		http://pear.php.net/package/HTML_Template_PHPLIB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
