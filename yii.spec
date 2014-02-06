%define         releasehash f0fee9

Name:           yii
Version:        1.1.14
Release:        0.3%{?dist}
Summary:        The Yii PHP framework

License:        BSD
URL:            http://www.yiiframework.com
Source0:        https://github.com/yiisoft/yii/releases/download/%{version}/yii-%{version}.%{releasehash}.tar.gz

BuildArch:      noarch
BuildRequires:  tar, gzip, findutils
Requires:       php-common >= 5.1.0, php-pdo

%description
A high-performance component-based PHP framework best for developing Web 2.0
applications

%prep
%setup -qn yii-%{version}.%{releasehash}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}/%{_datadir}/%{name}
%{__cp} -r framework/* %{buildroot}/%{_datadir}/%{name}/
%{__mkdir} -p %{buildroot}/%{_bindir}
ln -s ../..%{_datadir}/%{name}/yiic %{buildroot}/%{_bindir}/yiic
%{__mkdir} -p %{buildroot}/%{_datadir}/php
ln -s ../../..%{_datadir}/%{name}/yii.php %{buildroot}/%{_datadir}/php/yii.php
ln -s ../../..%{_datadir}/%{name}/yiilite.php %{buildroot}/%{_datadir}/php/yiilite.php
%{__rm} %{buildroot}/%{_datadir}/%{name}/yiic.bat
%{__rm} -rf %{buildroot}/%{_datadir}/%{name}/test

find %{buildroot}/%{_datadir}/%{name} -name .yii -exec rm {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README UPGRADE
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/gii
%{_datadir}/php

%package devel
Summary:        The Yii development files
Requires:       yii

%description devel
This package holds the Yii development files, including the yiic command-line
utility and the gii module.

%files devel
%{_datadir}/%{name}/yiic
%{_bindir}/yiic
%{_datadir}/%{name}/gii

%changelog
 * Tue Feb 4 2014 Da:Sourcerer <webmaster@dasourcerer.net> - 1.1.14-0.3
 - Bumped to v1.1.14

 * Sat Jul 28 2012 Da:Sourcerer <webmaster@dasourcerer.net> - 1.1.10-0.3
 - Split development files into their own devel package
 - Removed remaining test files

 * Wed Mar 21 2012 Da:Sourcerer <webmaster@dasourcerer.net> - 1.1.10-0.2
 - Minor tweaks

 * Tue Mar 20 2012 Da:Sourcerer <webmaster@dasourcerer.net> - 1.1.10-0.1
 - Initial spec
