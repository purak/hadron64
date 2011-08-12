metadata = """
summary @ Lists of the country, language, and currency names
homepage @ http://pkg-isocodes.alioth.debian.org/
license @ LGPL
src_url @ http://su-se.lunar-linux.org/lunar/mirrors/$fullname.tar.bz2
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("pkgconfigdir=/usr/lib/pkgconfig DESTDIR=%s" % install_dir)
