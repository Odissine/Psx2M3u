# Psx2M3u
Script to create M3u with PSX Files (cue, chd, ccd, ...)
I modified this script to add Cdi file (Dreamcast)

You just have to put this file into your PSX directories
Having Python installed on your computer

Launch this file
He check all files into directories and sub directories
If file is cue, chd, etc .. (see EXT values on top of files if you want to add new one or exotic one) 
it create a m3u file with the file into and if another file containing Disc or something ... it added to m3u

Some issues :
When disc name is [Leon Disc] [Claire Disc] for instance, it create two m3u files (what we want) but title is [Claire and [Leon instead of [Claire Disc] etc ... no big deal but it should be corrected soon.

Add Exception to not split Disc, Cd etc into name of game (like Discworld for instance ^^)

Readme is in progress writing ;)
