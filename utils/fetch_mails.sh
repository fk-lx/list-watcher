#/bin/bash
d="$(date +%Y-%m-%d)"
curl -XPOST 'http://localhost:5000/api/synchronise' --data since=$d