# Extract tarballs
This is a little tool to unpack a folder full of tarballs. The reason I created this instead of using the `tar` tool available on almost every platform, was because I wanted to extract all of the tarballs in the directory at once, and I was not sure how to do that without scripting it. And to ensure cross platform compatibility, I wrote this in Python instead of bash.

# Usage

> **NOTE:** This was only tested on `Python v3.8.2`. 

Copy the script to the location containing the tarballs and run through the terminal.

To get usage help:

```
python extract_tarballs.py --help
```

And to run it:

```
python extract_tarballs.py <tarball_location> <extraction_destination>
```

> **NOTE:** In the current implementation, you only have to specify the relative file location for either `tarball_location` or `extraction_destination`, but this is relative to the location of the `extract_tarballs.py` script. For example, using `python extract_tarballs.py . dest` would take the tarball location to be the directory containing the script and would assume `dest` is directory within that too. Therefore, ensure the script `extract_tarballs.py` is copied to the correct location before used.