class Solution:
    def mergeSimilarItems(self, items1, items2):
        d = {}

        # items1 ke values add karo
        for i in items1:
            value = i[0]
            weight = i[1]

            if value in d:
                d[value] = d[value] + weight
            else:
                d[value] = weight

        # items2 ke values add karo
        for i in items2:
            value = i[0]
            weight = i[1]

            if value in d:
                d[value] = d[value] + weight
            else:
                d[value] = weight

        ans = []

        # dict ko list me convert karo
        for key in d:
            ans.append([key, d[key]])

        # sort by value
        ans.sort()

        return ans