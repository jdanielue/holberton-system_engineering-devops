# script that set up your client SSH configuration file
file_line { '~/.ssh/config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/holberton',
  line   => '   PasswordAuthentication no',
}
