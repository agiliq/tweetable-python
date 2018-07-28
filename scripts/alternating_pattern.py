#Generates alternating pattern of two characters
'\n'.join([(x+1)*'#'+(7-x)*'*' for x in range(7)])
