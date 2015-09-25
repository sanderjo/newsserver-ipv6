#!/bin/sh

lynx --dump 'http://www.reddit.com/r/usenet/wiki/providers' | grep -i -e " http://" -e " https://" | awk -F/ '{ print $3 }' | awk -F. '{ print $(NF-1) "." $NF } ' | sort -u

