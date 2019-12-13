def angryProfessor(k, a):
    early = 0
    for i in a:
        if i <= 0:
            early = early + 1
    return "NO" if early >= k else "YES"
