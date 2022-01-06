# pytunneling

**NOTE: This module has not been completed but is functional. Use at own risk.**

## Description

Python module that allows multi-hop SSH tunneling/port-forwarding.

While modules like [Paramiko](https://github.com/paramiko/paramiko) and [sshtunnel](https://github.com/pahaz/sshtunnel) provide excellent SSH and SSH tunnelling functionality (and is what is used under the hood for this module), neither directly support multi-hop SSH tunneling commonly required in heavily firewalled environments or complex network structure that may not have direct connectivity.

The logic to this module progressively creates tunnels (that use the previous tunnel if applicable) based on your input until the final tunnel is created which is what is reported as the localport for you to use as you please. This may look something like; desktop 22<>22 bastion1 22<>22 bastion2 22<>5432 database server. Refer to usage below.

## Install

### Pip

```bash
pip install pytunneling
```

## Requirements

* Python 3.6 or greater

## Usage

### Import as Python module

Note: `tunnel_info` argument expects a list of dictionary objects containing keyword arguments noted in the [sshtunnel docs](https://sshtunnel.readthedocs.io/en/latest/#sshtunnel.SSHTunnelForwarder) corresponding to the bastion "hops", with the actual destination IP and port being `target_ip` and `target_port`.

```python
from pytunneling import TunnelNetwork
from time import sleep
tunnel_info = [
    {"ssh_address_or_host": "bastion1",
    "ssh_username": "sshuser",
    "ssh_pkey": "~/.ssh/id_rsa", # Note this refers to a local file on the machine that runs logic
    #"ssh_private_key_password ": "somekeypassword", # If applicable
    },
    {"ssh_address_or_host": "bastion2",
    "ssh_username": "sshuser",
    "ssh_password": "somesecurepassword",
    }
]
with TunnelNetwork(tunnel_info=tunnel_info, target_ip="database", target_port=5432) as tn:
    print(f"Tunnel available at localhost:{tn.local_bind_port}")
    while True:
        # Use this tunnel
        sleep(5)
```

### CLI

#### CLI Usage

**Note: The CLI is not yet implemented** 

```bash
# TODO
```

#### CLI Examples

```bash
# TODO
```

## Known Issues

* Currently this module will time out when an SSH thumbprint prompt appears (seen for first time SSH usage), be sure to validate SSH connection/credentials works. To investigate whether there is an option to accept or avoid this.

## Contributing

Feel free to raise any feature requests/problems/improvements as issue or pull request via [GitHub](https://github.com/mattykay/pytunneling).
