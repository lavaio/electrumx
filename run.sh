#!/bin/sh
###############
# run_electrumx
###############

# configure electrumx
export COIN=Lava
export DAEMON_URL=http://test:test@127.0.0.1:8332
export NET=mainnet
export CACHE_MB=400
export DB_DIRECTORY=/root/.electrumx/mainnet.db
export SSL_CERTFILE=/root/.electrumx/server.crt
export SSL_KEYFILE=/root/.electrumx/server.key
#export BANNER_FILE=/home/username/.electrumx/banner
#export DONATION_ADDRESS=your-donation-address
export ALLOW_ROOT=True
#export LOG_LEVEL=debug
# connectivity
#export HOST=0.0.0.0
#export TCP_PORT=60998
#export TCP_PORT=50001
#export SSL_PORT=60999
#export SSL_PORT=60000
export SERVICES=tcp://:60998,ssl://:60999,rpc://:8000
# visibility
#export RPC_HOST=0.0.0.0
#export RPC_PORT=8000
#export MAX_SEND=10000000
export MAX_SEND=10000000
#export BANDWIDTH_UNIT_COST=100000000
#export INITIAL_CONCURRENT=1000
#export COST_SOFT_LIMIT=100000
#export COST_HARD_LIMIT=100000
# run electrumx
ulimit -n 1000
#/root/wdy/git-repo/electrumx/electrumx_server.py 2>> /root/.electrumx/electrumx.log >> /root/.electrumx/electrumx.log &

######################
# auto-start electrumx
######################

# add this line to crontab -e
# @reboot /path/to/run_electrumx.sh

