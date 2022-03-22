def solution(S, K):
    idx_to_date = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    date_to_idx = {idx_to_date[i]: i for i in range(len(idx_to_date))}

    i = (date_to_idx[S] + K) % 7
    return idx_to_date[i]
