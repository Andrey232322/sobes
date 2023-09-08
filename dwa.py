# import glob
# import json
# import os
#
#
# zap = 'zapic`'
# def fail_est(id = 0):
#     return glob.glob(os.path.join(zap,f'*{id if id else ""}.json'))
# file = fail_est()
# b = []
# v = {}
# if file:
#     for f in file:
#         with open(f,'r', encoding='UTF-8') as q:
#             v[f] = json.load(q)
#             #b.append(json.load(q))
