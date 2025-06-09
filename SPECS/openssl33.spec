Name:           openssl33
Version:        3.3.1
Release:        1%{?dist}
Summary:        OpenSSL 3.3.1 - cryptographic and SSL/TLS toolkit

License:        OpenSSL
URL:            https://www.openssl.org/
Source0:        openssl-%{version}.tar.gz

BuildRequires:  perl, perl-IPC-Cmd, make, gcc
Requires:       libc.so.6()(64bit)

%define install_path /opt/openssl-%{version}
%define debug_package %{nil}
%global __brp_compress %{nil}

%description
OpenSSL is a robust toolkit for the TLS and SSL protocols and general-purpose cryptography library.
This version installs into %{install_path} and does not conflict with the system OpenSSL.

%prep
%autosetup -n openssl-%{version}

%build
./Configure linux-x86_64 \
    --prefix=%{install_path} \
    --openssldir=%{install_path}/ssl \
    shared zlib

make -j$(nproc)

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# 安裝 LICENSE 和 README.md 到 doc 路徑
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp -p %{_builddir}/openssl-%{version}/README.md %{buildroot}%{_defaultdocdir}/%{name}/

# Symlink for user access (optional)
mkdir -p %{buildroot}/usr/bin
ln -sf %{install_path}/bin/openssl %{buildroot}/usr/bin/openssl33

# Linker config for runtime libs
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{install_path}/lib64" > %{buildroot}/etc/ld.so.conf.d/openssl33.conf

%files
%doc README.md
%{install_path}
%config(noreplace) /etc/ld.so.conf.d/openssl33.conf
/usr/bin/openssl33

