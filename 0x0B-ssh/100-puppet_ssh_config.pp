# Ensures that there is a holberton file in tmp
file_line { '~/.ssh/config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  line   => 'PasswordAuthentication no',
}
