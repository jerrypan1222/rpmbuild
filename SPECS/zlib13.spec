Name:           zlib13
Version:        1.3.1
Release:        1%{?dist}
Summary:        zlib 1.3.1 (custom build in /opt)

License:        zlib
URL:            https://www.zlib.net
Source0:        zlib-1.3.1.tar.gz

# 安裝到 /opt/zlib-1.3.1 目錄下，不干擾系統套件
%define _prefix /opt/zlib-1.3.1
%define _libdir %{_prefix}/lib

# 禁用 debugsource（避免那個報錯）
%define debug_package %{nil}

%description
This is a custom build of zlib 1.3.1 installed in %{_prefix},
intended for use with custom OpenSSH 9.8p1 builds.

%prep
%autosetup -n zlib-%{version}

%build
./configure --prefix=%{_prefix}
make -j$(nproc)

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/share/man/man3/*
%doc README ChangeLog

%changelog
* Mon Jun 09 2025 You <you@example.com> - 1.3.1-1
- Custom build of zlib 1.3.1 under %{_prefix}

