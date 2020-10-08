# What about off campus?

At the time of writing, all of us Clemson students are taking classes online, so
off campus SSH is the norm.

Ordinarily, you'd have to manually `ssh` to the `access` node first and then
`ssh` to the box you really want. Fortunately, `ssh` has a built-in option to
do this for you, called proxy jumping.

The script will automatically set the access node as a proxy for you, unless
you tell it not to during the setup wizard.

More information:

> [SoC: Off Campus Access](https://computing.clemson.edu/help/remoteaccess.html)
