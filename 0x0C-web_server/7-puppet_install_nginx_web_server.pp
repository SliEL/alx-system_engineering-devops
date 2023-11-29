# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Ensure /var/www/html directory exists
file { '/var/www/html':
  ensure => directory,
}

# Create index.html with "Hello World!" content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Create your own Nginx default site configuration template
file { '/etc/nginx/sites-available/default.erb':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Configure Nginx using the custom template
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Configure redirect for /redirect_me
nginx::resource::location { '/redirect_me':
  ensure   => present,
  location => '^/redirect_me',
  server   => 'default',
  ssl      => false,
  proxy    => 'http://www.example.com',
  status   => '301',
  notify   => Service['nginx'],
}
