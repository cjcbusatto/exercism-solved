#!/usr/bin/env bash

word=${1^^}
score=0
for i in $(seq 1 ${#word})
do
    case ${word:i-1:1} in
        A|E|I|O|U|L|N|R|S|T)
            score=$((score+1));;
        D|G)
            score=$((score+2));;
        B|C|M|P)
            score=$((score+3));;
        F|H|V|W|Y)
            score=$((score+4));;
        K)
            score=$((score+5));;
        J|X)
            score=$((score+8));;
        Q|Z)
            score=$((score+10));;
    esac
done

echo $score
exit 0