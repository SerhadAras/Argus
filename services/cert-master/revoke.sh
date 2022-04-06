#!/bin/sh
$STEP_CLI ca revoke --root=$ROOT_CRT --ca-url=$CA_URL $1
