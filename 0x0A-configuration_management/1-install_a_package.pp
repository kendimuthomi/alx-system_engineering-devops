# install flask using puppet
exec {'flask':
  command => '/usr/bin/apt-get -y pip3 install flask -v 2.1.0',
}
