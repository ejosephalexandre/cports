pkgname = "haproxy"
pkgver = "2.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
]
hostmakedepends = ["linux-headers",
    "openssl-devel",
    "zlib-devel"
]
pkgdesc = "High Performance TCP/HTTP Load Balancer"
maintainer = "Erjo <erjo@cocoba.work>"
license = "GPL-2.0-or-later"
url = "https://www.haproxy.org"
source = f"https://www.haproxy.org/download/2.8/src/{pkgname}-{pkgver}.tar.gz"
sha256 = "698d6906d170946a869769964e57816ba3da3adf61ff75e89972b137f4658db0"
