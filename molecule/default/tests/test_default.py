import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bash_package(host):
    pkg = host.package("bash")
    assert pkg.is_installed


def test_bash_completion_package(host):
    pkg = host.package("bash-completion")
    assert pkg.is_installed


def test_shellcheck_package(host):
    pkg = host.package("ShellCheck")
    assert pkg.is_installed


def test_bats_package(host):
    pkg = host.package("bats")
    assert pkg.is_installed
