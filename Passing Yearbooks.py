def findSignatureCounts(arr):
    # Write your code here
    students = [i - 1 for i in arr]
    albums = [i for i in range(len(arr))]
    signs = [1 for _ in arr]
    album_index = -1
    for i in range(len(arr)):
        if albums[i] != students[i]:
            album_index = i
            break
    while album_index >= 0:
        for i in range(1, len(arr)):
            i = album_index - i
            if albums[i] == students[i]:
                continue
            signs[i] += 1
            albums[i], album_index = albums[album_index], albums[i]
            break
        else:
            album_index = -1

    return signs


if __name__ == '__main__':
    print([2, 2], findSignatureCounts([2, 1]))
    print([1, 1], findSignatureCounts([1, 2]))
    print([1, 1, 1], findSignatureCounts([1, 2, 3]))
    print([3, 3, 2], findSignatureCounts([1, 2, 3]))
