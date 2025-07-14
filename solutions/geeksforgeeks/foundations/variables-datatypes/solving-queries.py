# https://www.geeksforgeeks.org/batch/python-foundation/track/Python-Foundation-Data-Types/problem/solving-queries

class Solution:
    def Query(self, dict, query):
        # return a list of query outputs
        res = []
        for key in query:
            res.append(dict.get(key, "None"))
        return res