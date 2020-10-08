# What does the script actually do?

It modifies your `~/.ssh/config` file and adds host aliases for the SoC
machines. For each machine, it writes this to the file:

```sshconfig
Host <hostname>
    HostName <hostname>.computing.clemson.edu
    User <username>
    ProxyJump access  # if you use proxy jumpbox
    ForwardAgent yes  # if you request agent forwarding (off by default)
```
