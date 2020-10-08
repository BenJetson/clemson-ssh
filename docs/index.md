# `clemson-ssh` Documentation

Script to create SSH host aliases for Clemson SoC machines.

This is an UNOFFICIAL script, and is NOT CREATED NOR ENDORSED BY Clemson
University or the School of Computing.

## Why is this useful

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

## Show me how

It's easy. Download a copy of the script and run it in one line:

```zsh
python3 <(curl -s https://raw.githubusercontent.com/BenJetson/clemson-ssh/master/generator.py)
```

Then just follow the prompts.

## FAQ

- [What about off-campus?](agent.html)
- [What does this script actually do?](technical.html)
- [Will this work on Windows?](windows.html)
- [What is SSH agent forwarding and what are the risks?](agent.html)

## Official Resources

- [CU: Acceptable Use Policy](https://idp.clemson.edu/password/policy.html)
- [SoC: Linux Accounts](https://computing.clemson.edu/help/virtual.html)
- [SoC: SSH](https://computing.clemson.edu/help/ssh.html)
- [SoC: Off Campus Access](https://computing.clemson.edu/help/remoteaccess.html)
- [SoC: Remote Desktop](https://computing.clemson.edu/help/virtual.html)
