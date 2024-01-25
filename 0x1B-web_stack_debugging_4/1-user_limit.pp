#increase file open limits for holberton user
file_line { 'increase_holberton_soft_limit':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton soft nofile 4096',
  match  => '^holberton soft nofile',
}

file_line { 'increase_holberton_hard_limit':
  ensure => present,
  path   => '/etc/security/limits.conf',
  line   => 'holberton hard nofile 8192',
  match  => '^holberton hard nofile',
}

file_line { 'ensure_pam_limits':
  ensure => present,
  path   => '/etc/pam.d/common-session',
  line   => 'session required pam_limits.so',
}
