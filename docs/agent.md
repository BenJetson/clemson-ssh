# About SSH Agent Forwarding

This article explains what you must know prior to enabling SSH agent forwarding.

## What is SSH Agent Forwarding

The SSH Agent is a helper program which you may use to broker secure access to
your SSH identity/keys. Once keys have been added to the agent, they may be used
without re-prompting for the key passphrase.

This trades security for convenience.

The following article has a nice illustration explaining this:

> <http://unixwiz.net/techtips/ssh-agent-forwarding.html#fwd>

## Security Implications

When you use this on your local computer, you can be reasonably assured of which
programs may be taking advantage of the services offered by this agent.

The forwarding option makes the SSH agent of your local host computer available
to the remote server by forwarding the socket. Disk permissions for this socket
on the remote host will (when configured correctly) only allow your user on the
remote host to access this socket.

HOWEVER, any user with root access to the remote host can also access this
socket!

Recommended reading from SecuritySE:

> <https://security.stackexchange.com/q/101783>

## Your Choice

THEREFORE, you must **_fully trust_** the administrators of the remote server
when using this option. **Only you** can decide if **you** trust the
administrators of the SoC to not do this.

For this reason, the option for SSH agent forwarding defaults to **off** for
this script.

If this risk is acceptable to you and you would like the convenience, you may
request SSH forwarding when running the script.
