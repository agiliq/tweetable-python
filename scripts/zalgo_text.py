import random as r
u='̡̢̧̨̖̗̘̙̜̝̞̟̠̣̤̥̦̩̪̫̬̭̮̯̰̱̲̳̹̺̻̼͇͈͉͍͎͓͔͕͖͙͚͜͟͢ͅM̴̵̶̷̸'
o = "'̛̀́̂̃̄̅̆̇̈̉̊̋̌̍̎̏̐̑̒̓̔̽̾̿̀́͂̓̈́͆͊͋͌͐͑͒͗͛̕̚͘͝͞͠͡'"
def zalgo(txt):
    return str(b"".join([b"".join([el] + [r.choice(o+u) for _ in range(r.randint(0,6))])
                    for el in txt]), 'utf-8')

print(zalgo("He comes, he comes, the center cannot hold, it is too late"))
