#/bin/bash

ip=$(dig +short google.com A @$1 | head -n 1)
if [[ $ip && $? -eq 0 ]]; then
    echo "DNS query successful, running traceroute..."
else
    echo "DNS query unsucessful"
    exit 0
fi
traceroute $ip | tail -n 3
ping $ip -c 5
