from adblockparser import AdblockRules

ra = open("output.txt", 'r')
rads = ra.readline()
reads = rads.split(",")

rules = [
"||ads.example.com^",
"@@||ads.example.com/notbanner^$~script",
]
abp = AdblockRules(rules)
# write data into ads file
wa = open("kq.txt", 'w')
list_ads = []
count = 0
total = 0
for iad in reads:
    total += 1
result = abp.should_block(iad)
if iad in list_ads:
    count += 1
list_ads.append(iad)
ads = wa.write(iad+'\n')
print (iad)
print (count)