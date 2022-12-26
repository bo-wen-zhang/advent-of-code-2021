def part_one_solution():
    with open('input.txt') as f:
        bin_nums = list(map(lambda x : [int(y) for y in list(x.strip())], f.readlines()))
        bit_sums = [sum([num[i] for num in bin_nums]) for i in range(len(bin_nums[0]))]
        half = len(bin_nums) // 2
        gamma_rate = int(''.join(list(map(lambda x: '1' if x>half else '0', bit_sums))), 2)
        epsilon_rate = int(''.join(list(map(lambda x: '1' if x<half else '0', bit_sums))), 2)
        print(gamma_rate*epsilon_rate)

if __name__ == '__main__':
    part_one_solution()