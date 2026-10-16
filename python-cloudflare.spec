%define module cloudflare

Name:		python-cloudflare
Version:	5.9.0
Release:	1
Summary:	Official Python library for the Cloudflare API
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/cloudflare/cloudflare-python
Source0:	https://files.pythonhosted.org/packages/source/c/cloudflare/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)
BuildRequires:	python%{pyver}dist(pip)

%description
The official Python library for the Cloudflare API.
Certbot's DNS authenticator talks to Cloudflare through this module.
The optional aiohttp extra is not required.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
