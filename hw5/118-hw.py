#RTTs = [100, 150, 80, 75]
RTTs = [100]

a = 1/8
B = 1/4
SRTT = RTTs[0]
DevRTT = RTTs[0]/2
RTO = SRTT + 4*DevRTT

for rtt in RTTs[1:]:
    diff = rtt - SRTT
    SRTT = SRTT + a*diff
    DevRTT = DevRTT + B*(abs(diff) - DevRTT)
    RTO = SRTT + 4*DevRTT

for name, val in zip(['SRTT', 'DevRTT', 'RTO'], [SRTT, DevRTT, RTO]):
    print(name + ':', val)
