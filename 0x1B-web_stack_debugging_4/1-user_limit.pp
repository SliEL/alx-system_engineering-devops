# Puppet manifest to configure system limits and PAM to address 'Too many open files' issue for 'holberton' user

# Manage the /etc/security/limits.conf file directly
file { '/etc/security/limits.conf':
  ensure  => file,
  content => template('path/to/your/template/limits.conf.erb'),
}

# Ensure PAM applies these limits
file_line { 'ensure_pam_limits':
  ensure => present,
  path   => '/etc/pam.d/common-session',
  line   => 'session required pam_limits.so',
}
