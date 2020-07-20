#!/bin/sh
###############
# run_electrumx
###############

# configure electrumx
export COIN=LavaTestnet
export DAEMON_URL=http://test:test@127.0.0.1:18332
export NET=testnet
export CACHE_MB=400
export DB_DIRECTORY=/root/.electrumx/testnet.db
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
export SERVICES=tcp://:20998,ssl://:20999,rpc://:8001
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

