Name: gdcm
Version: 2.0.12
Release: %mkrel 2
License: GPLv2
Summary: GDCM is an open source DICOM library
Group: Development/C++
URL: http://sourceforge.net/apps/mediawiki/gdcm/index.php?title=Main_Page
# Get from https://svn.lrde.epita.fr/svn/oln/tags/olena-1.0 to have scribo
Source0:  %name-%version.tar.bz2
Patch0: %name-%version-insource.patch
Patch1: gdcm-2.0.12-system-libs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: cmake
BuildRequires: libuuid-devel
BuildRequires: zlib-devel
BuildRequires: jpeg-devel
BuildRequires: expat-devel
BuildRequires: openjpeg-devel
BuildRequires: doxygen
BuildRequires: vtk-devel
BuildRequires: python-vtk-devel
BuildRequires: tetex-latex
%py_requires -d

%description
GDCM is an open source DICOM library. It is meant to deal with DICOM files (as
specified in part 10 of the DICOM standard). It offers some compatibility with
ACR-NEMA 1.0 & 2.0 files (raw files).

%files
%defattr(-,root,root,-)
%_datadir/gdcm-2.0
%_bindir/*
%_mandir/*/*

#------------------------------------------------------------------------------

%package doc
Summary: %name documentation
Group: Books/Howtos

%description doc
%name documentation.

%files doc
%defattr(-,root,root,-)

#------------------------------------------------------------------------------

%define Common_major 2.0
%define libgdcmCommon %mklibname gdcmcommon %{Common_major}

%package -n %{libgdcmCommon}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmCommon}
Main %name library.

%files -n %{libgdcmCommon}
%defattr(-,root,root,-)
%{_libdir}/libgdcmCommon.so.%{Common_major}*

#------------------------------------------------------------------------------

%define DICT_major 2.0
%define libgdcmDICT %mklibname gdcmdict %{DICT_major}

%package -n %{libgdcmDICT}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmDICT}
Main %name library.

%files -n %{libgdcmDICT}
%defattr(-,root,root,-)
%{_libdir}/libgdcmDICT.so.%{DICT_major}*

#------------------------------------------------------------------------------

%define IOD_major 2.0
%define libgdcmIOD %mklibname gdcmiod %{IOD_major}

%package -n %{libgdcmIOD}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmIOD}
Main %name library.

%files -n %{libgdcmIOD}
%defattr(-,root,root,-)
%{_libdir}/libgdcmIOD.so.%{IOD_major}*

#------------------------------------------------------------------------------

%define DSED_major 2.0
%define libgdcmDSED %mklibname gdcmdsed %{DSED_major}

%package -n %{libgdcmDSED}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmDSED}
Main %name library.

%files -n %{libgdcmDSED}
%defattr(-,root,root,-)
%{_libdir}/libgdcmDSED.so.%{DSED_major}*

#------------------------------------------------------------------------------

%define MSFF_major 2.0
%define libgdcmMSFF %mklibname gdcmmsff %{MSFF_major}

%package -n %{libgdcmMSFF}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmMSFF}
Main %name library.

%files -n %{libgdcmMSFF}
%defattr(-,root,root,-)
%{_libdir}/libgdcmMSFF.so.%{MSFF_major}*

#------------------------------------------------------------------------------

%package devel
Summary: %name devel files
Group: Development/C++
Requires: %{libgdcmCommon} = %{version}
Requires: %{libgdcmMSFF} = %{version}
Requires: %{libgdcmDSED} = %{version}
Requires: %{libgdcmIOD} = %{version}
Requires: %{libgdcmDICT} = %{version}

%description devel
%name devel files

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/gdcm-2.0

#------------------------------------------------------------------------------

%define vtkgdcm_major 2.0
%define libgdcmvtkgdcm %mklibname vtkgdcm %{vtkgdcm_major}

%package -n %{libgdcmvtkgdcm}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmvtkgdcm}
Main %name library.

%files -n %{libgdcmvtkgdcm}
%defattr(-,root,root,-)
%{_libdir}/libvtkgdcm.so.%{vtkgdcm_major}*

#------------------------------------------------------------------------------

%define vtkgdcmPythonD_major 2.0
%define libgdcmvtkgdcmPythonD %mklibname vtkgdcmpythonp %{vtkgdcmPythonD_major}

%package -n %{libgdcmvtkgdcmPythonD}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmvtkgdcmPythonD}
Main %name library.

%files -n %{libgdcmvtkgdcmPythonD}
%defattr(-,root,root,-)
%py_platsitedir/libvtkgdcmPythonD.so.%{vtkgdcmPythonD_major}*

#------------------------------------------------------------------------------

%define jpeg_major 62.1
%define libgdcmjpeg %mklibname gdcmjpeg  %{jpeg_major}

%package -n %{libgdcmjpeg}
Summary: Main %name library
Group: Development/C++

%description -n %{libgdcmjpeg}
Main %name library.

%files -n %{libgdcmjpeg}
%defattr(-,root,root,-)
%{_libdir}/libgdcmjpeg*.so.%{jpeg_major}*

#------------------------------------------------------------------------------

%package -n python-gdcm
Summary: Python gdcm files
Group: Development/Python

%description -n python-gdcm
Python gdcm files.

%files -n python-gdcm
%defattr(-,root,root,-)
%py_platsitedir/*.py
%py_platsitedir/*.so
%exclude %py_platsitedir/vtkgdcm.py

#------------------------------------------------------------------------------

%package -n python-vtkgdcm
Summary: Python gdcm vtk files
Group: Development/Python
Requires: python-gdcm
Requires: python-vtk
Requires: %{libgdcmvtkgdcm}
Requires: %{libgdcmvtkgdcmPythonD}

%description -n python-vtkgdcm
Python gdcm vtk files.

%files -n python-vtkgdcm
%defattr(-,root,root,-)
%py_platsitedir/vtkgdcm.py

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig

%build
%cmake \
	-DGDCM_INSTALL_LIB_DIR=%_libdir \
	-DGDCM_INSTALL_MAN_DIR=%_mandir \
	-DGDCM_WRAP_PYTHON:BOOL=ON \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	-DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
	-DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	-DGDCM_PYTHON_SITEDIR=%{py_platsitedir} \
	-DGDCM_USE_VTK:BOOL=ON \
	-DVTK_DIR=%_libdir/vtk

%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot

