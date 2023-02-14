from functools import reduce
def part_one_solution():
    with open('input.txt') as f:
        bin_nums = list(map(lambda x : [int(y) for y in list(x.strip())], f.readlines()))
        bit_sums = [sum([num[i] for num in bin_nums]) for i in range(len(bin_nums[0]))]
        half = len(bin_nums) // 2
        gamma_rate = int(''.join(list(map(lambda x: '1' if x>half else '0', bit_sums))), 2)
        epsilon_rate = int(''.join(list(map(lambda x: '1' if x<half else '0', bit_sums))), 2)
        print(gamma_rate*epsilon_rate)
        
def part_two_solution():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    
    #oxygen generator rating
    
    bit_idx = 0
    number_of_bits = len(lines[0])
    numbers = lines
    while len(numbers) > 1 and bit_idx < number_of_bits:
        number_of_numbers = len(numbers)
        number_of_ones = reduce(lambda x, y: x+int(y[bit_idx]), numbers, 0)
        most_common_bit = '0' if number_of_ones < number_of_numbers/2 else '1'
        remaining_numbers = list(filter(lambda x: x[bit_idx] == most_common_bit, numbers))
        numbers = remaining_numbers
        bit_idx += 1
        
    oxy_rating = bin_to_den(int(numbers[0]))
    
    #CO2 scrubber rating
    
    bit_idx = 0
    number_of_bits = len(lines[0])
    numbers = lines
    while len(numbers) > 1 and bit_idx < number_of_bits:
        number_of_numbers = len(numbers)
        number_of_ones = reduce(lambda x, y: x+int(y[bit_idx]), numbers, 0)
        least_common_bit = '1' if number_of_ones < number_of_numbers/2 else '0'
        remaining_numbers = list(filter(lambda x: x[bit_idx] == least_common_bit, numbers))
        numbers = remaining_numbers
        bit_idx += 1
        
    co2_rating = bin_to_den(int(numbers[0]))
    
    print(oxy_rating*co2_rating)
    
def bin_to_den(binary_number):
    denary_number = 0
    unit_value = 1
    while binary_number:
        if binary_number % 2 == 1:
            denary_number += unit_value
        binary_number = binary_number // 10
        unit_value *= 2

    return denary_number            

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()