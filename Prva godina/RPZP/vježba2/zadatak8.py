# G. zamjena
# Za dani string zamjeni svaku brojčanu znamenku s "*", svako slovo s "-",
# a ostale znakove s "?"
# npr za dani string "pi=3.14" će dobiveni string izgledati "--?*?**"
def zamjena(s):
    ns = ''
    for slovo in s:
        if slovo.isdigit():
            ns += '*'
        elif slovo.isalpha():
            ns += '-'
        else:
            ns += '?'

    return ns


print(zamjena('pi=3.14'))
