# install flask using puppet
exec {'flask':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.5.0',
}
