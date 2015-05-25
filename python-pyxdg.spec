%define		module	pyxdg

Summary:	Python implementations of freedesktop.org standards
Name:		python-%{module}
Version:	0.25
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://people.freedesktop.org/~takluyver/%{module}-%{version}.tar.gz
# Source0-md5:	bedcdb3a0ed85986d40044c87f23477c
URL:		http://freedesktop.org/Software/pyxdg
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXDG is a python module to access freedesktop.org standards.

%package -n python3-pyxdg
Summary:	Python implementations of freedesktop.org standards
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-pyxdg
PyXDG is a python module to access freedesktop.org standards.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
        --optimize=2		\
        --root=$RPM_BUILD_ROOT	\
        --skip-build
%py_postclean
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

%{__python3} setup.py build -b python3 install	\
        --optimize=2		\
        --root=$RPM_BUILD_ROOT	\
        --skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%dir %{py_sitescriptdir}/xdg
%{py_sitescriptdir}/xdg/*.py[co]
%{py_sitescriptdir}/*.egg-info

%files -n python3-pyxdg
%defattr(644,root,root,755)
%{py3_sitescriptdir}/xdg
%{py3_sitescriptdir}/*.egg-info
