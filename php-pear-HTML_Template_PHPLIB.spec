%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_PHPLIB
Summary:	%{_pearname} - preg_* based template system
Summary(pl):	%{_pearname} - system szablon�w bazowany na preg_*
Name:		php-pear-%{_pearname}
Version:	1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	353a42a0086be45bb71c6087f3b4da3f
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-cosmetic.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The popular Template system from PHPLIB ported to PEAR.

This class has in PEAR status: %{_status}.

%description -l pl
Popularny system szablon�w dla PHPLIB, sportowane do PEAR-a.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
