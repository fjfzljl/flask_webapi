import grequests
import time



start = time.time()
req_list = [
    grequests.get("http://localhost/kvstore/Superstore"),
    grequests.get("http://localhost/kvstore/Costco"),
    grequests.get("http://localhost/kvstore/LondonDrug"),
    grequests.get("http://localhost/kvstore/ShoppersDrug"),
    grequests.get("http://localhost/kvstore/Walmart"),
    grequests.get("http://localhost/kvstore/TT")
]

res_list = grequests.map(req_list)
print("duration:" + str(time.time()-start))
print(res_list)