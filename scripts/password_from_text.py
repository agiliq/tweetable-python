# Generate Pronounceable passwords from a text file
def generate_pronounceable_password(words_file='/usr/share/dict/words', num_words=4):
    import random
    words=open(words_file).read().split()
    return "-".join([random.choice(words) for _ in range(num_words)])

def test_generate_pronounceable_password():
    assert generate_pronounceable_password() != generate_pronounceable_password()