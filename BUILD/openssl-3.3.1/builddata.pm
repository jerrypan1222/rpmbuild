package OpenSSL::safe::installdata;

use strict;
use warnings;
use Exporter;
our @ISA = qw(Exporter);
our @EXPORT = qw($PREFIX
                  $BINDIR $BINDIR_REL
                  $LIBDIR $LIBDIR_REL
                  $INCLUDEDIR $INCLUDEDIR_REL
                  $APPLINKDIR $APPLINKDIR_REL
                  $ENGINESDIR $ENGINESDIR_REL
                  $MODULESDIR $MODULESDIR_REL
                  $PKGCONFIGDIR $PKGCONFIGDIR_REL
                  $CMAKECONFIGDIR $CMAKECONFIGDIR_REL
                  $VERSION @LDLIBS);

our $PREFIX             = '/root/rpmbuild/BUILD/openssl-3.3.1';
our $BINDIR             = '/root/rpmbuild/BUILD/openssl-3.3.1/apps';
our $BINDIR_REL         = 'apps';
our $LIBDIR             = '/root/rpmbuild/BUILD/openssl-3.3.1';
our $LIBDIR_REL         = '.';
our $INCLUDEDIR         = '/root/rpmbuild/BUILD/openssl-3.3.1/include';
our $INCLUDEDIR_REL     = 'include';
our $APPLINKDIR         = '/root/rpmbuild/BUILD/openssl-3.3.1/ms';
our $APPLINKDIR_REL     = 'ms';
our $ENGINESDIR         = '/root/rpmbuild/BUILD/openssl-3.3.1/engines';
our $ENGINESDIR_REL     = 'engines';
our $MODULESDIR         = '/root/rpmbuild/BUILD/openssl-3.3.1/providers';
our $MODULESDIR_REL     = 'providers';
our $PKGCONFIGDIR       = '';
our $PKGCONFIGDIR_REL   = '';
our $CMAKECONFIGDIR     = '';
our $CMAKECONFIGDIR_REL = '';
our $VERSION            = '3.3.1';
our @LDLIBS             =
    # Unix and Windows use space separation, VMS uses comma separation
    split(/ +| *, */, '-lz -ldl -pthread ');

1;
