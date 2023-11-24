#!/usr/bin/pup
# install a specific version of flask

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}