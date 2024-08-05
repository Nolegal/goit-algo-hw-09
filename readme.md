#Резултати Динамічного програмування:
Best coin to use for 137 is 50
        Show how best result was calculated
Current sum is 137
Found that for the sum 137 the best coin to use is 50
Calculating next value of sum to search...
Current sum is 87
Found that for the sum 87 the best coin to use is 50
Calculating next value of sum to search...
Current sum is 37
Found that for the sum 37 the best coin to use is 25
Calculating next value of sum to search...
Current sum is 12
Found that for the sum 12 the best coin to use is 10
Calculating next value of sum to search...
Current sum is 2
Found that for the sum 2 the best coin to use is 2
Calculating next value of sum to search...
Time taken for find_min_coins: 0.622813 seconds

 Show how best result was calculated
Current sum is 12
Found that for the sum 12 the best coin to use is 6
Calculating next value of sum to search...
Current sum is 6
Found that for the sum 6 the best coin to use is 6
Calculating next value of sum to search...
Time taken for find_min_coins: 0.008088 seconds





#Результати Жадібного алгоритму
 Case for [50, 25, 10, 5, 2, 1] and sum: 137
Result for find_coins_greedy: {50: 2, 25: 1, 10: 1, 2: 1}
Time taken for find_coins_greedy: 0.004593 seconds
Result for find_coins_greedy_slow: {50: 2, 25: 1, 10: 1, 2: 1}
Time taken for find_coins_greedy_slow: 0.006175 seconds
Result for find_coins_greedy_fast: {50: 2, 25: 1, 10: 1, 2: 1}
Time taken for find_coins_greedy_fast: 0.004233 seconds

        Case for [10, 6, 1] and sum: 12
Result for find_coins_greedy: {10: 1, 1: 2}
Time taken for find_coins_greedy: 0.002842 seconds
Result for find_coins_greedy_slow: {10: 1, 1: 2}
Time taken for find_coins_greedy_slow: 0.003635 seconds
Result for find_coins_greedy_fast: {10: 1, 1: 2}
Time taken for find_coins_greedy_fast: 0.003433 seconds

        Case for [25, 10, 5, 2, 1] and sum: 543210
Result for find_coins_greedy: {25: 21728, 10: 1}
Time taken for find_coins_greedy: 0.004255 seconds


Часова складність жадібного алгоритму O(n), часова складність динамічного програмування близко O(1).
Жадібний алгоритм є набагато швидшим за динамічне програмування навіть на малих проміжках данних.



