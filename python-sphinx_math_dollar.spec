#
# Conditional build:
%bcond_with	tests	# unit tests (missing test-build data?)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to let you write LaTeX math using $$
Summary(pl.UTF-8):	Rozszerzenie Sphinksa pozwalające pisać wzory matematyczne w LaTeXu przy użyciu $$
Name:		python-sphinx_math_dollar
Version:	1.1.1
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-math-dollar/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-math-dollar/sphinx-math-dollar-%{version}.tar.gz
# Source0-md5:	9e1cbc49cb2f8d7d85c63df55120d16c
URL:		https://pypi.org/project/sphinx-math-dollar/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx
BuildRequires:	python-pytest
BuildRequires:	python-sphinx_testing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
BuildRequires:	python3-sphinx_testing
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.

%description -l pl.UTF-8
sphinx-math-dollar to rozszerzenie Sphinksa pozwalające pisać wzory
matematyczne w LaTeXu przy użyciu $$.

%package -n python3-sphinx_math_dollar
Summary:	Sphinx extension to let you write LaTeX math using $$
Summary(pl.UTF-8):	Rozszerzenie Sphinksa pozwalające pisać wzory matematyczne w LaTeXu przy użyciu $$
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx_math_dollar
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math
using $$.

%description -n python3-sphinx_math_dollar -l pl.UTF-8
sphinx-math-dollar to rozszerzenie Sphinksa pozwalające pisać wzory
matematyczne w LaTeXu przy użyciu $$.

%prep
%setup -q -n sphinx-math-dollar-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest sphinx_math_dollar/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest sphinx_math_dollar/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinx_math_dollar
%{py_sitescriptdir}/sphinx_math_dollar-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_math_dollar
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_math_dollar
%{py3_sitescriptdir}/sphinx_math_dollar-%{version}-py*.egg-info
%endif
