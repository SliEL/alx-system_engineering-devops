# Increase file open limits for holberton user
file_line {'increase_holberton_soft_limit':
  path   => '/etc/security/limits.conf',
  line   => 'holberton soft nofile 4096',
  match  => '^holberton soft nofile',
  ensure => present,
}

file_line {'increase_holberton_hard_limit':
  path   => '/etc/security/limits.conf',
  line   => 'holberton hard nofile 8192',
  match  => '^holberton hard nofile',
  ensure => present,
}

# Ensure PAM applies these limits
file_line {'ensure_pam_limits':
  path   => '/etc/pam.d/common-session',
  line   => 'session required pam_limits.so',
  ensure => present,
}
