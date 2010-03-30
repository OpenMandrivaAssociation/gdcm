%define name	gdcm
%define libname	%mklibname %{name} 0
%define devname	%mklibname %{name} -d
%define pyname	python-%{name}

Name:		%{name}
Version:	2.0.14
Release:	%mkrel 1
License:	GPL
Summary:	GDCM is an open source DICOM library
Group:		Development/C++
URL:		http://gdcm.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

# FIXME itk package is broken but should be optional here
#BuildRequires:	itk-devel
BuildRequires:	cmake
BuildRequires:	expat-devel
BuildRequires:	jpeg-devel
BuildRequires:	libuuid-devel
BuildRequires:	openjpeg-devel
BuildRequires:	doxygen
BuildRequires:	python-vtk-devel
BuildRequires:	swig
BuildRequires:	tetex-latex
BuildRequires:	vtk-devel
BuildRequires:	zlib-devel
%py_requires -d

Patch0:		gdcm-2.0.14-rpm-cmake.patch
Patch1:		gdcm-2.0.14-python-2.6.patch

%description
GDCM is an open source DICOM library. It is meant to deal with DICOM files
(as specified in part 10 of the DICOM standard). It offers some compatibility
with ACR-NEMA 1.0 & 2.0 files (raw files). It is written in C++ and offers
wrapping to the following target languages (via the use of swig):
    * Python (supported),
    * C# (supported),
    * Java (testing),
    * PHP (experimental). 

It attempts to support all possible DICOM image encodings, namely:

    * RAW,
    * JPEG lossy 8 & 12 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG lossless 8-16 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG 2000 reversible & irreversible (ITU-T T.800, ISO/IEC IS 15444-1),
    * RLE,
    * Deflated (compression at DICOM Dataset level),
    * JPEG-LS (testing) (ITU-T T.87, ISO/IEC IS 14495-1),
    * JPEG 2000 Multi-component reversible & irreversible (ISO/IEC IS 15444-2)
      (not supported for now),
    * MPEG-2 (not supported for now). 

GDCM is designed under the XP definition and has a nightly dashboard
(CMake/CTest/Dart).

%files
%defattr(-,root,root,-)
%dir %{_datadir}/gdcm
%{_datadir}/gdcm/*
%{_bindir}/*
%{_mandir}/*/*

#-----------------------------------------------------------------------
%define libgdcmCommon	%mklibname gdcmcommon	2.0
%define libgdcmDICT	%mklibname gdcmdict	2.0
%define libgdcmIOD	%mklibname gdcmiod	2.0
%define libgdcmDSED	%mklibname gdcmdsed	2.0
%define libgdcmMSFF	%mklibname gdcmmsff	2.0
%define libgdcmvtkgdcm	%mklibname vtkgdcm	2.0
%define libgdcmjpeg	%mklibname gdcmjpeg	8
%package	-n %{libname}
Summary:	Grassroots DICOM library
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	%{libgdcmCommon} < %{version}-%{release}
Obsoletes:	%{libgdcmDICT} < %{version}-%{release}
Obsoletes:	%{libgdcmIOD} < %{version}-%{release}
Obsoletes:	%{libgdcmDSED} < %{version}-%{release}
Obsoletes:	%{libgdcmMSFF} < %{version}-%{release}
Obsoletes:	%{libgdcmvtkgdcm} < %{version}-%{release}
# don't conflict with libgdcmjpeg6.12
Provides:	%{libgdcmjpeg} = %{version}-%{release}

%description	-n %{libname}
GDCM is an open source DICOM library. It is meant to deal with DICOM files
(as specified in part 10 of the DICOM standard). It offers some compatibility
with ACR-NEMA 1.0 & 2.0 files (raw files). It is written in C++ and offers
wrapping to the following target languages (via the use of swig):
    * Python (supported),
    * C# (supported),
    * Java (testing),
    * PHP (experimental). 

It attempts to support all possible DICOM image encodings, namely:

    * RAW,
    * JPEG lossy 8 & 12 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG lossless 8-16 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG 2000 reversible & irreversible (ITU-T T.800, ISO/IEC IS 15444-1),
    * RLE,
    * Deflated (compression at DICOM Dataset level),
    * JPEG-LS (testing) (ITU-T T.87, ISO/IEC IS 14495-1),
    * JPEG 2000 Multi-component reversible & irreversible (ISO/IEC IS 15444-2)
      (not supported for now),
    * MPEG-2 (not supported for now). 

