#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (missing index)
%bcond_with	tests	# unit tests (missing app fixture?)

Summary:	Sphinx extension to let you write LaTeX math using $$
Summary(pl.UTF-8):	Rozszerzenie Sphinksa pozwalające pisać wzory matematyczne w LaTeXu przy użyciu $$
Name:		python3-sphinx_math_dollar
Version:	1.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-math-dollar/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-math-dollar/sphinx_math_dollar-%{version}.tar.gz
# Source0-md5:	8c466dd5eba533b0f2823e189cb4e00f
URL:		https://pypi.org/project/sphinx-math-dollar/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools >= 1:42
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.

%description -l pl.UTF-8
sphinx-math-dollar to rozszerzenie Sphinksa pozwalające pisać wzory
matematyczne w LaTeXu przy użyciu $$.

%prep
%setup -q -n sphinx_math_dollar-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest sphinx_math_dollar/tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_math_dollar
%{py3_sitescriptdir}/sphinx_math_dollar-%{version}.dist-info
