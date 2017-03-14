import os
import subprocess

def test_kvm():
    subprocess.check_call(["wget", "https://downloads.openwrt.org/chaos_calmer/15.05.1/x86/kvm_guest/openwrt-15.05.1-x86-kvm_guest-combined-ext4.img.gz"])
    subprocess.check_call(["gunzip", "openwrt-15.05.1-x86-kvm_guest-combined-ext4.img.gz"])
    subprocess.check_call(["kvm", "--nographic", "openwrt-15.05.1-x86-kvm_guest-combined-ext4.img"])

    assert False
