#Maintainer: Doug Beney <contact@dougie.io>
pkgname=obanyconf
pkgver=0.0.1
pkgdesc='A script to use any configuration file type to configure openbox.'
arch=(any)
license=(GPL)
url="https://github.com/DougBeney/obanyconf"
depends=(python python-pip)
source=(
  https://github.com/DougBeney/obanyconf/archive/master.zip
)

package ()
{
  cd "$srcdir/$pkgname-$pkgver"
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps anymarkup
  python3 setup.py install --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm755 "$srcdir/$pkgname-$pkgver/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
