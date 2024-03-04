def bagOfTokensScore(tokens, power):
    # Sort tokens để lấy điểm bằng lượng power ít nhất và lấy được
    # lượng power nhiều nhất
    tokens.sort()

    score = 0
    max_score = 0
    # Khởi tạo 2 con trỏ trái và phải
    left, right = 0, len(tokens) - 1

    # Duyệt qua các token.
    # Nếu power >= tokens[left] thì chúng ta sẽ đổi tokens[left] power lấy score.
    # Ngược lại, chúng ta sẽ đổi score lấy power từ tokens[right] để nhận về
    # nhiều power nhất.

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            left += 1
            score += 1
            max_score = max(max_score, score)
        elif (
            score > 0
        ):  # Lượng power không thể đổi lấy tokens ở bên trái nữa => Đổi điểm lấy power
            power += tokens[right]
            right -= 1
            score -= 1
        else:  # Nếu cả 2 điều kiện trên không thỏa mãn thì thoát khỏi vòng lặp
            break

    return max_score
