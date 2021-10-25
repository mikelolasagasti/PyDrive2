%global sum An httplib2 transport for google-auth
%global srcname google-auth-httplib2

Name:           google-auth-httplib2
Summary:        %{sum}
Version:        0.1.0
Release:        1%{?dist}

License:        ASL 2.0
URL:            https://github.com/googleapis/google-auth-library-python-httplib2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description 
httplib has lots of problems such as lack of threadsafety and insecure usage
of TLS. Using it is highly discouraged. This library is intended to help
existing users of oauth2client migrate to google-auth.

%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{srcname}
Written by Google, this library provides a small, flexible, and powerful 
Python 3 client library for accessing Google APIs.

%prep
%autosetup -n google-auth-library-python-httplib2-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files google_auth_httplib2

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE 
%doc README.rst

%changelog
* Mon Oct 25 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.1.0-1
- Version bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.3-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.3-1
- Initial build

