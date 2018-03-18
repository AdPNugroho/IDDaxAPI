import API
Secret = 'YOUR-SECRET-KEY'
Key = 'YOUR-API-KEY'

interact = API.Private(Key,Secret)

interact.getInfo()
interact.transHistory()
interact.tradeHistory('btc_idr')
interact.transHistory()
interact.openOrders()
interact.orderHistory('btc_idr')
interact.getOrder(5177699,'nxt_idr')
interact.cancelOrder(5177699,'sell','nxt_idr')
interact.trade('nxt_idr','sell',20000,10,'nxt')