pkgname = "turnstile"
pkgver = "0.1.6"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dmanage_rundir=true"]
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["linux-pam-devel"]
depends = ["dinit-chimera"]
pkgdesc = "Chimera user service manager and session tracker"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/turnstile"
source = f"https://github.com/chimera-linux/turnstile/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ea1b87ad153e97ecda698526eec1cbc9fee1cd2b134c43b449f35d9cec0a61bc"
hardening = ["vis", "cfi"]
options = ["brokenlinks", "!splitdinit"]


def post_install(self):
    self.install_license("COPYING.md")
    # just make sure it exists
    self.install_dir("usr/lib/dinit.d/user/boot.d", empty=True)
    # linger
    self.install_dir("var/lib/turnstiled/linger", empty=True)
    # also default systemwide link
    self.install_dir("usr/lib/dinit.d/boot.d")
    self.install_link("../turnstiled", "usr/lib/dinit.d/boot.d/turnstiled")
