INTRODUCTION
============
**FindWords** is command line utility for searching the unix words file. Just pass a regular expression as an argument, and all matches will be printed to standard out.

INSTALLATION
------------  
1.  Save _./FindWords/findwords.py_ to your local file system in your PYTHONPATH

REQUIREMENTS
------------
 * OS X or another *nix system whose words file path is _/usr/share/dict/words_ 
 * Python 2.5.1 or greater 
 
USAGE
----- 
\>>> python findwords.py ^a{2}  
aa  
aal  
aalii  
aam  
aardvark  
aardwolf

LICENSE
-------  
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)