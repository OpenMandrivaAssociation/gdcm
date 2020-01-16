%define libname	%mklibname %{name} 0
%define devname	%mklibname %{name} -d
%define pyname	python-%{name}

Name:		gdcm
Version:	3.0.4
Release:	1
License:	GPL
Summary:	Open source DICOM library
Group:		Development/C++
URL:		http://gdcm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/gdcm/%{name}-%{version}.tar.bz2

BuildRequires:  CharLS-devel >= 2.0
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libxslt-devel
#BuildRequires:  dcmtk-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  git-core
BuildRequires:  graphviz
BuildRequires:  gl2ps-devel
BuildRequires:  libogg-devel
BuildRequires:  libtheora-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(osmesa)
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  poppler-devel
BuildRequires:  python-devel
BuildRequires:  swig
BuildRequires:  sqlite-devel
BuildRequires:  json-c-devel
BuildRequires:  libxml2-devel

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
%define libgdcmCommon		%mklibname gdcmcommon		2.0
%define libgdcmDICT		%mklibname gdcmdict		2.0
%define libgdcmIOD		%mklibname gdcmiod		2.0
%define libgdcmDSED		%mklibname gdcmdsed		2.0
%define libgdcmMSFF		%mklibname gdcmmsff		2.0
%define libgdcmvtkgdcm		%mklibname vtkgdcm		2.0
%define libgdcmvtkgdcmPythonD	%mklibname vtkgdcmpythonp	2.0
%define libgdcmjpeg		%mklibname gdcmjpeg		8
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
Obsoletes:	%{libgdcmvtkgdcmPythonD} < %{version}-%{release}
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
%{_libdir}/lib*.so.*

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
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libvtkgdcmPythonD.so
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
%{py_platsitedir}/*
%{_libdir}/libvtkgdcmPythonD.so

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

#-----------------------------------------------------------------------
%build
%cmake \
	-DGDCM_USE_ITK:BOOL=ON \
	-DGDCM_USE_VTK:BOOL=ON \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_INSTALL_BIN_DIR:PATH=%{_bindir} \
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
make

#-----------------------------------------------------------------------
%install
rm -fr %buildroot
%makeinstall_std -C build

mv -f %{buildroot}%{_libdir}/gdcm{-2.0,}
mv -f %{buildroot}%{_datadir}/gdcm{-2.0,}
pushd %{buildroot}%{_libdir}
  for f in lib*.so.%{version}; do
    ln -sf $f `echo $f | sed -e 's/.%{version}//'`
  done
popd

#-----------------------------------------------------------------------
%clean


%changelog
* Thu Nov 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0.18-1mdv2012.0
+ Revision: 731240
- Update to latest upstream release gdcm 2.0.18

* Tue May 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0.16-3
+ Revision: 675919
- Rebuild

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.16-2mdv2011.0
+ Revision: 593528
+ rebuild (emptylog)

* Tue Oct 05 2010 Funda Wang <fwang@mandriva.org> 2.0.16-1mdv2011.0
+ Revision: 583077
- New version 2.0.16

* Thu Jul 22 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.15-1mdv2011.0
+ Revision: 556738
- Update to version 2.0.15 and rebuild with newer itk and vtk.

* Thu May 20 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.14-3mdv2010.1
+ Revision: 545502
- Enable itk support.

* Wed Mar 31 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.14-2mdv2010.1
+ Revision: 530514
+ rebuild (emptylog)

* Tue Mar 30 2010 Paulo Andrade <pcpa@mandriva.com.br> 2.0.14-1mdv2010.1
+ Revision: 528945
- Update to latest upstream release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.12-3mdv2010.1
+ Revision: 522710
- rebuilt for 2010.1

* Fri Sep 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2.0.12-2mdv2010.0
+ Revision: 431511
- Initial compilation
- imported package gdcm


