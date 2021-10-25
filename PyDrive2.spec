Name:           PyDrive2
Version:        1.10.0
Release:        1%{?dist}
Summary:        Google Drive API Python wrapper library, maintained fork of PyDrive

License:        ASL-2.0 and BSD
URL:            https://github.com/iterative/PyDrive2
Source0:        %{url}/archive/%{version}/PyDrive2-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Google Drive API Python wrapper library. Maintained fork of PyDrive.

%package -n     python3-%{name}
Summary:        %{summary}

# required for check
BuildRequires:  pytest
BuildRequires:  python3dist(fsspec)
BuildRequires:  python3dist(funcy)
#BuildRequires:  python3dist(timeout_decorator)
BuildRequires:  python3dist(tqdm)

%description -n python3-%{name}
Google Drive API Python wrapper library. Maintained fork of PyDrive.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pydrive2

# ignoring for now as requires timeout_decorator
#%%check
#%%pytest

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Mon Oct 25 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 1.10.0-1
- Initial package
