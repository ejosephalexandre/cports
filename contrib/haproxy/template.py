pkgname = "haproxy"
pkgver = "2.8.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
make_build_args = [
    "TARGET=linux-musl",
    "USE_OPENSSL=1",
    "USE_LUA=1",
    "USE_PCRE2=1"
]
makedepends = [ "gmake",
    "lua5.4-devel",
    "clang",
    "linux-headers",
    "pcre2-devel",
    "openssl-devel",
    "zlib-devel",
]
pkgdesc = "High Performance TCP/HTTP Load Balancer"
maintainer = "Erjo <erjo@cocoba.work>"
license = "GPL-2.0-or-later"
url = "https://www.haproxy.org"
source = f"{url}/download/2.8/src/{pkgname}-{pkgver}.tar.gz"
sha256 = "698d6906d170946a869769964e57816ba3da3adf61ff75e89972b137f4658db0"

def init_build(self):
    self.tool_flags["LD"] = self.tool_flags["CC"]

