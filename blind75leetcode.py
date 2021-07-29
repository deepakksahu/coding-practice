import json
import requests

questions = ["two-sum",
    "longest-substring-without-repeating-characters",
    "longest-palindromic-substring",
    "container-with-most-water",
    "3sum",
    "remove-nth-node-from-end-of-list",
    "valid-parentheses",
    "merge-two-sorted-lists",
    "merge-k-sorted-lists",
    "search-in-rotated-sorted-array",
    "combination-sum",
    "rotate-image",
    "group-anagrams",
    "maximum-subarray",
    "spiral-matrix",
    "jump-game",
    "merge-intervals",
    "insert-interval",
    "unique-paths",
    "climbing-stairs",
    "set-matrix-zeroes",
    "minimum-window-substring",
    "word-search",
    "decode-ways",
    "validate-binary-search-tree",
    "same-tree",
    "binary-tree-level-order-traversal",
    "maximum-depth-of-binary-tree",
    "construct-binary-tree-from-preorder-and-inorder-traversal",
    "best-time-to-buy-and-sell-stock",
    "binary-tree-maximum-path-sum",
    "valid-palindrome",
    "longest-consecutive-sequence",
    "clone-graph",
    "word-break",
    "linked-list-cycle",
    "reorder-list",
    "maximum-product-subarray",
    "find-minimum-in-rotated-sorted-array",
    "reverse-bits",
    "number-of-1-bits",
    "house-robber",
    "number-of-islands",
    "reverse-linked-list",
    "course-schedule",
    "implement-trie-prefix-tree",
    "design-add-and-search-words-data-structure",
    "word-search-ii",
    "house-robber-ii",
    "contains-duplicate",
    "invert-binary-tree",
    "kth-smallest-element-in-a-bst",
    "lowest-common-ancestor-of-a-binary-search-tree",
    "lowest-common-ancestor-of-a-binary-tree",
    "product-of-array-except-self",
    "valid-anagram",
    "meeting-rooms",
    "meeting-rooms-ii",
    "graph-valid-tree",
    "missing-number",
    "alien-dictionary",
    "encode-and-decode-strings",
    "find-median-from-data-stream",
    "longest-increasing-subsequence",
    "coin-change",
    "number-of-connected-components-in-an-undirected-graph",
    "counting-bits",
    "top-k-frequent-elements",
    "sum-of-two-integers",
    "pacific-atlantic-water-flow",
    "longest-repeating-character-replacement",
    "non-overlapping-intervals",
    "serialize-and-deserialize-bst",
    "subtree-of-another-tree",
    "palindromic-substrings",
    "longest-common-subsequence"]


def get_query(question):
    query = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": question
        },
        "query": "query questionData($titleSlug: String!) {question(titleSlug: $titleSlug) {    questionId    questionFrontendId   title    titleSlug   isPaidOnly    difficulty  }}"
    }
    return query

url = "https://leetcode.com/graphql"

def main():
    quesdata = []
    for i, question in enumerate(questions):
        print("working on {}. {}".format(i, question))
        query = get_query(question)
        resp = requests.get(url, json=query)
        if resp.status_code != 200:
            print("failed for question {} with response {}".format(question, resp.json()))
            continue
        data = resp.json()['data']['question']

        quesdata.append(
            {
                "question": data['title'],
                "free": not data['isPaidOnly'],
                "difficulty": data['difficulty'],
                "slug": data['titleSlug'],
                "id": data['questionId']
            }
        )
        # break
    print(quesdata)
    with open("questiondata.json","w+") as f_:
        f_.write(json.dumps(quesdata))

main()