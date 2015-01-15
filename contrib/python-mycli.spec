# Failsafe backport of Python2-macros for RHEL <= 6
%{!?python_sitelib:	%global python_sitelib		%(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch:	%global python_sitearch		%(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%{!?python_version:	%global python_version		%(%{__python} -c "import sys; sys.stdout.write(sys.version[:3])")}
%{!?__python2:		%global __python2		%{__python}}
%{!?python2_sitelib:	%global python2_sitelib		%{python_sitelib}}
%{!?python2_sitearch:	%global python2_sitearch	%{python_sitearch}}
%{!?python2_version:	%global python2_version		%{python_version}}

%{!?python2_minor_version: %define python2_minor_version %(%{__python} -c "import sys ; print sys.version[2:3]")}

%global upstream_name mycli


Name:			python-%{upstream_name}
Version:		0.0.1
Release:		1%{?dist}
Summary:		A Python program that demonstrates usage of argparse
%{?el5:Group:		Applications/Scientific}
License:		ASL 2.0

URL:			https://github.com/marcindulak/%{name}
Source0:		https://github.com/marcindulak/%{name}/%{name}-%{version}.tar.gz

%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildArch:		noarch

%if 0%{?suse_version}
BuildRequires:		python-devel
%else
BuildRequires:		python2-devel
%endif


%description
A Python program that demonstrates usage of argparse.


%prep
%setup -qn %{name}-%{version}


%build
%{__python2} setup.py build


%install
%{?el5:rm -rf $RPM_BUILD_ROOT}
%{__python2} setup.py install --skip-build --prefix=%{_prefix} \
	   --optimize=1 --root $RPM_BUILD_ROOT


%check
export PYTHONPATH=`pwd`/build/lib
export PATH=`pwd`/build/scripts-%{python2_version}:${PATH}
%if 0%{python2_minor_version} >= 7
%{__python2} -m unittest discover -s %{upstream_name}/tests -p '*.py'
%endif


%clean
%{?el5:rm -rf $RPM_BUILD_ROOT}


%files
%doc LICENSE README.rst
%{_bindir}/*
%{python2_sitelib}/%{upstream_name}
%{?!el5:%{python2_sitelib}/*.egg-info}


%changelog
* Wed Jan 14 2015 Marcin Dulak <Marcin.Dulak@gmail.com> - 0.0.1-1
- initial version
