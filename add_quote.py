#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    print "Quote:"
    quote = raw_input()

    print "Source:"
    source = raw_input()

    result = """\n> {quote}  \n\n_{source}_\n\n--\n""".format(quote=quote, source=source)
    with open('README.md', 'a') as f:
        f.write(result)

if __name__ == '__main__':
    main()
