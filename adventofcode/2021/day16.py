import fileinput
import math

def to_bin(hex_packet):
    total_len = len(hex_packet) * 4
    return format(int(hex_packet, 16), f'0>{total_len}b')

# offset , size
# 0, 3: version
# 3, 3: typeID

# typeID
# 4: literal value (single binary number, sequences of 5 bits)
# other: operator (contains one or more packets)
#   lengthTypeID
#       0: next 15 bits are number that represents total length of all sub-packets
#       1: next 11 bits are number of sub-packets
#   subpacket

# returns (bits_parsed, version_sum, value), parses one packet
def parse(packet):
    # print(packet, len(packet))
    version = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)
    version_sum = version
    offset = 6
    value = -1
    # print(version, type_id)
    if type_id == 4: # literal
        literal = ''
        while (1):
            bingroup = packet[offset:offset+5]
            offset += 5
            is_last = (bingroup[0] == '0')
            literal += bingroup[1:]
            if is_last:
                break
        value = int(literal, 2)
    else: # operator
        length_type_id = int(packet[offset],2)
        offset += 1

        subpacket_vals = []
        if length_type_id == 0: # 15-bit number, total length of subpackets
            total_bits_to_parse = int(packet[offset:offset+15], 2)
            offset += 15
            # print('total_bits_to_parse', total_bits_to_parse)
            total_bits_parsed = 0
            while total_bits_parsed < total_bits_to_parse:
                bits_parsed, subpacket_sum, subval = parse(packet[offset:])
                subpacket_vals.append(subval)
                offset += bits_parsed
                total_bits_parsed += bits_parsed
                version_sum += subpacket_sum
        else: # 11-bit number, total num packets
            total_packets_to_parse = int(packet[offset:offset+11], 2)
            offset += 11
            # print('total_packets_to_parse', total_packets_to_parse)
            for _ in range(total_packets_to_parse):
                bits_parsed, subpacket_sum, subval = parse(packet[offset:])
                subpacket_vals.append(subval)
                offset += bits_parsed
                # print('bits_parsed',bits_parsed)
                version_sum += subpacket_sum

        # print(subpacket_vals)
        if type_id == 0: # sum
            value = sum(subpacket_vals)
        elif type_id == 1: # prod
            value = math.prod(subpacket_vals)
        elif type_id == 2: # min
            value = min(subpacket_vals)
        elif type_id == 3: # max
            value = max(subpacket_vals)
        elif type_id == 5: # greater than
            assert(len(subpacket_vals) == 2)
            if subpacket_vals[0] > subpacket_vals[1]:
                value = 1
            else:
                value = 0
        elif type_id == 6: # less than
            assert(len(subpacket_vals) == 2)
            if subpacket_vals[0] < subpacket_vals[1]:
                value = 1
            else:
                value = 0
        elif type_id == 7: # equal to
            assert(len(subpacket_vals) == 2)
            if subpacket_vals[0] == subpacket_vals[1]:
                value = 1
            else:
                value = 0

    # note: final padding on outer packet ignored

    # print('   final offset',offset)
    return (offset, version_sum, value)

# O(O(O(L)))
# 100010100000000001001010100000000001101010000000000000101111010001111000

# 100
# 010 (operator)
# 1 (length type, num packets)
# 00000000001 (num packets)

# 001
# 010 (operator)
# 1 (length type, num packets)
# 00000000001 (num packets)
#
# 101
# 010 (operator)
# 0 (length type, total length)
# 000000000001011 (length 11)
#
# 110
# 100 (literal)
# 0 (last)
# 1111 (value 15)
#
# 000 (padding)
# packet = '8A004A801A8002F478'
#------------------------------------

# 110
# 001 (operator)
# 0 (length type, total length)
# 000000001000000 (64 bytes)
# 000
# 000 (operator)
# 0 (length type, total length)
# 00000101100001000101010110001011001000100000000010000100011000111000110100
# packet = '620080001611562C8802118E34'
#----
# packet = 'C0015000016115A2E0802F182340'
# packet = 'A0016C880162017C3686B18A3D4780'
packet = '8054F9C95F9C1C973D000D0A79F6635986270B054AE9EE51F8001D395CCFE21042497E4A2F6200E1803B0C20846820043630C1F8A840087C6C8BB1688018395559A30997A8AE60064D17980291734016100622F41F8DC200F4118D3175400E896C068E98016E00790169A600590141EE0062801E8041E800F1A0036C28010402CD3801A60053007928018CA8014400EF2801D359FFA732A000D2623CADE7C907C2C96F5F6992AC440157F002032CE92CE9352AF9F4C0119BDEE93E6F9C55D004E66A8B335445009E1CCCEAFD299AA4C066AB1BD4C5804149C1193EE1967AB7F214CF74752B1E5CEDC02297838C649F6F9138300424B9C34B004A63CCF238A56B71520142A5A7FC672E5E00B080350663B44F1006A2047B8C51CC80286C0055253951F98469F1D86D3C1E600F80021118A124261006E23C7E8260008641A8D51F0C01299EC3F4B6A37CABD80252211221A600BC930D0057B2FAA31CDCEF6B76DADF1666FE2E000FA4905CB7239AFAC0660114B39C9BA492D4EBB180252E472AD6C00BF48C350F9F47D2012B6C014000436284628BE00087C5D8671F27F0C480259C9FE16D1F4B224942B6F39CAF767931CFC36BC800EA4FF9CE0CCE4FCA4600ACCC690DE738D39D006A000087C2A89D0DC401987B136259006AFA00ACA7DBA53EDB31F9F3DBF31900559C00BCCC4936473A639A559BC433EB625404300564D67001F59C8E3172892F498C802B1B0052690A69024F3C95554C0129484C370010196269D071003A079802DE0084E4A53E8CCDC2CA7350ED6549CEC4AC00404D3C30044D1BA78F25EF2CFF28A60084967D9C975003992DF8C240923C45300BE7DAA540E6936194E311802D800D2CB8FC9FA388A84DEFB1CB2CBCBDE9E9C8803A6B00526359F734673F28C367D2DE2F3005256B532D004C40198DF152130803D11211C7550056706E6F3E9D24B0'
print(parse(to_bin(packet))[1])

# packet = 'C200B40A82'
# packet = '04005AC33890'
# packet = '9C0141080250320F1802104A08'
# packet = 'CE00C43D881120'
print(parse(to_bin(packet))[2])
