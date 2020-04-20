#!/bin/sh

python texttest_fixture.py > gm.txt

git diff gm.txt