def test_packages(host):
    pkg = host.package('httpd')
    assert pkg.is_installed


def test_files(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
