# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Configure Nginx default site with custom 404 page and custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    server_name _;

    rewrite ^/redirect_me https://www.github.com/SliEl permanent;

    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
      internal;
    }

    add_header X-Served-By $hostname;

    location / {
      root /var/www/html;
      index index.html index.htm;
    }
  }",
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Test Nginx configuration
exec { 'nginx-test':
  command => 'nginx -t',
  path    => '/usr/sbin',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx after implementing the changes
service { 'nginx':
  ensure    => running,
  subscribe => File['/etc/nginx/sites-available/default'],
}
