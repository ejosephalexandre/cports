pkgname = "sudo"
pkgver = "1.9.14p3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",
    "--with-secure-path",
    "--with-all-insults",
    "--with-env-editor",
    "--with-passprompt",
    "--without-pam",
]
make_dir = "build"
pkgdesc = "Allows a system administrator to delegate authority"
maintainer = "Erjo <erjo@cocoba.work>"
license = "ISC"
url = "https://www.sudo.ws"
source = f"https://www.sudo.ws/dist/{pkgname}-{pkgver}.tar.gz"
sha256 = "a08318b1c4bc8582c004d4cd9ae2903abc549e7e46ba815e41fe81d1c0782b62"

configure_gen = []


