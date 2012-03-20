%define         svnrevision r3566

Name:           yii
Version:        1.1.10
Release:        0.1%{?dist}
Summary:        The Yii PHP framework

License:        BSD
URL:            http://www.yiiframework.com
Source0:        http://yii.googlecode.com/files/yii-%{version}.%{svnrevision}.tar.gz

BuildArch:      noarch
BuildRequires:  tar, gzip
Requires:       php-common >= 5.1.0, php-pdo
Provides:       yii = %{version}-%{release}

%description
Yii is a high-performance component-based PHP framework best for developing Web 2.0 applications

%prep
%setup -qn yii-%{version}.%{svnrevision}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}/%{_datadir}/%{name}
%{__cp} -r framework/* %{buildroot}/%{_datadir}/%{name}/
%{__mkdir} -p %{buildroot}/%{_bindir}
ln -s ../..%{_datadir}/%{name}/yiic %{buildroot}/%{_bindir}/yiic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README UPGRADE
%{_datadir}/%{name}
%{_bindir}/yiic

%changelog
 * Tue Mar 20 2012 Da:Sourcerer <webmaster@dasourcerer.net> - 1.1.10-0.1
 - Initial spec