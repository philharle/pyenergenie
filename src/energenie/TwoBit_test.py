# test_encoder.py  27/03/2016  D.J.Whale
#
# Test the OOK message encoder

import TwoBit

def ashex(data):
    if type(data) == list:
        line = ""
        for b in data:
            line += str(hex(b)) + " "
        return line
    else:
        return str(hex(data))


#----- TEST APPLICATION -------------------------------------------------------

print("*" * 80)

ALL_ON         = TwoBit.encode_switch_message(True)
ALL_OFF        = TwoBit.encode_switch_message(False)
ONE_ON         = TwoBit.encode_switch_message(True, device_address=1)
ONE_OFF        = TwoBit.encode_switch_message(False, device_address=1)
TWO_ON         = TwoBit.encode_switch_message(True, device_address=2)
TWO_OFF        = TwoBit.encode_switch_message(False, device_address=2)
THREE_ON       = TwoBit.encode_switch_message(True, device_address=3)
THREE_OFF      = TwoBit.encode_switch_message(False, device_address=3)
FOUR_ON        = TwoBit.encode_switch_message(True, device_address=4)
FOUR_OFF       = TwoBit.encode_switch_message(False, device_address=4)
MYHOUSE_ALL_ON = TwoBit.encode_switch_message(True, house_address=0x12345)

tests = [ALL_ON, ALL_OFF, ONE_ON, ONE_OFF, TWO_ON, TWO_OFF, THREE_ON, THREE_OFF, FOUR_ON, FOUR_OFF, MYHOUSE_ALL_ON]

for t in tests:
    print('')
    print(ashex(t))

# END


