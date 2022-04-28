#!/bin/bash

for f in $(find ./descriptions -name "*.md" )
do
    htmlFile=$(echo $f | sed -e 's/\.md$/\.html/g')
    marked -o "$htmlFile" -i "$f" --gfm --breaks --smart-lists
done
