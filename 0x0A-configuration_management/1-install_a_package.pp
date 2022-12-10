# install flask using puppet
exec {'flask':
  command => 'pip install flask -v 2.1.0',
}
