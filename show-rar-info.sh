#!/usr/bin/sh
# Show info of rar file: RAR type, volume number, contents

echo -n $1 " --- "
unrar l $1 | grep -e "^Details:" | cut -c10-
echo -n " --- " 
unrar l $1 | grep -P '\d{4}-\d{2}-\d{2}' | cut -c42- | tr "\n" "  "
echo " " 
