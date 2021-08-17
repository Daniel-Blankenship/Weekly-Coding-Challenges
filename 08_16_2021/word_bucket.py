def bucketize(phrase, max_characters):

    phrase_list = phrase.split()

    output = []
    bucket = ""

    for word in phrase_list:
        # if the word can fit in an empty bucket
        if len(word) <= max_characters:
            # if the bucket is partially filled
            if len(bucket) > 0:
                # if the word fits in the partially filled bucket
                if len(bucket + word) + 1 <= max_characters:
                    bucket += " " + word
                else:
                    # empty the bucket into the output so the word can fit
                    output.append(bucket)
                    bucket = word
            else:
                bucket = word
        else:
            # returns an empty array if the entire phrase can't be bucketized
            return []

    # if there is anything left over in the bucket, add it to the output
    if len(bucket) > 0:
        output.append(bucket)
    
    return output


print(bucketize("she sells sea shells by the sea", 10))
print(bucketize("she sells sea shells by the sea", 2))
print(bucketize("the mouse jumped over the cheese", 7))
print(bucketize("fairy dust coated the air", 20))
print(bucketize("a b c d e", 2))