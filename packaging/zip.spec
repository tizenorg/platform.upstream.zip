#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           zip
Version:        3.0
Release:        1
License:        BSD-3-Clause
%define file_version 30
Summary:        File compression program
Url:            http://www.info-zip.org/
Group:          Productivity/Archiving/Compression
Source:         %{name}-%{version}.tar.bz2

%description
Zip is a compression and file packaging utility. It is compatible with
PKZIP(tm) 2.04g (Phil Katz ZIP) for MS-DOS systems.

%prep
%setup -q -n zip%{file_version}

%build
make %{?_smp_mflags} -f unix/Makefile prefix=/usr CC="gcc %{optflags} -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" generic_gcc

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_mandir}/man1
make install -f unix/Makefile BINDIR=%{buildroot}/usr/bin MANDIR=%{buildroot}%{_mandir}/man1

%docs_package

%files
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/zip
%{_bindir}/zipcloak
%{_bindir}/zipnote
%{_bindir}/zipsplit

%changelog
