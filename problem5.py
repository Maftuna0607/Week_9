def parse_markdown(text):
    result=""
    list_of_words = text.replace(".","").split()
    for i in range(len(list_of_words)):
        if list_of_words[i][:2] == list_of_words[i][-2:] == "**":
            list_of_words[i] ="<b>" + list_of_words[i][2:-2] + "</b>"
        elif list_of_words[i][0] == list_of_words[i][-1] == "_":
             list_of_words[i] ="<i>" + list_of_words[i][1:-1] + "</i>"
    result = " ".join(list_of_words)+"."
    return result

print(parse_markdown("This is **bold** text."))
print(parse_markdown("Hello _world_."))
print(parse_markdown("Make **this** bold and _this_ italic."))
print(parse_markdown("No formatting here."))
print(parse_markdown("**Bold** at start."))