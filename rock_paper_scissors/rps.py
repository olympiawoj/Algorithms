#!/usr/bin/python

"""


- Use recursion to generate all permutations of plays given an input n rounds which is # of plays
- n = 2 has 9 permutations


n = permutations
0 = 0
1 = 0
2 = 9
["rr", "rp", "rs", "pr", "pp", "ps", "sr, "sp", "ss"]

3 = 27
["rrr", "rrp", "rrs", "rpr", "rsr", "rrp", "rrs", "rss", "rpp"

"ppp", "ppr", "pps", "prp", psp",
"prr", "pss", "prs", "psr"

"sss", "ssr, "ssp", "srs", "sps",
"srr", "spp", "spr", "srp
]

2^2 =3
3^2 = 27



"""

import sys

# n is the num of rounds

# n is number of rounds


def rock_paper_scissors(n):
    options = ["rock", "paper", "scissors"]
    results = []
    # Base case ends recursion
    if n <= 0:
        return [[]]

    # inner recursive function
    def recurse(arr, n):
        if n == 0:
            results.append(arr)
            return

        # loop through all options, for every option in rps
        for option in options:
            # Call recurse function, conatenating new_arr with the option
            recurse(arr + [option], n - 1)

    recurse([], n)
    print(f"n: {n}, length of results {len(results)}")
    return results


print(rock_paper_scissors(3))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
