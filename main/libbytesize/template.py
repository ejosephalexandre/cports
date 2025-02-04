pkgname = "libbytesize"
pkgver = "2.9"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "python",
    "gettext-tiny",
    "automake",
    "libtool",
]
makedepends = ["gmp-devel", "mpfr-devel", "pcre2-devel"]
pkgdesc = "Library for operations with sizes in bytes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libbytesize"
source = f"https://github.com/storaged-project/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bd0ea11ece2c2423382a7c4534679050e72a8ee91b4fdea3a7cc85199846d0c3"
# cba
options = ["!check"]


@subpackage("libbytesize-devel")
def _devel(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libbytesize-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python", "python-six"]

    return ["usr/lib/python*"]
