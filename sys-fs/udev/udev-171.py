metadata = """
summary @ Linux dynamic and persistent device naming support
homepage @ http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev.html
license @ GPL-2
src_url @ http://www.kernel.org/pub/linux/utils/kernel/hotplug/$fullname.tar.bz2
"""

depends = """
runtime @ sys-libs/glibc sys-apps/coreutils sys-apps/module-init-tools
          sys-apps/util-linux sys-libs/glib dev-util/gperf dev-libs/libusb:0
"""

#def prepare():
#    patch(level=1)

def configure():
    raw_configure("--sysconfdir=/etc", 
        "--sbindir=/sbin",
        "--with-rootlibdir=/lib", 
        "--libexecdir=/lib/udev",
        "--with-systemdsystemunitdir=/lib/systemd/system",
        "--disable-introspection",
        "--enable-logging",
        "--enable-rule_generator",
        "--enable-hwdb",
        "--with-pci-ids-path=/usr/share/misc/pci.ids",
        "--with-usb-ids-path=/usr/share/misc/usb.ids",
        "--enable-udev_acl",
        "--enable-gudev",
        "--enable-keymap",
        "--enable-floppy",
        "--enable-edd",
        "--enable-action_modeswitch")

def install():
    raw_install('DESTDIR=%s' % install_dir)
    
    #insfile("%s/80-drivers.rules" % filesdir, "/lib/udev/rules.d/80-drivers.rules")
    insfile("%s/81-arch.rules" % filesdir, "/lib/udev/rules.d/81-arch.rules")
    for rule in ("11-media-by-label-auto-mount.rules",  "11-sd-cards-auto-mount.rules"):
        insfile("%s/%s" % (filesdir, rule), "/lib/udev/rules.d/%s" % rule)

    #insfile("%s/load-modules.sh" % filesdir, "/lib/udev/load-modules.sh")
    #insfile("%s/cdsymlinks.sh" % filesdir, "/lib/udev/cdsymlinks.sh")

    for d in ("net", "pts", "shm", "hugepages"):
        makedirs("/lib/udev/devices/%s" % d)

    makesym("/lib/udev/scsi_id", "/sbin/scsi_id")
    
    makedirs("/etc/udev/rules.d")
    
    insdoc("COPYING", "ChangeLog", "README", "TODO", "extras/keymap/README.keymap.txt")

def post_install():
    from lpms import shelltools
    def create_node(params):
        return shelltools.system("mknod "+params, show=False)

    create_node("-m 0600 /lib/udev/devices/console c 5 1 &>/dev/null")
    create_node("-m 0660 /lib/udev/devices/loop0 b 7 0 &>/dev/null")
    
    nodes = {"null": "1 3", "zero": "1 5", "kmsg": "1 11", "net/tun": "10 200",
            "fuse": "10 200", "ppp": "108 0"}
    for i in nodes:
        create_node("-m 0666 /lib/udev/devices/%s c %s &>/dev/null" % (i, nodes[i]))

