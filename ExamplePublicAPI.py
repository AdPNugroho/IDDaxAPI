import API
# Public API untuk pair btc_idr
# Pair yang tersedia :
# - btc_idr         - bts_btc    
# - bch_idr         - drk_btc
# - btg_idr         - doge_btc
# - eth_idr         - eth_btc
# - etc_idr         - ltc_btc
# - ignis_idr       - nxt_btc
# - ltc_idr         - ten_btc
# - nxt_idr         - str_btc
# - ten_idr         - nem_btc
# - waves_idr       - xrp_btc
# - str_idr
# - xrp_idr 
# - xzc_idr 
btc = API.Public('btc_idr')

print(btc.getTrades()) # Trade Pair
print(btc.getDepth()) # Value Depth Pair
print(btc.getTicker()) # Harga Pair