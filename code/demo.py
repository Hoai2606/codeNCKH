from adblockparser import AdblockRules
EASYLIST_FILE = "rules.txt"
OUTPUT_URL = "input.txt"
ADS_URL = "output.txt"
rop = open("rules.txt", 'r')
rules = rop.readlines()

# open file and read file have iframe
ra = open(OUTPUT_URL, 'r')
rads = ra.readline()
reads = rads.split(",")
abp = AdblockRules(rules)
# write data into ads file
wa = open(ADS_URL, 'w')
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
    # print iad
    # print result
    # print "------------------------"
    # print count_TRUE
    # print str(total)
    # print str((count_TRUE*1.0/total)*100) + "%"