GDCM is designed under the XP definition and has a nightly dashboard
(CMake/CTest/Dart).

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

#-----------------------------------------------------------------------
%package	-n %{devname}
Summary:	Grassroots DICOM library
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
GDCM is an open source DICOM library. It is meant to deal with DICOM files
(as specified in part 10 of the DICOM standard). It offers some compatibility
with ACR-NEMA 1.0 & 2.0 files (raw files). It is written in C++ and offers
wrapping to the following target languages (via the use of swig):
    * Python (supported),
    * C# (supported),
    * Java (testing),
    * PHP (experimental). 

It attempts to support all possible DICOM image encodings, namely:

    * RAW,
    * JPEG lossy 8 & 12 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG lossless 8-16 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG 2000 reversible & irreversible (ITU-T T.800, ISO/IEC IS 15444-1),
    * RLE,
    * Deflated (compression at DICOM Dataset level),
    * JPEG-LS (testing) (ITU-T T.87, ISO/IEC IS 14495-1),
    * JPEG 2000 Multi-component reversible & irreversible (ISO/IEC IS 15444-2)
      (not supported for now),
    * MPEG-2 (not supported for now). 

GDCM is designed under the XP definition and has a nightly dashboard
(CMake/CTest/Dart).

%files		-n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib*.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

#-----------------------------------------------------------------------
%package	-n %{pyname}
Summary:	Grassroots DICOM library
Group:		Development/Python
Obsoletes:	python-vtkgdcm < %{version}-%{release}
Provides:	python-vtkgdcm = %{version}-%{release}

%description	-n %{pyname}
GDCM is an open source DICOM library. It is meant to deal with DICOM files
(as specified in part 10 of the DICOM standard). It offers some compatibility
with ACR-NEMA 1.0 & 2.0 files (raw files). It is written in C++ and offers
wrapping to the following target languages (via the use of swig):
    * Python (supported),
    * C# (supported),
    * Java (testing),
    * PHP (experimental). 

It attempts to support all possible DICOM image encodings, namely:

    * RAW,
    * JPEG lossy 8 & 12 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG lossless 8-16 bits (ITU-T T.81, ISO/IEC IS 10918-1),
    * JPEG 2000 reversible & irreversible (ITU-T T.800, ISO/IEC IS 15444-1),
    * RLE,
    * Deflated (compression at DICOM Dataset level),
    * JPEG-LS (testing) (ITU-T T.87, ISO/IEC IS 14495-1),
    * JPEG 2000 Multi-component reversible & irreversible (ISO/IEC IS 15444-2)
      (not supported for now),
    * MPEG-2 (not supported for now). 

GDCM is designed under the XP definition and has a nightly dashboard
(CMake/CTest/Dart).

%files		-n %{pyname}
%defattr(-,root,root)
%{py_platsitedir}/*

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1
%patch1 -p1

#-----------------------------------------------------------------------
%build
%cmake \
	-DGDCM_USE_ITK:BOOL=OFF \
	-DGDCM_USE_VTK:BOOL=ON \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_INSTALL_LIB_DIR:PATH=%{_libdir} \
	-DGDCM_INSTALL_INCLUDE_DIR:PATH=%{_includedir}/%{name} \
	-DGDCM_INSTALL_DOC_DIR:PATH=%{_docdir}/%{name} \
	-DGDCM_INSTALL_MAN_DIR=%{_mandir} \
	-DGDCM_WRAP_PYTHON:BOOL=ON \
	-DGDCM_WRAP_CSHARP:BOOL=OFF \
	-DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	-DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	-DGDCM_USE_SYSTEM_ZLIB:BOOL=ON
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std -C build

mv -f %{buildroot}%{_libdir}/gdcm{-2.0,}
mv -f %{buildroot}%{_datadir}/gdcm{-2.0,}
pushd %{buildroot}%{_libdir}
  for f in lib*.so.2.0.14; do
    ln -sf $f `echo $f | sed -e 's/.2.0.14//'`
  done
popd

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
