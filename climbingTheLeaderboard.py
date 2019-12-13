# Climbing The Leaderboard
def climbingLeaderboard(scores, alice):
    for i in range(len(alice)):
        newScores, newScores[-1] = scores, alice[i]
        scoreSet = list(set(newScores))
        # print(scoreSet[])


scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))

climbingLeaderboard(scores, alice)
