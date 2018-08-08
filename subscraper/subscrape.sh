#!/bin/bash
for url in $(cat $2)
    do
        wget $url.$1;
        sleep 2;
        grep "href=" index.html | cut -d"/" -f3 | grep "\." | cut -d'"' -f1 | sort -u | cut -d"." -f1 | sort -u >> $3;
        mv index.html $url.index.html
    done
