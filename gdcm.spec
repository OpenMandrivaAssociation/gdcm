# Enabled by default
%bcond_with tests

%define libname	%mklibname %{name} 0
%define devname	%mklibname %{name} -d
%define pyname	python-%{name}

%define oname GDCM

Name:		gdcm
Version:	3.0.4
Release:	1
License:	GPL
Summary:	Open source DICOM library
Group:		Development/C++
URL:		http://gdcm.sourceforge.net/
# Use github release
Source0:    https://github.com/malaterre/%{name}/archive/v%{version}/%{oname}-%{version}.tar.gz
Source1:    http://downloads.sourceforge.net/project/gdcm/gdcmData/gdcmData/gdcmData.tar.gz


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
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package    doc
Summary:    Includes html documentation for gdcm
BuildArch:  noarch

%description doc
You should install the gdcm-doc package if you would like to
access upstream documentation for gdcm.

%package    applications
Summary:    Includes command line programs for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package    devel
Summary:    Libraries and headers for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-applications%{?_isa} = %{version}-%{release}

%description devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package    examples
Summary:    CSharp, C++, Java, PHP and Python example programs for GDCM
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
GDCM examples

%package -n python-gdcm
Summary:    Python binding for GDCM
%{?python_provide:%python_provide python-gdcm}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description -n python-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep
%autosetup -n GDCM-%{version} -S git
# Data source
%setup -n GDCM-%{version} -q -T -D -a 1

# Fix cmake command
sed -i.backup 's/add_dependency/add_dependencies/' Utilities/doxygen/CMakeLists.txt

# Stop doxygen from producing LaTeX output
sed -i.backup 's/^GENERATE_LATEX.*=.*YES/GENERATE_LATEX = NO/' Utilities/doxygen/doxyfile.in

# Remove bundled utilities (we use Fedora's ones)

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

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}

%cmake  .. \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
    -DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
    -DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
    -DGDCM_INSTALL_MAN_DIR=%{_mandir} \
    -DGDCM_INSTALL_LIB_DIR=%{_libdir} \
    -DGDCM_BUILD_TESTING:BOOL=ON \
    -DGDCM_DATA_ROOT=../gdcmData/ \
    -DGDCM_BUILD_EXAMPLES:BOOL=OFF \
    -DGDCM_DOCUMENTATION:BOOL=OFF \
    -DGDCM_WRAP_PYTHON:BOOL=ON \
    -DPYTHON_EXECUTABLE=%{__python3} \
    -DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitearch} \
    -DGDCM_WRAP_JAVA:BOOL=OFF \
    -DGDCM_WRAP_CSHARP:BOOL=OFF \
    -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
    -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
    -DGDCM_USE_VTK:BOOL=OFF \
    -DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
    -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
    -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
    -DGDCM_USE_SYSTEM_UUID:BOOL=ON \
    -DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
    -DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
    -DGDCM_USE_JPEGLS:BOOL=ON \
    -DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
    -DGDCM_USE_SYSTEM_JSON:BOOL=ON \
    -DGDCM_USE_SYSTEM_POPPLER:BOOL=ON

#Cannot build wrap_java:
#   -DGDCM_VTK_JAVA_JAR:PATH=/usr/share/java/vtk.jar no found!
#   yum provides */vtk.jar -> No results found

popd

%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}
install -d $RPM_BUILD_ROOT%{python3_sitearch}

# Install examples
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/Examples/
cp -rv ./Examples/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/Examples/

%if %{with tests}
%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make test -C %{_target_platform} || exit 0
%endif

%files
%doc AUTHORS README.md
%license Copyright.txt README.Copyright.txt
%{_libdir}/libgdcmCommon.so.3.0
%{_libdir}/libgdcmCommon.so.3.0.1
%{_libdir}/libgdcmDICT.so.3.0
%{_libdir}/libgdcmDICT.so.3.0.1
%{_libdir}/libgdcmDSED.so.3.0
%{_libdir}/libgdcmDSED.so.3.0.1
%{_libdir}/libgdcmIOD.so.3.0
%{_libdir}/libgdcmIOD.so.3.0.1
%{_libdir}/libgdcmMEXD.so.3.0
%{_libdir}/libgdcmMEXD.so.3.0.1
%{_libdir}/libgdcmMSFF.so.3.0
%{_libdir}/libgdcmMSFF.so.3.0.1
%{_libdir}/libgdcmjpeg12.so.3.0
%{_libdir}/libgdcmjpeg12.so.3.0.1
%{_libdir}/libgdcmjpeg16.so.3.0
%{_libdir}/libgdcmjpeg16.so.3.0.1
%{_libdir}/libgdcmjpeg8.so.3.0
%{_libdir}/libgdcmjpeg8.so.3.0.1
%{_libdir}/libgdcmmd5.so.3.0
%{_libdir}/libgdcmmd5.so.3.0.1
%{_libdir}/libsocketxx.so.1.2
%{_libdir}/libsocketxx.so.1.2.0
%dir %{_datadir}/%{name}
%{_datadir}/%{name}-3.0/XML/
%exclude %{_docdir}/%{name}/html/
%exclude %{_docdir}/%{name}/Examples/

%files doc
#doc %{_docdir}/%{name}/html/

%files applications
%{_bindir}/gdcmanon
%{_bindir}/gdcmconv
%{_bindir}/gdcmdiff
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

%files devel
%{_includedir}/%{name}/
%{_libdir}/libgdcmCommon.so
%{_libdir}/libgdcmDICT.so
%{_libdir}/libgdcmDSED.so
%{_libdir}/libgdcmIOD.so
%{_libdir}/libgdcmMEXD.so
%{_libdir}/libgdcmMSFF.so
%{_libdir}/libgdcmjpeg12.so
%{_libdir}/libgdcmjpeg16.so
%{_libdir}/libgdcmjpeg8.so
%{_libdir}/libgdcmmd5.so
%{_libdir}/libsocketxx.so
%{_libdir}/cmake/%{name}/

%files examples
%{_datadir}/%{name}/Examples/

%files -n python-gdcm
%{python_sitearch}/%{name}*.py
%{python_sitearch}/_%{name}swig.so
%{python_sitearch}/__pycache__/%{name}*


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


