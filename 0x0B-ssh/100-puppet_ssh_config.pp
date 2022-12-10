# Config file using puppet
include stdlib

file_line { 'Turn off passwd auth':
  ensure             => created,
  path               => '/etc/ssh/ssh_config'
  line               => '    PasswordAuthentication no',
  replace            => true,
  append_on_no_match => true
}

file_line { 'Declare identity file':
  ensure             => created,
  path               => '/etc/ssh/ssh_config',
  line               => '     IdentityFile ~/.ssh/school',
  replace            => true,
  append_on_no_match => true
}
