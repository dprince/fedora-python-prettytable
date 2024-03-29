%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

%global modname prettytable


Name:		python-%{modname}
Version:	0.6.1
Release:	1%{?dist}
Summary:	Python library to display tabular data in tables

Group:		Development/Languages
License:	BSD
Source0:    http://pypi.python.org/packages/source/P/PrettyTable/%{modname}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:  python-setuptools

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif


%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:	Python library to display tabular data in tables
Group:		Development/Languages

%description -n python3-%{modname}
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.
%endif


%prep
%setup -q -n %{modname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%check
%{__python} %{modname}_test.py

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} %{modname}_test.py
popd
%endif


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc README COPYING CHANGELOG
%{python_sitelib}/%{modname}.py*
%{python_sitelib}/%{modname}-%{version}*

%if 0%{?with_python3}
%files -n python3-%{modname}
%doc README COPYING CHANGELOG
%{python3_sitelib}/%{modname}.py*
%{python3_sitelib}/__pycache__/%{modname}*
%{python3_sitelib}/%{modname}-%{version}*
%endif


%changelog
* Tue Aug 07 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- New upstream version
- Added support for python3
- Included README, COPYING, and CHANGELOG in docs

* Tue Aug 07 2012 Pádraig Brady <P@draigBrady.com> - 0.6-1
- Update to 0.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.5-2
- BuildRequire python-setuptools

* Wed Jun 29 2011 Chris Lalancette <clalance@redhat.com> - 0.5-1
- Initial package.
