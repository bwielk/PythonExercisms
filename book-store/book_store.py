def calculate_total(books):
    result = 0

    books_in_cart = {}
    for book in books:
        if book not in books_in_cart.keys():
            books_in_cart[book] = 1
        else:
            books_in_cart[book] += 1

    result = result + calculating_purchase_on_n_of_different_books(books_in_cart)
    result = result + two_groups_of_4_is_cheaper_than_group_of_5_plus_group_of_3_and_group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(books_in_cart)
    result = result + two_each_of_first_4_books_and_1_copy_each_of_rest(books_in_cart)
    result = result + group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(books_in_cart)
    result = result + two_copies_of_each_book(books_in_cart)
    result = result + three_copies_of_first_book_and_2_each_of_remaining(books_in_cart)
    result = result + three_each_of_first_2_books_and_2_each_of_remaining_books(books_in_cart)
    result = result + four_groups_of_4_are_cheaper_than_2_groups_each_of_5_and_3(books_in_cart)
    return result

def calculating_purchase_on_n_of_different_books(cart):
    discout_on_num_of_books = {1: 1,
                               2: 0.95,
                               3: 0.9,
                               4: 0.8,
                               5: 0.75}
    num_of_book_types = len(cart)
    if len(cart.values()) <= 1:
        return list(cart.values())[0]*800 if len(cart.values()) == 1 else 0
    elif all(num == 1 for num in cart.values()):
        return num_of_book_types*(discout_on_num_of_books[num_of_book_types]*800)
    else:
        return 0

def two_groups_of_4_is_cheaper_than_group_of_5_plus_group_of_3_and_group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(cart):
    if len(cart) == 5 and list(cart.values()).count(1) == 2:
        return 8*(0.8*800)
    else:
        return 0

def group_of_4_plus_group_of_2_is_cheaper_than_2_groups_of_3(cart):
    if len(cart) == 4 and any(num > 1 for num in cart.values()):
        return 4*(0.8*800) + 2*(0.95*800)
    else:
        return 0

def two_each_of_first_4_books_and_1_copy_each_of_rest(cart):
    if len(cart) == 5 and list(cart.values()).count(1) == 1:
        return 5*(0.75*800) + 4*(0.8*800)
    else:
        return 0

def two_copies_of_each_book(cart):
    if len(cart) == 5 and all(num == 2 for num in cart.values()):
        return 10*(0.75*800)
    else:
        return 0

def three_copies_of_first_book_and_2_each_of_remaining(cart):
    if len(cart) == 5 and list(cart.values()).count(3) == 1:
        return 10*(0.75*800)+800
    else:
        return 0

def three_each_of_first_2_books_and_2_each_of_remaining_books(cart):
    if len(cart) == 5 and list(cart.values()).count(3) == 2:
        return 10*(0.75*800)+2*(0.95*800)
    else:
        return 0

def four_groups_of_4_are_cheaper_than_2_groups_each_of_5_and_3(cart):
    if len(cart) == 5 and any(num > 3 for num in cart.values()):
        return 4*4*(0.8*800)
    else:
        return 0