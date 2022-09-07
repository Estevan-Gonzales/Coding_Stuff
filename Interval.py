# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
    tuples_merged = []
    start_length = 0
    end_length = 1
    while start_length != end_length:
        start_length = end_length
        for current_tuple in tuples_list:
            for compare_tuple in tuples_list:
                if current_tuple != compare_tuple:
                    if ((current_tuple[0] <= compare_tuple[0] and current_tuple[1] >= compare_tuple[0]) or \
                    (current_tuple[1] >= compare_tuple[0] and current_tuple[1] <= compare_tuple[1])):
                        tuples_merged.append((min(current_tuple[0], compare_tuple[0]), max(current_tuple[1], compare_tuple[1])))
                        try:
                            tuples_merged.remove(compare_tuple)
                        except:
                            pass
        tuples_list = [*set(tuples_merged)]
        end_length = len(tuples_list)
    return tuples_list

# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    tuples_lengths = []
    for t in tuples_list:
        tuples_lengths.append(t[1] - t[0] + 1)

    min_range = 2
    tuples_sorted = []
    while min_range <= max(tuples_lengths):

        tuples_intermediate = []


        for t in range(len(tuples_list)):
            if tuples_lengths[t] == min_range:
                tuples_intermediate.append(tuples_list[t])

        lowest = -100
        while lowest <= 100:
            for t in tuples_intermediate:
                if t[0] == lowest:
                    tuples_sorted.append(t)
            lowest += 1
        min_range += 1

    return tuples_sorted


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():

  # open file intervals.in and read the data and create a list of tuples
    import sys
    intervals = []
    print(" ")
    with open(sys.argv[1], 'r') as file: #
        n_intervals = 0
        for line in file:
            line = line.strip().split(' ')
            try:
                tup = (int(line[0]), int(line[1]))
                intervals.append((tup))
            except:
                n_intervals = (line[0])

  # merge the list of tuples
    tuples_merged = merge_tuples(intervals)

  # sort the list of tuples according to the size of the interval
    tuples_sorted = sort_by_interval_size(tuples_merged)
  # run your test cases
    '''
    print (test_cases())
    '''

  # write the output list of tuples from the two functions
    print(tuples_sorted)
if __name__ == "__main__":
  main()
