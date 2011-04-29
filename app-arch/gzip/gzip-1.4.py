metadata = """
summary @ GNU compression utility
homepage @ http://www.gnu.org/software/gzip/
license @ GPL-3
src_url @ ftp://ftp.gnu.org/pub/gnu/$name/$fullname.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    export("DEFS", "NO_ASM")
    conf()

def install():
    linstall()
    makedirs("bin")
    for i in ('gunzip', 'gzip', 'uncompress', 'zcat'):
        move('%s/usr/bin/%s' % (install_dir, i), '/bin/%s' % i)
