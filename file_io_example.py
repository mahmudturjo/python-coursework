def write_scores(filename, scores):
    with open(filename, "w") as file:
        for score in scores:
            file.write(str(score) + "\n")


def read_scores(filename):
    scores = []
    with open(filename, "r") as file:
        for line in file:
            scores.append(int(line.strip()))
    return scores


if __name__ == "__main__":
    filename = "scores.txt"
    scores = [85, 90, 78, 92]

    write_scores(filename, scores)
    loaded_scores = read_scores(filename)

    print("Scores:", loaded_scores)
    print("Average:", sum(loaded_scores) / len(loaded_scores))
