%define		module	pyxdg

Summary:	Python implementations of freedesktop.org standards
Name:		python-%{module}
Version:	0.24
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://people.freedesktop.org/~takluyver/%{module}-%{version}.tar.gz
# Source0-md5:	f87bcec485261a59030df4ecf7dfe035
URL:		http://freedesktop.org/Software/pyxdg
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXDG is a python module to access freedesktop.org standards.

%prep
%setup -qn %{module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install	\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%dir %{py_sitescriptdir}/xdg
%{py_sitescriptdir}/xdg/*.py[co]

