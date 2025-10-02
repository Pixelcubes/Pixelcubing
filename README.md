Features: Slot Machine sort that I came up with whilst working on something fun (procrastinating).
Completely pointless and for fun only.

Takes in input as a list of size N

Algorithm:
1) Computes target by sorting the list first. (making it extra useless)
2) Defines slot boundaries by taking the min and max of the element(s) in the list.
3) Initialises an empty array for use in storing generated slot numbers.
4) From 0 to n-1, generates ONE number AT A TIME within boundaries (both endpoints inclusive) and appends to empty array.
5) When generated list matches length of input list, check if bingo (sorted).
6) If not sorted, discards the whole array entirely and starts from scratch.
7) Continues until list is "sorted".
