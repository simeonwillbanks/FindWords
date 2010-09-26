#!/usr/bin/env python
# encoding: utf-8
"""
findwords.py

Use functional programming to find specific words from words standard file.
http://en.wikipedia.org/wiki/Words_(Unix)

Created by Simeon F. Willbanks on 2010-09-23.

Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

"""


from __future__ import with_statement
import re
import sys
import getopt


# Comparison program exit statuses 
# 0 to indicate success
EXIT_STATUS_SUCCESS = 0
# 1 to indicate a mismatch
EXIT_STATUS_MISMATCH = 1
# 2 to indicate an inability to compare
EXIT_STATUS_CANT_COMPARE = 2


class UsageError(Exception):
    """UsageError class extends Exception.
    Provides a graceful way to exit on program usage error.
    
    """
    def __init__(self, msg):
        self.msg = str(msg).capitalize()


def wordslist():
    """Read shared words file into a list"""
    # It is good practice to use the with keyword when dealing with file 
    # objects. This has the advantage that the file is properly closed after 
    # its suite finishes, even if an exception is raised on the way.
    with open('/usr/share/dict/words', 'r') as wfile:
        wlist = map(lambda word: word.strip(), wfile.readlines())
    return wlist
    

def wordsfilter(unfilterd, pattern):
    """Filter list of words by a regex and return a list"""
    regex = re.compile(pattern)
    return filter(lambda word: regex.search(word), unfilterd)

    
def wordsout(wordlist):
    """Render all words in a list"""
    for word in wordlist:
        print word


def main(argv=None):
    """
    Find words from words standard file via regex. 
    First and only argument should be a regex pattern.

    >>> python findwords.py ^a{2}
    aa
    aal
    aalii
    aam
    aardvark
    aardwolf

    """
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.GetoptError, msg:    
            raise UsageError(msg)
        if opts:
            print main.__doc__
            return EXIT_STATUS_SUCCESS
        argslength = len(args)
        if argslength > 1:
            tense = len(args[1:]) > 1 and 's' or ''
            invalid = " ".join(args[1:])
            raise UsageError("invalid argument%s: %s" % (tense, invalid))
        elif argslength == 0:
            raise UsageError("regex pattern argument is required")
        # Program passed a regex pattern, so look for words
        wordsfound = wordsfilter(wordslist(), args[0])
        if wordsfound:
            wordsout(wordsfound)
            return EXIT_STATUS_SUCCESS
        else:
            print "No words found"
            return EXIT_STATUS_MISMATCH
    except UsageError, err:
        # Extended print form or "print chevron"
        # An expression is written to a "file-like" object
        # In this case, write messages to standard error
        print >> sys.stderr, err.msg
        print >> sys.stderr, "For help use --help"
        return EXIT_STATUS_CANT_COMPARE
    

if __name__ == '__main__':
    sys.exit(main())