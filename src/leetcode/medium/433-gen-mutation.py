from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        possible_gens = ["A", "C", "G", "T"]

        queue = deque()
        queue.append(startGene)
        visited = {startGene}

        min_mutations = 0
        while queue:
            min_mutations += 1
            for _ in range(len(queue)):
                mutation = queue.popleft()
                for index in range(len(mutation)):
                    mutation_list = list(mutation)
                    for gen in possible_gens:
                        mutation_list[index] = gen
                        if (possible_mutation := "".join(mutation_list)) in bank:
                            if possible_mutation == endGene:
                                return min_mutations
                            if possible_mutation not in visited:
                                queue.append(possible_mutation)
                                visited.add(possible_mutation)
        return -1

startGene = "AAAACCCC"
endGene = "CCCCCCCC"
bank = ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]

Solution().minMutation(startGene, endGene, bank)