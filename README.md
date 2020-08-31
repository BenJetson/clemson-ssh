# clemson-ssh

Script to create SSH host aliases for Clemson SoC machines.

This is an UNOFFICIAL script, and is NOT CREATED NOR ENDORSED BY Clemson University
or the School of Computing.

## Why is this useful?

Save your fingers! Instead of typing all of this:

```shell
ssh user@host#.computing.clemson.edu
```

Just use the hostname and number!

```zsh
ssh host#
```

Or even better, don't type the number either. The script will randomly select
a host number for you when you generate the configuration.

```zsh
ssh host
```

## What about off campus?

At the time of writing, all of us Clemson students are taking classes online, so
off campus SSH is the norm.

Ordinarily, you'd have to manually `ssh` to the `access` node first and then
`ssh` to the box you really want. Fortunately, `ssh` has a built-in option to
do this for you, called proxy jumping.

The script will automatically set the access node as a proxy for you, unless
you tell it not to during the setup wizard.

## Show me how!

It's easy. Download a copy of the script and run it in one line:

```zsh
python3 <(curl -s https://raw.githubusercontent.com/BenJetson/clemson-ssh/master/generator.py)
```

Then just follow the prompts.

## What does the script actually do?

It modifies your `~/.ssh/config` file and adds host aliases for the SoC
machines. For each machine, it writes this to the file:

```sshconfig
Host <hostname>
	HostName <hostname>.computing.clemson.edu
	User <username>
	ProxyJump access  # if you use proxy jumpbox
```

## Will this work on Windows?

No, sorry. SSH clients on Windows (like PuTTY) format their configuration
differently from the standard SSH config file format used on \*nix platforms.

**UNLESS** you are using the Windows Subsystem for Linux, of course! Then you
can run this script from inside a WSL terminal just like any other \*nix box.
