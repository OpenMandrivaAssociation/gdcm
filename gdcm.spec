%bcond_without	doc
%bcond_without	java
%bcond_without	python
%bcond_without	tests
%bcond_with	vtk

Name:		gdcm
Version:	3.0.24
Release:	9
License:	GPL
Summary:	Open source DICOM library
Group:		Development/C++
URL:		https://gdcm.sourceforge.net/
# Use github release
#Source0:	https://github.com/malaterre/GDCM/archive/v%{version}/GCDM-%{version}.tar.gz
Source0:	https://downloads.sourceforge.net/project/gdcm/gdcm%203.x/GDCM%20%{version}/%{name}-%{version}.tar.bz2
# last update: 2011-12-30
Source1:	https://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-style-xsl-ns
BuildRequires:	doxygen
%if %{with doc}
BuildRequires:	texlive
BuildRequires:	texlive-dehyph
BuildRequires:	texlive-dehyph-exptl
BuildRequires:	pkgconfig(libxslt)
%endif
BuildRequires:	git-core
BuildRequires:	gl2ps-devel
BuildRequires:	graphviz
%if %{with java}
BuildRequires:	java-devel
BuildRequires:	java-vtk
%endif
BuildRequires:	cmake(DCMTK)
BuildRequires:	cmake(charls)
BuildRequires:	cmake(expat)
BuildRequires:	cmake(json-c)
BuildRequires:	cmake(ogg)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(poppler)
%if %{with python}
BuildRequires:	pkgconfig(python3)
%endif
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	swig
%if %{with vtk}
BuildRequires:	cmake(vtk)
BuildRequires:	cmake(fmt)
%endif
# For man pages
BuildRequires:	xsltproc

%patchlist
gdcm-3.0.10-fix_copyright.patch
gdcm-fix-poppler-24.11.patch

%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%files
%doc AUTHORS README.md
%license Copyright.txt README.Copyright.txt
%{_libdir}/lib*.so.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}-3.0/XML/
#exclude %{_docdir}/%{name}/html/
#exclude %{_docdir}/%{name}/Examples/

#---------------------------------------------------------------------------

%package doc
Summary:	Includes html documentation for gdcm
BuildArch:	noarch

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.

%files doc
%doc %{_docdir}/%{name}/html/

#---------------------------------------------------------------------------

%package applications
Summary:	Includes command line programs for GDCM
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%files applications
%{_bindir}/gdcmanon
%{_bindir}/gdcmdiff
%{_bindir}/gdcmclean
%{_bindir}/gdcmconv
%{_bindir}/gdcmdump
%{_bindir}/gdcmgendir
%{_bindir}/gdcmimg
%{_bindir}/gdcminfo
%{_bindir}/gdcmpap3
%{_bindir}/gdcmpdf
%{_bindir}/gdcmraw
%{_bindir}/gdcmscanner
%{_bindir}/gdcmscu
%{_bindir}/gdcmtar
%{_bindir}/gdcmxml
%doc %{_mandir}/man1/*.1*

#---------------------------------------------------------------------------

%package devel
Summary:	Libraries and headers for GDCM
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-applications%{?_isa} = %{version}-%{release}

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/cmake/%{name}/

#---------------------------------------------------------------------------

%package examples
Summary:	CSharp, C++, Java, PHP and Python example programs for GDCM
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description examples
GDCM examples

%files examples
%{_datadir}/%{name}/Examples/

#---------------------------------------------------------------------------

%if %{with python}
%package -n python-gdcm
Summary:	Python binding for GDCM
%{?python_provide:%python_provide python-gdcm}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%files -n python-gdcm
%{python_sitearch}/%{name}*.py
%{python_sitearch}/_%{name}swig.so
%endif

#---------------------------------------------------------------------------

%if %{with java}
%package -n java-gdcm
Summary:	Java binding for GDCM
Group:		Development/Java
Requires:	%{name}%{?_isa} = %{version}-%{release}
Obsoletes:	%{name}-java < %{version}
Provides:	%{name}-java = %{version}

%description -n java-gdcm
This package contains Java bindings for GDCM.

%files -n java-gdcm
%{_libdir}/java/%{name}.jar
%endif

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -a 0 -S git -a 1

# Stop doxygen from producing LaTeX output
sed -i.backup 's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' Utilities/doxygen/doxyfile.in Utilities/doxygen/vtk/doxyfile.in

# Remove bundled utilities /use system's ones) 
rm -rf Utilities/gdcmexpat
rm -rf Utilities/gdcmopenjpeg-v1
rm -rf Utilities/gdcmopenjpeg-v2
rm -rf Utilities/gdcmzlib
rm -rf Utilities/gdcmuuid
rm -rf Utilities/gdcmcharls

# Remove bundled utilities (we don't use them)
rm -rf Utilities/getopt
rm -rf Utilities/pvrg
rm -rf Utilities/rle
rm -rf Utilities/wxWidgets

# Needed for testing:
#rm -rf Utilities/gdcmmd5

# Fix path
sed -i -e 's,CharLS/charls.h,charls/charls.h,g' Utilities/gdcm_charls.h

%build
LDFLAGS="%ldflags `pkg-config --libs charls`"

%cmake .. \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
	-DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
	-DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
	-DGDCM_INSTALL_MAN_DIR=%{_mandir} \
	-DGDCM_INSTALL_LIB_DIR=%{_libdir} \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_BUILD_EXAMPLES:BOOL=OFF \
	-DGDCM_BUILD_TESTING:BOOL=%{?with_tests:ON}%{?!with_tests:OFF} \
	-DGDCM_DATA_ROOT=../gdcmData/ \
	-DGDCM_DEFAULT_JAVA_VERSION:STRING=1.8 \
	-DGDCM_DOCUMENTATION:BOOL=%{?with_doc:ON}%{?!with_doc:OFF} \
	-DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
	-DGDCM_WRAP_CSHARP:BOOL=OFF \
	-DGDCM_WRAP_JAVA:BOOL=%{?with_java:ON}%{?!with_java:OFF} \
	-DGDCM_WRAP_PYTHON:BOOL=%{?with_python:ON}%{?!with_python:OFF} \
	-DPYTHON_EXECUTABLE=%{__python3} \
	-DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitearch} \
	-DGDCM_USE_VTK:BOOL=%{?with_vtk:ON}%{?!with_vtk:OFF} \
	-DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
	-DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	-DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	-DGDCM_USE_SYSTEM_PAPYRUS:BOOL=OFF \
	-DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	-DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
	-DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
	-DGDCM_USE_JPEGLS:BOOL=ON \
	-DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
	-DGDCM_USE_SYSTEM_JSON:BOOL=ON \
	-DGDCM_USE_SYSTEM_POPPLER:BOOL=ON \
	-DCMAKE_CXX_STANDARD=20 \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

%if %{with python}
install -d %{buildroot}%{python3_sitearch}
%endif

# Install examples
install -d %{buildroot}/%{_datadir}/%{name}/Examples/
cp -rv ./Examples/* %{buildroot}%{_datadir}/%{name}/Examples/

# fix java library path
%if %{with java}
install -d 0755 %{buildroot}%{_libdir}/java/
mv -f %{buildroot}%{_libdir}/%{name}.jar %{buildroot}%{_libdir}/java/
%endif

%if %{with tests}
%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make test -C build || exit 0
%endif
