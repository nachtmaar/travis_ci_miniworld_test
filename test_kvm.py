import os
import subprocess
import time
import signal

def test_kvm():
    subprocess.check_call(["wget", "https://downloads.openwrt.org/chaos_calmer/15.05.1/x86/kvm_guest/openwrt-15.05.1-x86-kvm_guest-combined-ext4.img.gz"])
    subprocess.check_call(["gunzip", "openwrt-15.05.1-x86-kvm_guest-combined-ext4.img.gz"])
    proc = subprocess.Popen(["kvm", "--nographic", "openwrt-15.05.1-x86-kvm_guest-combined-ext4.img"])
    time.sleep(10)
    os.kill(proc.pid, signal.SIGINT)

    assert False
