# Share doc between python- and python3-
%global _docdir_fmt %{name}
%global sum Google APIs Client Library for Python
%global srcname google-api-client

Name:           google-api-python-client
Summary:        %{sum}
Epoch:          2
Version:        2.27.0
Release:        1%{?dist}

License:        ASL 2.0
URL:            https://github.com/googleapis/%{name}/
Source0:        https://github.com/googleapis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description 
Written by Google, this library provides a small, flexible, and powerful
Python client library for accessing Google APIs.

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files googleapiclient apiclient

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE 
%doc README.md

%changelog
* Mon Oct 25 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2:2.27.0-1
- Version bump and switch to pyproject-rpm-macros

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2:1.6.7-15
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 2:1.6.7-13
- Revert to 1.6.7

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.12.1-1
- 1.12.1

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.11.0-1
- 1.11.0

* Wed Aug 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.10.1-1
- 1.10.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.10.0-1
- 1.10.0

* Tue Jun 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.9.3-2
- Requires fix.

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.9.3-1
- Update to 1.9.3

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.6.7-12
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.6.7-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.6.7-9
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.6.7-8
- Subpackage python2-google-api-client has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Michele Baldessari <michele@acksyn.org> - 1.6.7-5
- Add an epoch and downgrade to 1.6.7 while we get python-google-auth-httplib2

* Mon Jan 21 2019 Michele Baldessari <michele@acksyn.org> - 1.7.7-1
- New upstream

* Fri Jul 20 2018 Alfredo Moralejo <amoralej@redhat.com> - 1.6.7-4
- Fix build when disabling python3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Michele Baldessari <michele@acksyn.org> - 1.6.7-1
- New upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Michele Baldessari <michele@acksyn.org> - 1.6.5-1
- New upstream

* Mon Oct 23 2017 Michele Baldessari <michele@acksyn.org> - 1.6.4-1
- New upstream

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.3-2
- Fix BuildRequires/Requires to use python2-* for Fedora

* Thu Aug 31 2017 Michele Baldessari <michele@acksyn.org> - 1.6.3-1
- New upstream

* Fri Aug 4 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.2-2
- Fix conditionals for epel

* Tue Aug 1 2017 Nick Bebout <nb@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.5-2
- Rebuild for Python 3.6

* Thu Nov 10 2016 Michele Baldessari <michele@acksyn.org> - 1.5.5-1
New upstream

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 22 2016 Michele Baldessari <michele@acksyn.org> - 1.5.1-1
- New upstream

* Thu Mar 10 2016 Michele Baldessari <michele@acksyn.org> - 1.5.0-1
- New upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Michele Baldessari <michele@acksyn.org> - 1.4.2-4
- Make spec more epel friendly

* Mon Nov 02 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-3
- Cleanup spec according to newest python policy
- Drop python3 conditional, we'll build this for Fedora only for now anyways

* Wed Oct 21 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-2
- Address some comments from BZ 1272187

* Thu Oct 15 2015 Michele Baldessari <michele@acksyn.org> - 1.4.2-1
- Update to 1.4.2

* Tue Jun 23 2015 Michele Baldessari <michele@acksyn.org> - 1.4.1-1
- Update to 1.4.1

* Sun Jun 07 2015 Michele Baldessari <michele@acksyn.org> - 1.4.0-1
- Update to latest version
- Add python3 package
- Tag LICENSE with appropriate macro
- Generate {python,python3}-google-api-client packages to be more consistent
  within Fedora
- Add python-oauthclient dependency

* Sat Feb 14 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.1-1
- Update to latest version

* Sat Jul 27 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.1-1
- Initial rpm package

