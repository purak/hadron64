metadata = """
summary @ Standard GNU file utilities (chmod, cp, dd, dir, ls...), text utilities (sort, tr, head, wc..), and shell utilities (whoami, who,...)
license @ GPL-3
homepage @ http://www.gnu.org/software/coreutils/
src_url @ http://ftp.gnu.org/gnu/coreutils/coreutils-8.10.tar.gz
arch @ ~x86
"""

depends = """
runtime @ sys-libs/glibc dev-libs/pcre
        sys-apps/attr sys-libs/pam
        sys-apps/acl dev-libs/gmp
        sys-libs/libcap
"""

def prepare():
    patch(level=1)
    autoreconf("-v")

def configure():
    conf("--enable-install-program=su",
         "--enable-no-install-program=groups,hostname,kill,uptime",
         "--enable-pam")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    fhs = ('cat', 'chgrp', 'chmod', 'chown', 'cp', 'date', 'dd', 'df', 'echo',
            'false', 'ln', 'ls', 'mkdir', 'mknod', 'mv', 'pwd', 'rm', 'rmdir',
            'stty', 'su', 'sync', 'true', 'uname')
    for f in fhs:
        move("/usr/bin/%s" %  f, "/bin/%s" %  f)

    bins = ('cut', 'dir', 'dircolors', 'du', 'install', 'mkfifo', 'readlink',
            'shred', 'sleep', 'touch', 'tr', 'vdir')
    for b in bins:
        move("/usr/bin/%s" %  b, "/bin/%s" %  b)

    makesym("/bin/sleep", "/usr/bin/sleep")
