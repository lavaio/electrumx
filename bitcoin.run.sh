#!/bin/sh
###############
# run_electrumx
###############

# configure electrumx
export COIN=BitcoinSegwit
export DAEMON_URL=http://test:test@127.0.0.1:8332
#export DAEMON_URL=http://whh:whh@172.31.239.208:9332
export NET=mainnet
export CACHE_MB=400
export DB_DIRECTORY=/root/.electrumx/bitcoin.db
export SSL_CERTFILE=/root/.electrumx/server.crt
export SSL_KEYFILE=/root/.electrumx/server.key
#export BANNER_FILE=/home/username/.electrumx/banner
#export DONATION_ADDRESS=your-donation-address
export ALLOW_ROOT=True
# connectivity
#export HOST=0.0.0.0
#export TCP_PORT=60998
#export TCP_PORT=50001
#export SSL_PORT=60999
#export SSL_PORT=60000
export SERVICES=tcp://:60998,ssl://:60999
# visibility
#export RPC_HOST=0.0.0.0
#export RPC_PORT=8000

# run electrumx
ulimit -n 65535
#/root/wdy/git-repo/electrumx/electrumx_server.py 2>> /root/.electrumx/electrumx.log >> /root/.electrumx/electrumx.log &

######################
# auto-start electrumx
######################

# add this line to crontab -e
# @reboot /path/to/run_electrumx.sh

