# install flask using puppet
exec {'flask':
  command => 'pip3 install flask -v 2.1.0',
  path    => '/usr/bin/',
}
