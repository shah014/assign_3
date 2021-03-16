def name_style(string, seperator):
    a = ' '
    for i in range(1, len(string)):
        string = ''.join(a + x if x.isupper() else x for x in string).strip(a).split(a)
        snake_case = "_".join(string).lower()
        kebab_case = seperator.join(string).lower()
        return snake_case, kebab_case


print(name_style('ThisIsCamelCase', '-'))