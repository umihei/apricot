#!/bin/bash

try() {
    expected="$1"
    input="$2"

    /home/local/python373/bin/python3.7 apricot.py "$input" > tmp.s
    gcc -o tmp tmp.s
    ./tmp
    actual="$?"

    if [ "$actual" = "$expected" ]; then
        echo "$input => $actual"
    else
        echo "$expected expected, but got $actual"
        exit 1
    fi
}

try 0 0
try 42 42
try 21 '5+20-4'
try 21 '5 + 20 - 4'

echo OK

