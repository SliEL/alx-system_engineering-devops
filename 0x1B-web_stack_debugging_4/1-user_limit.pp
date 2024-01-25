# Puppet manifest to increase file descriptor limits for the 'holberton' user and configure PAM

exec { 'increase_holberton_nofile_limit':
  command => "echo 'holberton - nofile 4096' >> /etc/security/limits.conf",
  unless  => "grep -q 'holberton - nofile 4096' /etc/security/limits.conf",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}

exec { 'ensure_pam_limits_module':
  command => "echo 'session required pam_limits.so' >> /etc/pam.d/common-session",
  unless  => "grep -q 'session required pam_limits.so' /etc/pam.d/common-session",
  path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/'],
}
