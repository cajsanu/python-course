# Write your solution here

import random
import string

def generate_strong_password(amount: int, boolean1, boolean2):
    letters = string.ascii_lowercase
    specials = "!?=+-()#"
    numbers = string.digits
    let_num_together = "".join(letters + numbers)
    let_spec_together = "".join(letters + specials)
    all_together = "".join(letters + specials + numbers)
    first = ""
    if boolean1 and boolean2:
        first = random.choice(letters) + random.choice(specials) + random.choice(numbers)
        password = first + "".join(random.sample(all_together, amount-3))
    elif boolean1:
        first = random.choice(letters) + random.choice(numbers)
        password = first + "".join(random.sample(let_num_together, amount-2))
    elif boolean2:
        first = random.choice(letters) + random.choice(specials)
        password = first + "".join(random.sample(let_spec_together, amount-2))
    else: 
        password = "".join(random.sample(letters, amount))

    return password


# for i in range(10):
#     print(generate_strong_password(8, False, True))