%global pypi_name proglog

Name:           python-%{pypi_name}
Version:        0.1.9
Release:        %mkrel 1
Group:          Development/Python
Summary:        Log and progress bar manager for console, notebooks, web
License:        MIT
URL:            https://github.com/Edinburgh-Genome-Foundry/Proglog
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Proglog is a progress logging system for Python. It allows to build
complex libraries while giving the user control on the management of
logs, callbacks and progress bars.

%package -n python3-%{pypi_name}
Summary:        Log and progress bar manager for console, notebooks, web
Group:          Development/Python
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Proglog is a progress logging system for Python. It allows to build
complex libraries while giving the user control on the management of
logs, callbacks and progress bars.
This is the Python 3 build of %{pypi_name}.

%prep
%setup -q -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENCE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
