#!/bin/zsh

YEAR="${1}"
DAY="${2}"

DAY_FORMATTED=`printf "%02d" $DAY`
SESSION_KEY=$(<session_key.txt)

URL="https://adventofcode.com/$YEAR/day/$DAY/input"

cd ../y$YEAR/

#copy template dir
cp -R day00/ day$DAY_FORMATTED/
cd day$DAY_FORMATTED

#rename code file
mv day00.py Day$DAY_FORMATTED.py

#download input
curl $URL -H "cookie: session=$SESSION_KEY" -o input.txt

pwd