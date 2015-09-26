#!/bin/sh
lynx --dump 'http://www.usenet-providers.nl/Vergelijk' | grep -i -e " http" | awk '{ print "lynx --dump "  $2 }'  | sort -u | /bin/sh |\
grep -i " http" | grep -vi usenet-providers.nl | awk -F/ '{ print $3 }' | awk -F\. '{ print $(NF-1) "."  $NF }' | sort -u
