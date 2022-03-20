%global pypi_name proglog

Name:           python-%{pypi_name}
Version:        0.1.9
Release:        2
Group:          Development/Python
Summary:        Log and progress bar manager for console, notebooks, web
License:        MIT
URL:            https://github.com/Edinburgh-Genome-Foundry/Proglog
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildArch:      noarch

%description
Proglog is a progress logging system for Python. It allows to build
complex libraries while giving the user control on the management of
logs, callbacks and progress bars.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENCE.txt
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info
