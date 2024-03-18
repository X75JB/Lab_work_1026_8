episode4 = {"Luke","Leia","Han","Chewie","C3PO","R2D2","Vader","Greedo","Kenobi"}
episode5={"Luke","Leia","Han","Chewie","C3PO","R2D2","Vader","Tauntaun","Yoda","Lando"}
episode6={"Luke","Leia","Han","Chewie","C3PO","R2D2","Vader","Palpatine","Ackbar","Jabba","Rancor","Boba"}

unEps = episode4.union(episode5, episode6)
interEp45 = episode4.intersection(episode5)
final = episode6.difference(interEp45)

print(final)