#!/bin/sh
$STEP_CLI ca certificate --root=$ROOT_CRT --ca-url=$CA_URL $1 $2 $3
