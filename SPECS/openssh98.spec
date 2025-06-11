Name:           openssh
Version:        9.8p1
Release:        1%{?dist}
Summary:        OpenSSH implementation of SSH protocol

License:        BSD
URL:            https://www.openssh.com
Source0:        openssh-%{version}.tar.gz
Source1:        sshd.service
Source2:        sshd.pam

BuildRequires:  pam-devel zlib13 openssl33 chrpath
Requires:       pam zlib13 openssl33

# 禁用 RPATH 檢查
%define _disable_rpath 1
%define debug_package %{nil}
%global __brp_strip_static_archive %{nil}
%global __brp_compress %{nil}

%description
OpenSSH is a free version of the SSH connectivity tools that technical users
rely on. OpenSSH encrypts all traffic and provides secure tunneling and
authentication.

%prep
%autosetup -n openssh-%{version}

%build
export CFLAGS="-I/opt/zlib-1.3.1/include -I/opt/openssl-3.3.1/include"
export LDFLAGS="-L/opt/zlib-1.3.1/lib -L/opt/openssl-3.3.1/lib64"
./configure --prefix=/usr \
            --sysconfdir=/etc/ssh \
            --libexecdir=/usr/libexec/openssh \
            --with-pam \
            --with-privsep-path=/var/lib/sshd \
            --with-ssl-dir=/opt/openssl-3.3.1 \
            --with-zlib=/opt/zlib-1.3.1
make -j$(nproc)

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# 建立必要目錄
mkdir -p %{buildroot}/var/lib/sshd
chmod 700 %{buildroot}/var/lib/sshd

# 安裝 pam 與 systemd 服務檔案
install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/sshd.service
install -D -m 644 %{SOURCE2} %{buildroot}/etc/pam.d/sshd

# 移除所有 binary 的 RPATH
find %{buildroot} -type f -exec chrpath --delete {} + 2>/dev/null || :

%post
%systemd_post sshd.service
if [ ! -f /etc/ssh/ssh_host_rsa_key ]; then
    /usr/bin/ssh-keygen -A
fi
chmod 600 /etc/ssh/ssh_host_*_key 2>/dev/null || :

%preun
%systemd_preun sshd.service

%postun
%systemd_postun_with_restart sshd.service

%files
%defattr(-,root,root,-)
/usr/bin/*
/usr/sbin/*
/usr/libexec/openssh/*
%dir /etc/ssh
%config(noreplace) /etc/ssh/sshd_config
%config(noreplace) /etc/ssh/ssh_config
/etc/ssh/moduli
/etc/pam.d/sshd
/usr/lib/systemd/system/sshd.service
/var/lib/sshd
%doc README.md
%license LICENCE

%{_mandir}/man1/scp.1*
%{_mandir}/man1/sftp.1*
%{_mandir}/man1/ssh.1*
%{_mandir}/man1/ssh-add.1*
%{_mandir}/man1/ssh-agent.1*
%{_mandir}/man1/ssh-keygen.1*
%{_mandir}/man1/ssh-keyscan.1*
%{_mandir}/man5/moduli.5*
%{_mandir}/man5/ssh_config.5*
%{_mandir}/man5/sshd_config.5*
%{_mandir}/man8/sshd.8*
%{_mandir}/man8/sftp-server.8*
%{_mandir}/man8/ssh-keysign.8*
%{_mandir}/man8/ssh-pkcs11-helper.8*
%{_mandir}/man8/ssh-sk-helper.8*


%changelog
* Mon Jun 09 2025 DevOpsGPT <you@example.com> - 9.8p1-1
- Initial custom build with zlib-1.3.1 and openssl-3.3.1

