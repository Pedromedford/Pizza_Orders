"""
Pizza Ordering Test
"""
def parse_input_file(filename):

    with open(filename) as order_file:
        line_list = []

        for line in order_file:
            data_row = line.split()
            line_list.append(data_row)

    return (line_list)

def pizzeria_information(pizza_info):

    num_pizzas_available = pizza_info[0]
    num_two_person_teams = pizza_info[1]
    num_three_person_teams = pizza_info[2]
    num_four_person_teams = pizza_info[3]

    return(num_pizzas_available,num_two_person_teams, num_three_person_teams, num_four_person_teams)

def pizza_order(pizza_info, num_team_members):

    ingredients = 0
    total_ingredients = []
    unique_ingredients = []

    for pizza in pizza_info[:num_team_members]:

        ingredients += int(pizza[0])

        for ingredient in pizza[1:]:

            total_ingredients.append(ingredient)

            if ingredient in unique_ingredients:
                pass
            else:
                unique_ingredients.append(ingredient)

    return(total_ingredients, unique_ingredients)

def main():

    input_data = parse_input_file("b_little_bit_of_everything.in")

    pizza_info = input_data.pop(0)
    pizza_ingredients_list = input_data

    num_pizzas_available, num_two_person_teams, num_three_person_teams, num_four_person_teams = pizzeria_information(pizza_info)

    #test

    delivery_score = 0
    counter = 0
    log = []
    num_deliveries = 0

    for teams in range (int(num_two_person_teams)):

        total_ingredients, unique_ingredients = pizza_order(pizza_ingredients_list,2)
        delivery_score +=  len(unique_ingredients)**2
        counter +=2
        num_deliveries +=1
        log.append([2, counter -2, counter - 1])
        print("Delivery #",num_deliveries, "Score:", delivery_score)

        pizza_ingredients_list.pop(0)
        pizza_ingredients_list.pop(0)

    for teams in range(int(num_three_person_teams)):

        total_ingredients, unique_ingredients = pizza_order(pizza_ingredients_list, 3)
        delivery_score += len(unique_ingredients) ** 2
        counter += 3
        num_deliveries += 1
        log.append([3, counter - 3, counter - 2, counter - 1])
        print("Delivery #", num_deliveries, "Score:", delivery_score)

        pizza_ingredients_list.pop(0)
        pizza_ingredients_list.pop(0)


    while (counter <= 496):

        total_ingredients, unique_ingredients = pizza_order(pizza_ingredients_list, 4)
        delivery_score += len(unique_ingredients) ** 2
        counter += 4
        num_deliveries += 1
        log.append([4, counter - 4, counter - 3, counter - 2, counter - 1])
        print("Delivery #", num_deliveries, "Score:", delivery_score)

        pizza_ingredients_list.pop(0)
        pizza_ingredients_list.pop(0)

    with open ("submission_file.txt","w") as sub_file:

        sub_file.writelines(str(num_deliveries)+"\n")

        for log_item in log:

            string_ints = [str(num) for num in log_item]
            str_of_ints = " ".join(string_ints)

            sub_file.write(str_of_ints+"\n")

if __name__ == "__main__":
    main()

