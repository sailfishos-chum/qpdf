# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       qpdf

# >> macros
# << macros
%define __cmake_in_source_build OFF

Summary:    PDF transformation/manipulation program + library
Version:    11.3.0
Release:    0
Group:      Applications
License:    ASL 2.0 or Artistic 2.0
URL:        https://qpdf.sourceforge.io/
Source0:    %{name}-%{version}.tar.gz
Source100:  qpdf.yaml
Source101:  qpdf-rpmlintrc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake
BuildRequires:  perl
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  cmake

%description
QPDF is a command-line tool and C++ library that performs
content-preserving transformations on PDF files. It supports
linearization, encryption, and numerous other features. It can also
be used for splitting and merging files, creating PDF files (but you
have to supply all the content yourself), and inspecting files for
study or analysis. QPDF does not render PDFs or perform text
extraction, and it does not contain higher-level interfaces for
working with page contents. It is a low-level tool for working with
the structure of PDF files and can be a valuable tool for anyone who
wants to do programmatic or command-line-based manipulation of PDF
files.

%if "%{?vendor}" == "chum"
PackageName: QPDF
Type: console-application
PackagerName: nephros
Categories:
 - Office
 - Utility
 - Library
Custom:
  Repo: %{url}
#  PackagingRepo: %{url}
Icon: https://qpdf.sourceforge.io/qpdf.svg
Url:
  Homepage: https://qpdf.sourceforge.io/
  Help: https://qpdf.readthedocs.io/en/stable/
  Bugtracker: https://github.com/qpdf/qpdf/issues/
  Donation: https://www.paypal.com/cgi-bin/webscr?item_name=Donation+to+QPDF&cmd=_donations&business=ejb%40ql.org
%endif


%package tools
Summary:    Library files for %{name}
Group:      Applications

%description tools
QPDF is a command-line tool and C++ library that performs
content-preserving transformations on PDF files. It supports
linearization, encryption, and numerous other features. It can also
be used for splitting and merging files, creating PDF files (but you
have to supply all the content yourself), and inspecting files for
study or analysis. QPDF does not render PDFs or perform text
extraction, and it does not contain higher-level interfaces for
working with page contents. It is a low-level tool for working with
the structure of PDF files and can be a valuable tool for anyone who
wants to do programmatic or command-line-based manipulation of PDF
files.


%if "%{?vendor}" == "chum"
PackageName: QPDF Tools
PackagerName: nephros
Type: console-application
Categories:
 - Office
 - Utility
Icon: https://qpdf.sourceforge.io/qpdf.svg
Custom:
  Repo: %{url}
Url:
  Homepage: https://qpdf.sourceforge.io/
  Help: https://qpdf.readthedocs.io/en/stable/
  Bugtracker: https://github.com/qpdf/qpdf/issues/
  Donation: https://www.paypal.com/cgi-bin/webscr?item_name=Donation+to+QPDF&cmd=_donations&business=ejb%40ql.org
%endif


%package -n lib%{name}
Summary:    Library files for %{name}
Group:      Applications
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}
QPDF is a command-line tool and C++ library that performs
content-preserving transformations on PDF files. It supports
linearization, encryption, and numerous other features. It can also
be used for splitting and merging files, creating PDF files (but you
have to supply all the content yourself), and inspecting files for
study or analysis. QPDF does not render PDFs or perform text
extraction, and it does not contain higher-level interfaces for
working with page contents. It is a low-level tool for working with
the structure of PDF files and can be a valuable tool for anyone who
wants to do programmatic or command-line-based manipulation of PDF
files.


%if "%{?vendor}" == "chum"
PackagerName: nephros
Categories:
 - Library
Icon: https://qpdf.sourceforge.io/qpdf.svg
Custom:
  Repo: %{url}
Url:
  Homepage: https://qpdf.sourceforge.io/
  Help: https://qpdf.readthedocs.io/en/stable/
  Bugtracker: https://github.com/qpdf/qpdf/issues/
  Donation: https://www.paypal.com/cgi-bin/webscr?item_name=Donation+to+QPDF&cmd=_donations&business=ejb%40ql.org
%endif


%package devel
Summary:    Development files for %{name}
Group:      Applications
Requires:   lib%{name} = %{version}-%{release}

%description devel
QPDF is a command-line tool and C++ library that performs
content-preserving transformations on PDF files. It supports
linearization, encryption, and numerous other features. It can also
be used for splitting and merging files, creating PDF files (but you
have to supply all the content yourself), and inspecting files for
study or analysis. QPDF does not render PDFs or perform text
extraction, and it does not contain higher-level interfaces for
working with page contents. It is a low-level tool for working with
the structure of PDF files and can be a valuable tool for anyone who
wants to do programmatic or command-line-based manipulation of PDF
files.

%if "%{?vendor}" == "chum"
PackagerName: nephros
Categories:
 - Library
Icon: https://qpdf.sourceforge.io/qpdf.svg
Custom:
  Repo: %{url}
Url:
  Homepage: https://qpdf.sourceforge.io/
  Help: https://qpdf.readthedocs.io/en/stable/
  Bugtracker: https://github.com/qpdf/qpdf/issues/
  Donation: https://www.paypal.com/cgi-bin/webscr?item_name=Donation+to+QPDF&cmd=_donations&business=ejb%40ql.org
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
mkdir -p build/
pushd build
# << build pre

%cmake .  \
    -S ../ \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_STATIC_LIBS=OFF \
    -DCMAKE_POSITION_INDEPENDENT_CODE=True \
    -DINSTALL_MANUAL=OFF \
    -DINSTALL_EXAMPLES=OFF \
    -DREQUIRE_CRYPTO_OPENSSL=ON \
    -DDEFAULT_CRYPTO_OPENSSL=ON

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
pushd build
# << install pre
%make_install

# >> install post
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_docdir}
# << install post

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name} -p /sbin/ldconfig


%files tools
%defattr(-,root,root,-)
%license LICENSE.txt
%{_bindir}/*
# >> files tools
# << files tools

%files -n lib%{name}
%defattr(-,root,root,-)
%license LICENSE.txt
%{_libdir}/*.so.*
# >> files lib%{name}
# << files lib%{name}

%files devel
%defattr(-,root,root,-)
%license LICENSE.txt
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*
# >> files devel
# << files devel
