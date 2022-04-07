ra = open("input.txt",'r')
rads = ra.readline()
reads = rads.split(",")
rop = open("rules.txt", 'r')
rules = rop.readline()
from adblockparser import AdblockRules
abp = AdblockRules(rules)
# write data into ads file
wa = open("output.txt",'w')
list_ads = []
count_TRUE = 0
total = 0
for iad in reads:
 total += 1
 result = abp.should_block(iad)
 if result and iad not in list_ads:
    count_TRUE += 1
 list_ads.append(iad)
 ads = wa.write(iad+'\n')