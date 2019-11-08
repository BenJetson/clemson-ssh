# clemson-ssh-config-generator

Script to create SSH host aliases for Clemson SoC machines.

This is an UNOFFICIAL script, and is NOT CREATED NOR ENDORSED BY Clemson University
or the School of Computing.

## Why is this useful?

Save your fingers! Instead of typing all of this:

```
ssh user@host#.computing.clemson.edu
```

Just use the hostname and number!

```
ssh host#
```

Or even better, don't type the number either. The script will randomly select
a host number for you when you generate the configuration.

```
ssh host
```

## Show me how!

It's easy. Download a copy of the script and run it in one line:

```
python3 <(curl -s https://raw.githubusercontent.com/BenJetson/clemson-ssh-config-generator/master/generator.py)
```

Then just follow the prompts.

## What does the script actually do?

It modifies your `~/.ssh/config` file and adds host aliases for the SoC 
machines. For each machine, it writes this to the file:

```
Host <hostname>
	HostName <hostname>.computing.clemson.edu
	User <username>
```

## Will this work on Windows?

No, sorry. SSH clients on Windows format their configuration files differently
from the standard SSH config file format used on *nix platforms.
