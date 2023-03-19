# train-ticket-auto-query

Train Ticket Auto Query Python Scripts (Modified by Leo)

## Configure address
Modify base_address in atomic_queries.py to specify the address of your microservices. 
This works currently, but in case you use some other files, make sure
to modify the base_address in those files also. Some ports also need to be changed
to the exact port of the target service.

## How to use

python3 normal_request_manager.py 2> {YOUR_FILE}
